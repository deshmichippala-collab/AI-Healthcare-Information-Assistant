from health_answers import get_health_answer
import streamlit as st

st.set_page_config(
    page_title="AI Healthcare Information Assistant",
    page_icon="🏥",
    layout="wide"
)

# General information for educational demonstration only
GUIDANCE = {
    "Headache": (
        "Rest in a quiet place and drink water if appropriate. "
        "Seek medical advice if the headache persists or worries you."
    ),
    "Cold": (
        "Rest and drink fluids. Seek medical advice if symptoms worsen "
        "or you experience difficulty breathing."
    ),
    "Digestive discomfort": (
        "Consider regular meals and fluids if appropriate. "
        "Consult a healthcare professional if symptoms persist."
    ),
    "Fever": (
        "Rest and maintain fluids if you can. Seek medical advice if "
        "the fever persists or you feel seriously unwell."
    ),
    "Other": (
        "Please consult a qualified healthcare professional for "
        "guidance about your concern."
    ),
}

FAQS = {
    "What is this application?": (
        "It is a student-built educational prototype for exploring "
        "general health information."
    ),
    "Does it diagnose diseases?": (
        "No. It does not diagnose diseases, recommend prescriptions, "
        "or replace a healthcare professional."
    ),
    "Does it generate AI answers?": (
        "No. This version uses predefined information and does not "
        "connect to an AI model."
    ),
    "When should I seek medical help?": (
        "Contact a healthcare professional for personal medical advice. "
        "For a possible emergency, contact your local emergency service."
    ),
}

# Sidebar
with st.sidebar:
    st.title("🏥 Health Assistant")
    st.caption("Student project prototype")
    page = st.radio(
        "Navigation",
        ["Home", "Health FAQs", "Safety Information"]
    )
    st.divider()
    st.caption("Educational use only")

# Home page
if page == "Home":
    st.title("🏥 AI Healthcare Information Assistant")
    st.write(
        "Explore general health information through a simple "
        "interactive interface."
    )

    st.warning(
        "This educational prototype does not diagnose illnesses "
        "or replace a doctor."
    )

    st.subheader("Explore General Health Information")

    topic = st.selectbox(
        "Select a topic",
        [
            "Choose a topic",
            "Headache",
            "Cold",
            "Digestive discomfort",
            "Fever",
            "Other",
        ],
        key="topic",
    )

    if topic != "Choose a topic":
        st.markdown("### General information")
        st.info(GUIDANCE[topic])

    st.divider()
    st.subheader("Ask a General Question")

    question = st.text_area(
        "Enter your question",
        placeholder="Type a general health information question...",
        key="question",
    )

    col1, col2 = st.columns([1, 5])

    with col1:
        submit = st.button("Submit Question", type="primary")

    with col2:
        if st.button("Clear / Reset"):
            st.session_state["question"] = ""
            st.session_state["topic"] = "Choose a topic"
            st.rerun()

    if submit:
        if question.strip():
            st.info(
                "Your question has been entered successfully. "
                "This prototype does not generate AI answers yet. "
                "Consult a reliable health resource or healthcare "
                "professional for an answer."
            )
        else:
            st.error("Please enter a question first.")

# FAQ page
elif page == "Health FAQs":
    st.title("📚 Frequently Asked Questions")
    st.write("Learn about this project's features and limitations.")

    for question, answer in FAQS.items():
        with st.expander(question):
            st.write(answer)

# Safety page
elif page == "Safety Information":
    st.title("🛡️ Safety Information")
    st.write(
        "This application is a student educational prototype, "
        "not a medical device or diagnostic system."
    )

    st.subheader("Important limitations")
    st.markdown(
        """
        - Information is predefined and may not fit every person.
        - The application does not diagnose or treat conditions.
        - It does not generate AI answers in this version.
        - Do not enter names, contact details, medical records,
          or other personal health information.
        - Consult a qualified healthcare professional for personal advice.
        - For a possible medical emergency, contact local emergency services.
        """
    )

st.divider()
st.caption(
    "AI Healthcare Information Assistant | Educational prototype | "
    "Not intended for diagnosis or treatment"
)
