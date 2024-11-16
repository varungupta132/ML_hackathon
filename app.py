import streamlit as st
import pytesseract
from PIL import Image
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')  # Corrected typo

# Set the path for Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to extract text from files (PDF, images)
def text_to_file(file):
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text.strip()
    elif file.name.endswith((".jpg", ".png", ".jpeg")):
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text.strip()
    else:
        st.error("Unsupported file type. Upload a PDF or image.")
        return None

# Function to calculate marks and feedback
def calculate_marks(student_answers, teacher_answers, exam_type):
    marks = 0
    detailed_feedback = []
    vectorizer = TfidfVectorizer()

    for i, (student, teacher) in enumerate(zip(student_answers, teacher_answers)):
        if exam_type == "MCQ":
            if student.strip().lower() == teacher.strip().lower():
                marks += 1
                feedback = f"Q{i+1}: Correct"
            else:
                feedback = f"Q{i+1}: Incorrect"
        elif exam_type == "Short Answer":
            vectors = vectorizer.fit_transform([student, teacher])
            similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
            if similarity > 0.7:
                marks += 1
                feedback = f"Q{i+1}: Similar (Similarity: {round(similarity * 100, 2)}%)"
            else:
                feedback = f"Q{i+1}: Not Similar (Similarity: {round(similarity * 100, 2)}%)"
        elif exam_type == "Essay":
            student_tokens = word_tokenize(student)
            teacher_tokens = word_tokenize(teacher)

            corrected_student = TextBlob(student).correct()
            corrected_tokens = word_tokenize(str(corrected_student))
            grammatical_errors = len(set(student_tokens) - set(corrected_tokens))
            vectors = vectorizer.fit_transform([student, teacher])
            similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
            marks += similarity * 1  # You can tweak this multiplier if needed

            feedback = f"Q{i+1}: Essay (Similarity: {round(similarity * 100, 2)}%, Grammatical Errors: {grammatical_errors})"
        
        detailed_feedback.append(feedback)

    return marks, detailed_feedback


# Streamlit UI
st.title("Exam Evaluation System")

st.sidebar.header("Upload Files")
student_file = st.sidebar.file_uploader("Upload Student's Answer Sheet", type=["pdf", "jpg", "png"])
teacher_file = st.sidebar.file_uploader("Upload Teacher's Answer Sheet", type=["pdf", "jpg", "png"])

exam_type = st.selectbox("Select Exam Type", ("MCQ", "Short Answer", "Essay"))

if student_file and teacher_file:
    student_text = text_to_file(student_file)
    teacher_text = text_to_file(teacher_file)

    if student_text and teacher_text:
        st.subheader("Student's Answers")
        st.write(student_text)

        st.subheader("Teacher's Answers")
        st.write(teacher_text)

        student_answers = student_text.split("\n")
        teacher_answers = teacher_text.split("\n")

        if len(student_answers) != len(teacher_answers):
            st.error("Uploaded question has a mismatch in the no. of questions.")
        else:
            marks, feedback = calculate_marks(student_answers, teacher_answers, exam_type)
            st.subheader("Results")
            st.write(f"Total Marks Scored: {marks}/{len(teacher_answers)}")

            st.subheader("Feedback")
            for f in feedback:
                st.write(f)
