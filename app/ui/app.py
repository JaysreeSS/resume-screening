import streamlit as st
import requests

st.title("Resume Screening App")

# File uploads
resume_file = st.file_uploader(
    "Upload Candidate Resume (PDF)",
    type=["pdf"]
)

jd_file = st.file_uploader(
    "Upload Job Description (PDF)",
    type=["pdf"]
)

# Show uploaded files
if resume_file is not None:
    st.success(f"Resume uploaded: {resume_file.name}")

if jd_file is not None:
    st.success(f"Job Description uploaded: {jd_file.name}")


# Process button
if resume_file is not None and jd_file is not None:

    if st.button("Evaluate Candidate"):

        with st.spinner("Analyzing resume against the job description..."):

            response = requests.post(
                "http://localhost:8000/screening/",
                files={
                    "resume": (
                        resume_file.name,
                        resume_file,
                        "application/pdf"
                    ),
                    "jd": (
                        jd_file.name,
                        jd_file,
                        "application/pdf"
                    )
                }
            )

        if response.status_code == 200:

            response_data = response.json()

            st.success("Candidate evaluation completed!")

            # Overall evaluation
            st.subheader("Overall Evaluation")
            st.metric(
                "Candidate Status",
                response_data.get(
                    "candidate_status",
                    "Not available"
                )
            )

            # Reason / summary
            st.subheader("Assessment")

            st.write(
                response_data.get(
                    "reason",
                    "No assessment available."
                )
            )

            # Skills
            st.subheader("Skills Match")

            st.progress(
                response_data.get(
                    "skill_match_percentage",
                    0
                ) / 100
            )

            st.write(
                f"Skills matched: "
                f"{response_data.get('skill_match_percentage', 0)}%"
            )

            # Matched skills
            matched_skills = response_data.get(
                "matched_skills",
                []
            )

            if matched_skills:
                st.subheader("Matched Skills")

                for skill in matched_skills:
                    st.write(f"✓ {skill}")

            # Missing skills
            missing_skills = response_data.get(
                "missing_skills",
                []
            )

            if missing_skills:
                st.subheader("Missing / Required Skills")

                for skill in missing_skills:
                    st.write(f"• {skill}")

            # Strengths
            strengths = response_data.get(
                "strengths",
                []
            )

            if strengths:
                st.subheader("Candidate Strengths")

                for strength in strengths:
                    st.write(f"✓ {strength}")

            # Gaps
            gaps = response_data.get(
                "gaps",
                []
            )

            if gaps:
                st.subheader("Candidate Gaps")

                for gap in gaps:
                    st.write(f"• {gap}")

        else:

            st.error(
                f"Error processing candidate: "
                f"{response.text}"
            )

else:
    st.info(
        "Upload both a resume and a job description "
        "to evaluate the candidate."
    )
