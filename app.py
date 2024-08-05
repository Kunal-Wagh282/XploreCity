import streamlit as st
from streamlit_chat import message

def main():
    conversation_flow = {
        "": {
            "text": "Hello, Nice to see you. Is there something I can help you with?",
            "options": ["Yes", "No"]
        },
        "Yes": {
            "text": "Get Started with the given quick links or feel free to ask your query via text or voice.",
            "options": ["Sign-in", "Registration", "Onboarding", "Search", "AR", "Avatars", "Profile"]
        },
        "No": {
            "text": "If you have any questions, please don't hesitate to ask.",
            "options": ["Back to main menu", "Contact customer support"]
        },
        "Sign-in": {
            "text": "Please enter your credentials to sign in.",
            "options": ["Back to main menu"]
        },
        "Registration": {
            "text": "Please fill in the registration form.",
            "options": ["Back to main menu"]
        },
        "Onboarding": {
            "text": "Welcome! Let's get you started with some onboarding information.",
            "options": ["Back to main menu"]
        },
        "Search": {
            "text": "What would you like to search for?",
            "options": ["Choose your Attraction"]
        },
        "Choose your Attraction": {
            "text": "Here are some categories to choose from:",
            "options": ["Religious sites", "Historical monuments", "Museum", "Nature walk", "Arcade"]
        },
        "Religious sites": {
            "text": "Here are some religious sites:",
            "options": ["Back to main menu"]
        },
        "Historical monuments": {
            "text": "Here are some historical monuments:",
            "options": ["Back to main menu"]
        },
        "Museum": {
            "text": "Here are some museums:",
            "options": ["Back to main menu"]
        },
        "Nature walk": {
            "text": "Here are some nature walks:",
            "options": ["Back to main menu"]
        },
        "Arcade": {
            "text": "Here are some arcades:",
            "options": ["Back to main menu"]
        },
        "AR": {
            "text": "Explore Augmented Reality features.",
            "options": ["Back to main menu"]
        },
        "Avatars": {
            "text": "Customize your avatar or take a selfie with characters.",
            "options": ["Characters", "Click a Selfie"]
        },
        "Characters": {
            "text": "Choose from these characters:",
            "options": ["Back to main menu"]
        },
        "Click a Selfie": {
            "text": "Get ready to take a selfie!",
            "options": ["Back to main menu"]
        },
        "Profile": {
            "text": "Manage your profile settings.",
            "options": ["Onboarding information", "Places you visited", "Rate experience", "Help centre"]
        },
        "Onboarding information": {
            "text": "Here is your onboarding information.",
            "options": ["Back to main menu"]
        },
        "Places you visited": {
            "text": "Here are the places you have visited.",
            "options": ["Back to main menu"]
        },
        "Rate experience": {
            "text": "Rate your experience.",
            "options": ["Back to main menu"]
        },
        "Help centre": {
            "text": "How can we assist you?",
            "options": ["FAQs & Chatbot", "Account & settings", "Rewards", "Offers"]
        },
        "FAQs & Chatbot": {
            "text": "Here are some frequently asked questions and our chatbot.",
            "options": ["Back to main menu"]
        },
        "Account & settings": {
            "text": "Manage your account settings.",
            "options": ["Back to main menu"]
        },
        "Rewards": {
            "text": "Check out your rewards.",
            "options": ["Back to main menu"]
        },
        "Offers": {
            "text": "Here are some special offers.",
            "options": ["Back to main menu"]
        },
        "Contact customer support": {
            "text": "Please contact our customer support at support@example.com or call us at 123-456-7890.",
            "options": ["Back to main menu"]
        }
    }

    st.set_page_config(page_title="🤖 Chat Bot", layout="wide")
    st.title("🤖 Xplore-City Chatbot")

    # Initialize session state
    if "step" not in st.session_state:
        st.session_state.step = ""
        st.session_state.history = []

    # Display the current step's message
    current_step = st.session_state.step

    # Add the current step to the history only if it's a new step
    if st.session_state.history == [] or st.session_state.history[-1] != current_step:
        st.session_state.history.append(current_step)

    # Display conversation history
    for idx, step in enumerate(st.session_state.history):
        if idx == 0:
            message(f"Welcome to Xplore-City! ��", key=f"bot_{idx-1}")
            message(f"{conversation_flow[step]['text']}", key=f"bot_{idx}")
            if step == "":
                continue
            message(f"{step}", is_user=True, key=f"user_{idx}")
        else:
            message(f"{step}", is_user=True, key=f"user_{idx}")
            message(f"{conversation_flow[step]['text']}", key=f"bot_{idx}")
    # Display the current step's message

    # Display options as buttons in multiple columns
    options = conversation_flow[current_step]["options"]
    cols = st.columns(3)  # Adjust the number of columns as needed
    for i, option in enumerate(options):
        if cols[i % 3].button(option):  # Adjust the modulo value based on number of columns
            if option == "Back to main menu":
                st.session_state.step = ""
                st.session_state.history = []
            else:
                st.session_state.step = option

    # Add a reset button to clear the session state
    if st.button("Reset Conversation"):
        st.session_state.step = ""
        st.session_state.history = []

    # Add custom CSS to style the chatbot
    st.markdown("""
    <style>
        .stButton button {
            width: 100%;
            margin: 2px 0;
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;
            border-radius: 12px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
