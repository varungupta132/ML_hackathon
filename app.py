import streamlit as st
from backend import text_file, calculation

st.set_page_config(page_title="Exam Evaluation System", page_icon="📝", layout="wide")

st.title("📝 Automated Exam Evaluation System")
st.markdown("---")
st.markdown("### Upload answer sheets and get instant evaluation with AI-powered grading")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Student's Answer Sheet")
    sf = st.file_uploader("Upload Student's Answer Sheet", type=["pdf", "jpg", "png", "jpeg"], key="student")

with col2:
    st.subheader("📋 Teacher's Answer Sheet")
    tf = st.file_uploader("Upload Teacher's Answer Sheet", type=["pdf", "jpg", "png", "jpeg"], key="teacher")

st.markdown("---")
exam_type = st.selectbox("📚 Select Exam Type", ("MCQ", "Short Answers", "Essay"))

if sf and tf:
    with st.spinner("🔍 Processing files... Please wait"):
        try:
            s_text = text_file(sf)
            t_text = text_file(tf)

            if s_text and t_text:
                st.success("✅ Files processed successfully!")
                st.markdown("---")
                
                with st.expander("👨‍🎓 View Student's Answers", expanded=False):
                    st.text_area("Student Answers", s_text, height=200, disabled=True)

                with st.expander("👨‍🏫 View Teacher's Answers", expanded=False):
                    st.text_area("Teacher Answers", t_text, height=200, disabled=True)

                s_answers = [ans.strip() for ans in s_text.split("\n") if ans.strip()]
                t_answers = [ans.strip() for ans in t_text.split("\n") if ans.strip()]

                if len(s_answers) != len(t_answers):
                    st.error(f"⚠️ Mismatch in number of questions! Student: {len(s_answers)}, Teacher: {len(t_answers)}")
                else:
                    st.markdown("---")
                    marks, feedback = calculation(s_answers, t_answers, exam_type)
                    
                    # Results section with better formatting
                    st.markdown("## 📊 Evaluation Results")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Questions", len(t_answers))
                    with col2:
                        st.metric("Marks Scored", f"{marks:.2f}")
                    with col3:
                        percentage = (marks / len(t_answers)) * 100 if len(t_answers) > 0 else 0
                        st.metric("Percentage", f"{percentage:.1f}%")
                    
                    st.markdown("---")
                    st.markdown("## 💬 Detailed Feedback")
                    
                    for f in feedback:
                        if "Correct" in f or "Similar" in f:
                            st.success(f"✅ {f}")
                        else:
                            st.warning(f"❌ {f}")
            else:
                st.error("❌ Failed to extract text from files. Please ensure they are readable.")
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
else:
    st.info("👆 Please upload both Student's and Teacher's answer sheets to begin evaluation.")
