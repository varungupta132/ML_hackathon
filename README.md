# **Automated Exam Evaluation System**

## **Project Overview**

This repository contains the code for an **Automated Exam Evaluation System** developed for a **Machine Learning Hackathon** at **GLA University**, Mathura. The system is designed to evaluate exam sheets using **Optical Character Recognition (OCR)**, **Natural Language Processing (NLP)**, and **Machine Learning (ML)** technologies. It can automatically grade **MCQ**, **Short Answer**, and **Essay** type questions.

---

## **Tech Stack**

- **Backend**: Python
  - **Tesseract OCR** (for digitizing handwritten responses)
  - **pdfplumber** (for extracting text from PDFs)
  - **TF-IDF Vectorizer** (for comparing short answers using cosine similarity)
  - **TextBlob** (for grammar correction in essays)
  - **Streamlit** (for the frontend app)
  
---

## **Features**

1. **OCR for Handwritten Responses**:
   - Uses **pytesseract** to extract text from image files (JPG, PNG, JPEG).
   - Supports text extraction from both scanned PDFs and images.

2. **Evaluation of Exam Answers**:
   - For **MCQs**, the system compares student answers with the teacher’s answer and awards marks based on exact matches.
   - For **Short Answers**, the system uses **cosine similarity** based on **TF-IDF** to measure how close the student's answer is to the teacher's answer.
   - For **Essays**, the system performs grammar correction using **TextBlob** and evaluates the similarity of the student’s answer to the teacher’s, providing feedback on grammatical errors and similarity percentage.

3. **Streamlit Web Interface**:
   - Teachers can upload student and teacher answer sheets (PDF, JPG, PNG).
   - The system displays the student's and teacher's answers, calculates marks, and provides detailed feedback.

4. **Scalable and Flexible**:
   - Works for different types of exams: **MCQs**, **Short Answers**, and **Essays**.
   - Easily deployable for different educational environments.

---

## **How It Works**

### **File Upload**
   - Both the student’s answer sheet and teacher’s answer sheet are uploaded to the system (in PDF or image format).
  
### **OCR Processing**
   - The system extracts the text from the uploaded files using **pytesseract** for images and **pdfplumber** for PDFs.

### **Answer Evaluation**
   - The system uses the **TF-IDF vectorizer** to compare the student’s and teacher’s answers for **short answer** questions.
   - For **essays**, it uses **TextBlob** for grammar correction and calculates similarity between the student’s and teacher’s answers.

### **Feedback and Results**
   - The system provides feedback for each question, showing whether the answer is correct (for MCQs), how similar it is (for short answers), or detailed feedback with grammar checks (for essays).

---

## **Setup & Installation**

### **Requirements**

- Python 3.x
- Required Python libraries:
  - `pytesseract`
  - `pdfplumber`
  - `scikit-learn`
  - `nltk`
  - `textblob`
  - `streamlit`

## Installation Steps

You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```
###Tesseract Installation:###
Download and install Tesseract OCR.
Make sure Tesseract is correctly installed and update the pytesseract.pytesseract.tesseract_cmd variable in the code with the correct path.

## Usage

### Run the Streamlit App:
Once you have installed the dependencies, you can run the app using:

```bash
streamlit run app.py
```

## Uploading Files

You will be prompted to upload both the student’s and teacher’s answer sheets.

Select the appropriate exam type:
- **MCQ**
- **Short Answers**
- **Essay**

## Results and Feedback

After uploading the files and selecting the exam type, the system will display:
- The student’s answers and the teacher’s answers.
- The **total marks scored**.
- **Detailed feedback** for each question.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

