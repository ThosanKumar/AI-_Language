import streamlit as st
from datetime import date

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Streamlit Fundamentals Lab v1",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================
# 2. SESSION STATE INITIALIZATION
# =====================================================
if "score" not in st.session_state:
    st.session_state.score = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "submitted_answer" not in st.session_state:
    st.session_state.submitted_answer = None

if "activities_completed" not in st.session_state:
    st.session_state.activities_completed = []


# =====================================================
# 3. REUSABLE PYTHON FUNCTIONS
# =====================================================
def validate_name(name):
    """Return whether the supplied name is non-empty."""
    return bool(name.strip())


def evaluate_answer(answer, correct_answer):
    """Return whether an answer is correct."""
    return answer == correct_answer


def render_metric(label, value, help_text=None):
    """Reusable UI helper for a metric."""
    st.metric(label=label, value=value, help=help_text)


# =====================================================
# 4. SIDEBAR NAVIGATION
# =====================================================
st.sidebar.title("🧪 Streamlit Lab")
st.sidebar.caption("Language Tutor AI — learning prototype")

page = st.sidebar.radio(
    "Choose a lesson",
    [
        "Dashboard",
        "Widgets & Forms",
        "Grammar Quiz",
        "Session State",
        "Python Functions",
        "File Upload",
    ],
)

st.sidebar.divider()

learner_level = st.sidebar.selectbox(
    "English level",
    ["Beginner", "Intermediate", "Advanced"],
)

daily_goal = st.sidebar.slider(
    "Daily learning goal (minutes)",
    min_value=5,
    max_value=60,
    value=15,
    step=5,
)

st.sidebar.write(f"Selected level: **{learner_level}**")
st.sidebar.write(f"Daily goal: **{daily_goal} minutes**")

# =====================================================
# 5. DASHBOARD: DISPLAY ELEMENTS AND LAYOUTS
# =====================================================
if page == "Dashboard":
    st.title("🧪 Streamlit Fundamentals Lab")
    st.subheader("Build interactive applications with Python")

    st.write(
        "This lab demonstrates the main Streamlit concepts "
        "needed to build Language Tutor AI."
    )

    st.markdown(
        """
        ### Learning objectives
        - Create a user interface using Python.
        - Collect input with widgets and forms.
        - Use functions and conditional logic.
        - Preserve information using session state.
        - Build an interactive grammar quiz.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        render_metric(
            "Quiz score",
            st.session_state.score,
            "Correct answers accumulated in this session",
        )

    with col2:
        render_metric(
            "Attempts",
            st.session_state.attempts,
        )

    with col3:
        render_metric(
            "Activities completed",
            len(st.session_state.activities_completed),
        )

    st.divider()

    with st.container(border=True):
        st.subheader("Today's learning plan")
        st.write(f"Level: {learner_level}")
        st.write(f"Learning time: {daily_goal} minutes")

        if st.button("Complete sample activity"):
            if "Sample activity" not in st.session_state.activities_completed:
                st.session_state.activities_completed.append(
                    "Sample activity"
                )
            st.success("Activity completed!")

    with st.expander("What is Streamlit?"):
        st.write(
            "Streamlit is a Python framework for building "
            "interactive data and AI applications."
        )

    st.info("Use the sidebar to explore each lesson.")

# =====================================================
# 6. WIDGETS AND FORMS
# =====================================================
elif page == "Widgets & Forms":
    st.title("🧩 Widgets and Forms")

    st.write("Try different widgets used to collect learner preferences.")

    with st.form("preferences_form"):
        name = st.text_input("Learner name")

        learning_goal = st.text_area(
            "What do you want to improve?",
            placeholder="For example: grammar and vocabulary",
        )

        topics = st.multiselect(
            "Choose topics",
            ["Grammar", "Vocabulary", "Reading", "Writing", "Speaking"],
            default=["Grammar"],
        )

        difficulty = st.radio(
            "Difficulty",
            ["Beginner", "Intermediate", "Advanced"],
            horizontal=True,
        )

        study_days = st.number_input(
            "Study days per week",
            min_value=1,
            max_value=7,
            value=5,
        )

        wants_reminders = st.checkbox("Enable study reminders")

        submitted = st.form_submit_button("Save Preferences")

    if submitted:
        if not validate_name(name):
            st.warning("Please enter your name.")
        elif not topics:
            st.warning("Choose at least one learning topic.")
        else:
            st.success(f"Preferences saved for {name.strip()}!")

            st.write("### Submitted values")
            st.write(f"Learning goal: {learning_goal or 'Not specified'}")
            st.write(f"Topics: {', '.join(topics)}")
            st.write(f"Difficulty: {difficulty}")
            st.write(f"Study days per week: {study_days}")
            st.write(f"Reminders: {'Enabled' if wants_reminders else 'Disabled'}")

# =====================================================
# 7. GRAMMAR QUIZ: CONDITIONS AND FORMS
# =====================================================
elif page == "Grammar Quiz":
    st.title("📝 Grammar Quiz")

    questions = [
        {
            "question": "She ___ to college every day.",
            "options": ["go", "goes", "going"],
            "answer": "goes",
            "explanation": "Use 'goes' with he, she, or it in the simple present.",
        },
        {
            "question": "They ___ playing cricket now.",
            "options": ["is", "am", "are"],
            "answer": "are",
            "explanation": "Use 'are' with the subject 'they'.",
        },
        {
            "question": "I have lived here ___ 2020.",
            "options": ["since", "for", "during"],
            "answer": "since",
            "explanation": "Use 'since' with a starting point in time.",
        },
    ]

    question_number = st.selectbox(
        "Choose a question",
        options=list(range(len(questions))),
        format_func=lambda i: f"Question {i + 1}",
    )

    q = questions[question_number]

    st.write(q["question"])

    # Each question has its own answer widget key.
    answer = st.radio(
        "Your answer",
        q["options"],
        key=f"answer_{question_number}",
    )

    if st.button("Check Answer"):
        # Only count a question once per selected answer in this demo.
        submission_key = f"{question_number}:{answer}"

        if submission_key != st.session_state.submitted_answer:
            st.session_state.attempts += 1

            correct = evaluate_answer(answer, q["answer"])

            if correct:
                st.session_state.score += 1
                st.session_state.last_result = "correct"
            else:
                st.session_state.last_result = "incorrect"

            st.session_state.submitted_answer = submission_key

        if st.session_state.last_result == "correct":
            st.success("Correct!")
        else:
            st.error("Not quite. Review the explanation below.")

        st.info(q["explanation"])

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Correct answers", st.session_state.score)

    with col2:
        st.metric("Answer checks", st.session_state.attempts)

    if st.button("Reset quiz statistics"):
        st.session_state.score = 0
        st.session_state.attempts = 0
        st.session_state.last_result = None
        st.session_state.submitted_answer = None
        st.rerun()

# =====================================================
# 8. SESSION STATE
# =====================================================
elif page == "Session State":
    st.title("💾 Understanding Session State")

    st.write(
        "Streamlit reruns your script after many interactions. "
        "Session state preserves selected values across those reruns."
    )

    if "counter" not in st.session_state:
        st.session_state.counter = 0

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Increase counter"):
            st.session_state.counter += 1

    with col2:
        if st.button("Reset counter"):
            st.session_state.counter = 0

    st.metric("Counter value", st.session_state.counter)

    st.write("Activities completed in this session:")
    st.write(st.session_state.activities_completed or "No activities yet.")

    if st.button("Add practice activity"):
        st.session_state.activities_completed.append(
            f"Practice on {date.today().isoformat()}"
        )
        st.success("Activity added!")

    st.warning(
        "Session state is temporary. "
        "Values may reset when the browser session ends."
    )

# =====================================================
# 9. PYTHON FUNCTIONS AND CONDITIONAL LOGIC
# =====================================================
elif page == "Python Functions":
    st.title("🐍 Python Functions and Conditions")

    st.write("Enter an answer to test a reusable Python function.")

    def classify_score(score):
        if score >= 80:
            return "Excellent"
        elif score >= 50:
            return "Good progress"
        return "Keep practising"

    sample_score = st.slider(
        "Choose a sample score",
        min_value=0,
        max_value=100,
        value=70,
    )

    if st.button("Evaluate sample score"):
        feedback = classify_score(sample_score)
        st.write(f"Score: {sample_score}")
        st.success(feedback)

    st.code(
        """def classify_score(score):
    if score >= 80:
        return "Excellent"
    elif score >= 50:
        return "Good progress"
    return "Keep practising"
""",
        language="python",
    )

# =====================================================
# 10. FILE UPLOAD
# =====================================================
elif page == "File Upload":
    st.title("📁 File Upload")

    st.write("This demonstrates how Streamlit accepts an uploaded file.")

    uploaded_file = st.file_uploader(
        "Upload a text file",
        type=["txt"],
    )

    if uploaded_file is not None:
        text_content = uploaded_file.getvalue().decode(
            "utf-8",
            errors="replace",
        )

        st.success(f"Uploaded: {uploaded_file.name}")
        st.write(f"File size: {uploaded_file.size} bytes")

        with st.expander("Preview file contents"):
            st.markdown(text_content)

    st.caption(
        "Later, this pattern can be adapted for image comprehension."
    )

# =====================================================
# 11. FOOTER
# =====================================================
st.divider()
st.caption(
    "Language Tutor AI | Streamlit Fundamentals Lab | "
    "Learning prototype — no AI API or database is connected yet."
)
