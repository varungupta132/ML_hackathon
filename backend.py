import pytesseract
from PIL import Image
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
import os

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
except:
    pass

# Tesseract configuration - will work on different systems
if os.name == 'nt':  # Windows
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def text_file(file):
    """Extract text from PDF or image files"""
    try:
        if file.name.endswith(".pdf"):
            with pdfplumber.open(file) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text.strip()
        elif file.name.endswith((".jpg", ".png", ".jpeg")):
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
            return text.strip()
        else:
            return None
    except Exception as e:
        print(f"Error extracting text: {str(e)}")
        return None

def calculation(s_answers, t_answers, exam_type):
    """Calculate marks and provide feedback based on exam type"""
    marks = 0
    feedback = []
    vectorizer = TfidfVectorizer()

    for i, (student, teacher) in enumerate(zip(s_answers, t_answers)):
        if not student or not teacher:
            feedback.append(f"Q{i+1}: Empty answer provided")
            continue
            
        if exam_type == "MCQ":
            if student.strip().lower() == teacher.strip().lower():
                marks += 1
                feedback.append(f"Q{i+1}: Correct ✓")
            else:
                feedback.append(f"Q{i+1}: Incorrect (Expected: {teacher.strip()}, Got: {student.strip()})")
                
        elif exam_type == "Short Answers":
            try:
                vec = vectorizer.fit_transform([student, teacher])
                similarity = cosine_similarity(vec[0], vec[1])[0][0]
                if similarity > 0.7:
                    marks += 1
                    feedback.append(f"Q{i+1}: Good Answer - Similarity: {round(similarity * 100, 2)}%")
                elif similarity > 0.5:
                    marks += 0.5
                    feedback.append(f"Q{i+1}: Partial Credit - Similarity: {round(similarity * 100, 2)}%")
                else:
                    feedback.append(f"Q{i+1}: Needs Improvement - Similarity: {round(similarity * 100, 2)}%")
            except:
                feedback.append(f"Q{i+1}: Unable to evaluate")
                
        elif exam_type == "Essay":
            try:
                s_tokens = word_tokenize(student.lower())
                t_tokens = word_tokenize(teacher.lower())

                # Calculate similarity
                vec = vectorizer.fit_transform([student, teacher])
                similarity = cosine_similarity(vec[0], vec[1])[0][0]
                
                # Grammar checking
                corrected_s = str(TextBlob(student).correct())
                grammar_errors = len(student.split()) - len(corrected_s.split())
                
                # Award marks based on similarity
                marks += similarity
                
                feedback.append(
                    f"Q{i+1}: Essay Score - Similarity: {round(similarity * 100, 2)}%, "
                    f"Grammar Issues: {max(0, grammar_errors)}"
                )
            except Exception as e:
                feedback.append(f"Q{i+1}: Unable to evaluate essay")
    
    return round(marks, 2), feedback
