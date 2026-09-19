# **Automated Exam Evaluation System**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success)](https://varungupta132.github.io/ML_hackathon/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## **Project Overview**

This repository contains the code for an **Automated Exam Evaluation System** developed for a **Machine Learning Hackathon** at **GLA University**, Mathura. The system is designed to evaluate exam sheets using **Optical Character Recognition (OCR)**, **Natural Language Processing (NLP)**, and **Machine Learning (ML)** technologies. It can automatically grade **MCQ**, **Short Answer**, and **Essay** type questions.

🌐 **[View Live Demo](https://varungupta132.github.io/ML_hackathon/)**

---

## **✨ Features**

### **1. OCR for Handwritten Responses**
- Uses **pytesseract** to extract text from image files (JPG, PNG, JPEG)
- Supports text extraction from both scanned PDFs and images
- Handles multiple file formats seamlessly

### **2. Intelligent Answer Evaluation**
- **MCQs**: Exact match comparison with teacher's answers
- **Short Answers**: Uses **cosine similarity** based on **TF-IDF** to measure answer quality
  - >70% similarity: Full marks
  - 50-70% similarity: Partial credit
  - <50% similarity: Needs improvement
- **Essays**: 
  - Grammar correction using **TextBlob**
  - Similarity-based scoring
  - Detailed grammatical error feedback

### **3. Modern Web Interface**
- Built with **Streamlit** for easy interaction
- Upload student and teacher answer sheets (PDF, JPG, PNG)
- Real-time processing with visual feedback
- Detailed results with percentage scores
- Color-coded feedback for easy understanding

### **4. Scalable and Flexible**
- Works for different types of exams
- Easy to extend and customize
- Cross-platform compatibility

---

## **🛠️ Tech Stack**

- **Backend**: Python 3.8+
- **OCR**: Tesseract OCR, pytesseract
- **PDF Processing**: pdfplumber
- **Machine Learning**: Scikit-learn (TF-IDF, Cosine Similarity)
- **NLP**: NLTK, TextBlob
- **Frontend**: Streamlit
- **Deployment**: GitHub Pages

---

## **📋 Prerequisites**

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Tesseract OCR

---

## **🚀 Installation & Setup**

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/varungupta132/ML_hackathon.git
cd ML_hackathon
```

### **Step 2: Install Python Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 3: Install Tesseract OCR**

#### Windows:
1. Download the installer from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)
2. Install and note the installation path
3. Update the path in `backend.py` if needed (default: `C:\Program Files\Tesseract-OCR\tesseract.exe`)

#### Linux:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

#### macOS:
```bash
brew install tesseract
```

---

## **💻 Usage**

### **Run the Streamlit App**

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### **Using the Application**

1. **Upload Files**:
   - Upload the student's answer sheet (PDF/Image)
   - Upload the teacher's answer sheet (PDF/Image)

2. **Select Exam Type**:
   - Choose from: MCQ, Short Answers, or Essay

3. **View Results**:
   - See extracted answers from both sheets
   - Get total marks and percentage
   - Review detailed feedback for each question

---

## **📁 Project Structure**

```
ML_hackathon/
├── app.py              # Main Streamlit application
├── backend.py          # Core evaluation logic
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── index.html         # GitHub Pages landing page
```

---

## **🔧 How It Works**

### **1. Text Extraction**
The system extracts text from uploaded files using:
- **pytesseract** for images (JPG, PNG, JPEG)
- **pdfplumber** for PDF documents

### **2. Answer Comparison**
Different evaluation strategies based on exam type:

**MCQ**: Direct string comparison
```python
if student_answer.lower() == teacher_answer.lower():
    marks += 1
```

**Short Answers**: TF-IDF + Cosine Similarity
```python
vectorizer = TfidfVectorizer()
similarity = cosine_similarity(student_vector, teacher_vector)
```

**Essays**: NLP-based evaluation
```python
# Grammar checking
corrected = TextBlob(answer).correct()
# Similarity scoring
similarity = cosine_similarity(student_essay, teacher_essay)
```

### **3. Feedback Generation**
- Detailed feedback for each question
- Similarity percentages for subjective answers
- Grammar error counts for essays
- Overall performance metrics

---

## **🎯 Use Cases**

- **Educational Institutions**: Automate exam grading process
- **Online Learning Platforms**: Instant assessment for students
- **Test Preparation**: Self-evaluation tools
- **Teachers**: Save time on manual grading
- **Students**: Get instant feedback on practice tests

---

## **🤝 Contributing**

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## **📝 Future Enhancements**

- [ ] Support for multiple languages
- [ ] Handwriting recognition improvements
- [ ] Batch processing for multiple students
- [ ] Export results to PDF/Excel
- [ ] Integration with Learning Management Systems (LMS)
- [ ] Advanced analytics dashboard
- [ ] Mobile app version

---

## **📄 License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **👨‍💻 Author**

**Varun Gupta**
- GitHub: [@varungupta132](https://github.com/varungupta132)

---

## **🙏 Acknowledgments**

- GLA University, Mathura for organizing the ML Hackathon
- Tesseract OCR team for the amazing OCR engine
- Streamlit team for the intuitive web framework
- All contributors and users of this project

---

## **📞 Support**

If you have any questions or need help, please:
- Open an [issue](https://github.com/varungupta132/ML_hackathon/issues)
- Contact via GitHub

---

**⭐ If you find this project helpful, please consider giving it a star!**
