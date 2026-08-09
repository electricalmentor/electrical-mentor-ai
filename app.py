import streamlit as st
from scenarios.motors import motor_scenarios

if "score" not in st.session_state:
    st.session_state.score = 100

if "question" not in st.session_state:
    st.session_state.question = 1
    
    if "feedback" not in st.session_state:
    st.session_state.feedback = None
st.sidebar.title("⚡ Training Center")

category = st.sidebar.selectbox(
    "Choose Category",
    [
        "Motors"
    ]
)
scenario_choice = st.sidebar.selectbox(
    "Choose Job",
    list(motor_scenarios.keys())
)
selected_scenario = motor_scenarios[scenario_choice]
st.title("⚡ Electrical Mentor AI Simulator")
st.sidebar.divider()

st.sidebar.write("👷 Apprentice Profile")

st.sidebar.write("Level: Electrical Apprentice I")

st.sidebar.write(
    f"XP: {st.session_state.score}"
)

# Create score
if "score" not in st.session_state:
    st.session_state.score = 100

if "question" not in st.session_state:
    st.session_state.question = 1


st.subheader("Scenario #001")
st.write(selected_scenario["title"])

st.write(f"""
Equipment:
{selected_scenario['equipment']}
""")
st.info("Always follow Lockout/Tagout procedures before troubleshooting.")

st.divider()

if st.session_state.feedback:

    feedback_type, feedback_message = st.session_state.feedback

    if feedback_type == "correct":
        st.success(feedback_message)
    else:
        st.error(feedback_message)

    st.session_state.feedback = None
if st.session_state.question <= len(selected_scenario["questions"]):

    current_question = selected_scenario["questions"][
        st.session_state.question - 1
    ]

    st.write(selected_scenario["symptom"])

    answer = st.radio(
        current_question["question"],
        current_question["answers"],
        key=f"question_{st.session_state.question}"
    )

    if st.button("Submit Answer"):

        if answer == current_question["correct"]:
            st.session_state.feedback = (
                "correct",
                f"Correct! Good troubleshooting. +{current_question['points']} XP"
            )
            st.session_state.score += current_question["points"]

        else:
            st.session_state.feedback = (
                "incorrect",
                f"Incorrect. The best answer was: "
                f"{current_question['correct']}"
            )
            st.session_state.score -= 10

        st.session_state.question += 1
        st.rerun()


if st.session_state.question > len(selected_scenario["questions"]):

    st.header("Scenario Complete")

    st.write(
        f"Final Score: {st.session_state.score}/100"
    )

    if st.session_state.score >= 100:
        st.success("Electrical Apprentice Level Up!")
    else:
        st.info(
            "Keep practicing. Every electrician builds troubleshooting skills through repetition."
        )

    if st.button("Try Another Scenario"):
        st.session_state.question = 1
        st.rerun()
