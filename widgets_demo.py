import streamlit as st

st.set_page_config(page_title="Grammar Practice", page_icon="📝")

st.title("📝 Grammar Practice")
st.write("Configure your English grammar exercise.")

with st.form("grammar_form"):
    learner_name = st.text_input("Your name")

    topic = st.selectbox(
        "Grammar topic",
        ["Tenses", "Articles", "Prepositions", "Subject-verb agreement"],
    )

    level = st.radio(
        "Difficulty",
        ["Beginner", "Intermediate", "Advanced"],
    )

    number_of_questions = st.slider(
        "Number of questions",
        min_value=3,
        max_value=10,
        value=5,
    )

    include_explanations = st.checkbox(
        "Show explanations after answering",
        value=True,
    )

    submitted = st.form_submit_button("Create Practice")

if submitted:
    if not learner_name.strip():
        st.warning("Please enter your name.")
    else:
        st.subheader("Your practice settings")
        st.write(f"Learner: {learner_name}")
        st.write(f"Topic: {topic}")
        st.write(f"Difficulty: {level}")
        st.write(f"Questions: {number_of_questions}")
        st.write(f"Explanations: {'Yes' if include_explanations else 'No'}")
        st.success("Practice settings submitted successfully!")
