import pytesseract
from PIL import Image
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def text_file(file):
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
        return None

def calculation(s_answers, t_answers, exam_type):
    marks = 0
    feedback = []
    vectorizer = TfidfVectorizer()

    for i, (student, teacher) in enumerate(zip(s_answers, t_answers)):
        if exam_type == "MCQ":
            if student.strip().lower() == teacher.strip().lower():
                marks += 1
                feedback.append(f"Q{i+1}: Correct")
            else:
                feedback.append(f"Q{i+1}: Incorrect")
        elif exam_type == "Short Answers":
            vec = vectorizer.fit_transform([student, teacher])
            simu = cosine_similarity(vec[0], vec[1])[0][0]
            if simu > 0.7:
                marks += 1
                feedback.append(f"Q{i+1}: Similar (simu: {round(simu * 100, 2)}%)")
            else:
                feedback.append(f"Q{i+1}: Not Similar (simu: {round(simu * 100, 2)}%)")
        elif exam_type == "Essay":
            s_tokens = word_tokenize(student)
            t_tokens = word_tokenize(teacher)

            corrected_s = TextBlob(student).correct()
            corrected_t = word_tokenize(str(corrected_s))
            grammer_error = len(set(s_tokens) - set(corrected_t))
            vec = vectorizer.fit_transform([student, teacher])
            simu = cosine_similarity(vec[0], vec[1])[0][0]
            marks += simu * 1

            feedback.append(f"Q{i+1}: Essay (simu: {round(simu * 100, 2)}%, Grammatical Errors: {grammer_error})")
    
    return marks, feedback
