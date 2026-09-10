import streamlit as st
from resume_analyzer import analyze_resume, generate_ai_feedback

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI Resume Analyzer")
st.caption("ATS-style resume analysis, job matching, skill gaps, and AI improvement suggestions.")

with st.sidebar:
    st.header("Settings")
    use_ai = st.toggle("Enable AI feedback", value=False)
    if use_ai:
        st.info("Add OPENAI_API_KEY in Streamlit Secrets to enable AI feedback.")
    st.divider()
    st.markdown("**Supported files:** PDF, DOCX, TXT")
    st.markdown("**Tip:** Add a job description for a more useful match score.")

uploaded = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx", "txt"],
)

job_description = st.text_area(
    "Paste the Job Description (optional)",
    height=220,
    placeholder="Example: We are looking for a Python Developer with SQL, FastAPI, Git and AWS experience..."
)

if uploaded:
    with st.spinner("Analyzing resume..."):
        result = analyze_resume(uploaded, job_description)

    if result["errors"]:
        for err in result["errors"]:
            st.error(err)
    else:
        score = result["overall_score"]
        if score >= 80:
            label = "Excellent"
        elif score >= 65:
            label = "Good"
        elif score >= 50:
            label = "Needs Improvement"
        else:
            label = "Weak"

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Overall Score", f"{score}/100")
        c2.metric("ATS Score", f'{result["ats_score"]}/100')
        c3.metric("Job Match", f'{result["job_match_score"]}/100')
        c4.metric("Skills Found", str(len(result["skills_found"])))

        st.subheader(f"Overall assessment: {label}")

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["📊 Scores", "🛠 Skills", "⚠️ Issues", "📄 Resume Text", "🤖 AI Feedback"]
        )

        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                st.write("### Score breakdown")
                st.progress(result["ats_score"] / 100, text=f'ATS / structure: {result["ats_score"]}/100')
                st.progress(result["keyword_score"] / 100, text=f'Keyword coverage: {result["keyword_score"]}/100')
                st.progress(result["job_match_score"] / 100, text=f'Job match: {result["job_match_score"]}/100')
            with col2:
                st.write("### Detected sections")
                for section, found in result["sections"].items():
                    st.write(("✅ " if found else "❌ ") + section)

        with tab2:
            left, right = st.columns(2)
            with left:
                st.write("### Skills found")
                if result["skills_found"]:
                    st.write(", ".join(result["skills_found"]))
                else:
                    st.info("No known skills were detected. Expand SKILL_LIBRARY for your target domain.")

            with right:
                st.write("### Skills missing from your resume")
                if result["missing_skills"]:
                    st.write(", ".join(result["missing_skills"]))
                else:
                    st.success("No obvious skill gaps from the current job description.")

        with tab3:
            st.write("### Issues to fix")
            for issue in result["issues"]:
                st.warning(issue)

            st.write("### Strong points")
            for point in result["strengths"]:
                st.success(point)

        with tab4:
            st.text_area(
                "Extracted resume text",
                result["text"],
                height=450,
            )

        with tab5:
            if use_ai:
                with st.spinner("Generating AI feedback..."):
                    feedback, ai_error = generate_ai_feedback(
                        result["text"],
                        job_description,
                        result,
                    )
                if ai_error:
                    st.error(ai_error)
                else:
                    st.markdown(feedback)
            else:
                st.info("Enable 'AI feedback' in the sidebar to generate LLM-based suggestions.")

        st.download_button(
            "Download analysis as JSON",
            data=result["json"],
            file_name="resume_analysis.json",
            mime="application/json",
        )
else:
    st.info("Upload a resume to start.")
