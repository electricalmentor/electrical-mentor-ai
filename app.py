import streamlit as st

st.title("⚡ Electrical Mentor AI Simulator")

st.write("Scenario #001: 480V Motor Will Not Start")

st.subheader("Equipment")
st.write("""
- 480V three-phase motor
- Across-the-line starter
- 120V control circuit
- Conveyor application
""")

st.subheader("Problem")

st.write("""
Operator reports:
"The conveyor motor will not start."
""")

answer = st.radio(
    "What should you check first?",
    [
        "Replace the motor",
        "Check incoming voltage",
        "Check control voltage",
        "Megger the motor"
    ]
)

if st.button("Submit"):

    if answer == "Check control voltage":
        st.success("Correct! Troubleshooting starts with verifying the control circuit.")
        
        st.write("""
        Measurements:
        
        Control transformer secondary: 120 VAC
        
        Start button: Good
        
        Contactor coil: 0 VAC
        """)
        
    else:
        st.error("Not the best first step. Think like a troubleshooter.")
