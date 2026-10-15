import streamlit as st

st.set_page_config(page_title="Grammar Quiz", page_icon="📝")

st.title("📝 English Grammar Quiz")

# Initialize session state once
if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False


def check_answer(answer):
    """Check the learner's answer and save the result."""
    st.session_state.answered = True

    if answer == "goes":
        st.session_state.score += 1


with st.form("quiz_form"):
    st.write("Choose the correct word:")

    st.write("She ___ to college every day.")

    answer = st.radio(
        "Your answer",
        ["go", "goes", "going"],
    )

    submitted = st.form_submit_button("Submit Answer")

if submitted and not st.session_state.answered:
    check_answer(answer)

if st.session_state.answered:
    if answer == "goes":
        st.success("Correct! 🎉")
    else:
        st.error("Incorrect. The correct answer is 'goes'.")

    st.write(f"Score: {st.session_state.score} / 1")

    if st.button("Try Again"):
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()
