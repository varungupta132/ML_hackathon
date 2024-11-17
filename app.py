import streamlit as st
from backend import tt_file, calculation

st.title("Exam Evaluation System")

st.sidebar.header("Upload Files")
sf = st.sidebar.file_uploader("Student's Answer Sheet", type=["pdf", "jpg", "png"])
tf = st.sidebar.file_uploader("Teacher's Answer Sheet", type=["pdf", "jpg", "png"])

exam_type = st.selectbox("Exam Type", ("MCQ", "Short Answers", "Essay"))

if sf and tf:
    s_text = tt_file(sf)
    t_text = tt_file(tf)

    if s_text and t_text:
        st.subheader("student's Answers")
        st.write(s_text)

        st.subheader("teacher's Answers")
        st.write(t_text)

        s_answers = s_text.split("\n")
        t_answers = t_text.split("\n")

        if len(s_answers) != len(t_answers):
            st.error("uploaded question has a mismatch in the number of questions.")
        else:
            marks, feedback = calculation(s_answers, t_answers, exam_type)
            st.subheader("results")
            st.write(f"total marks scored: {marks}/{len(t_answers)}")

            st.subheader("feedback")
            for f in feedback:
                st.write(f)
