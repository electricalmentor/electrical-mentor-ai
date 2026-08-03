import streamlit as st
from scenarios.motors import motor_scenarios

if "score" not in st.session_state:
    st.session_state.score = 100

if "question" not in st.session_state:
    st.session_state.question = 1
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


if st.session_state.question == 1:

   st.write(selected_scenario["symptom"])

answer = st.radio(
    "What should you do first?",
        [
            "Replace the motor",
            "Ask questions about the failure",
            "Megger the motor",
            "Replace the contactor"
        ]
    )


    if st.button("Submit Answer"):

        if answer == "Ask questions about the failure":
            st.success("Correct! Good electricians gather information first.")
            st.session_state.score += 5
        else:
            st.error("Incorrect. Do not replace parts before troubleshooting.")
            st.session_state.score -= 10

        st.session_state.question = 2


if st.session_state.question == 2:

    st.write("""
    You arrive at the MCC.

    The breaker is ON.

    What should you check next?
    """)

    answer = st.radio(
        "Choose your next step:",
        [
            "Check incoming voltage",
            "Replace the motor",
            "Check the bearings",
            "Order a new VFD"
        ]
    )


    if st.button("Submit Second Answer"):

        if answer == "Check incoming voltage":
            st.success("Correct! Verify power before moving deeper into the circuit.")
            st.session_state.score += 5
        else:
            st.error("Not the best troubleshooting step.")
            st.session_state.score -= 10

        st.session_state.question = 3


if st.session_state.question == 3:

    st.write("""
    Measurements:

    Control transformer:
    120 VAC

    Start button:
    Good

    Contactor coil:
    0 VAC

    What is the likely problem?
    """)

    answer = st.radio(
        "Diagnosis:",
        [
            "Failed motor",
            "Open control circuit",
            "Bad bearings",
            "Wrong overload setting"
        ]
    )


    if st.button("Finish Scenario"):

        if answer == "Open control circuit":
            st.success("Excellent troubleshooting!")
            st.session_state.score += 10
        else:
            st.error("Review control circuit troubleshooting.")
            st.session_state.score -= 10


        st.session_state.question = 4


if st.session_state.question == 4:

    st.header("Scenario Complete")

    st.write(
        f"Final Score: {st.session_state.score}/100"
    )

    if st.session_state.score >= 100:
        st.success("Electrical Apprentice Level Up!")
    else:
        st.info("Keep practicing. Every electrician builds troubleshooting skills through repetition.")
