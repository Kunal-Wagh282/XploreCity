import streamlit as st

def main():
    conversation_flow = {
        "": {
            "text": "Hello! I am Apsara, your virtual assistant. How can I help you today?",
            "options": ["Refunds", "Locations", "Attractions", "App Features", "AR Experience", "Booking", "Support", "General Queries"]
        },
        "Refunds": {
            "text": "I can help you with refunds. What would you like to know?",
            "options": ["How to get a refund", "When will I get my refund?", "Any validity for refund?", "Where to contact for refund?", "Back to main menu"]
        },
        "How to get a refund": {
            "text": "Go to the About section - Refunds and settlements - Select trip, see eligibility, and apply.",
            "options": ["Back to main menu"]
        },
        "When will I get my refund?": {
            "text": "If your booking is more than 2 hours from now, you are eligible for a refund in 2 weeks.",
            "options": ["Back to main menu"]
        },
        "Any validity for refund?": {
            "text": "You can request a refund within 2 hours from the booking date.",
            "options": ["Back to main menu"]
        },
        "Where to contact for refund?": {
            "text": "Go to the About section - Refunds and settlements - Select trip, see eligibility, and apply.",
            "options": ["Back to main menu"]
        },
        "Locations": {
            "text": "I can assist you with locations. What would you like to know?",
            "options": ["Nearest locations for brunch", "Is this place safe to travel at night?", "Can the app notify me about the nearest location to hang out?", "Back to main menu"]
        },
        "Nearest locations for brunch": {
            "text": "I sadly can't help you with that.",
            "options": ["Back to main menu"]
        },
        "Is this place safe to travel at night?": {
            "text": "I'm sorry, I don't know. You can WhatsApp message us to find out!",
            "options": ["Back to main menu"]
        },
        "Can the app notify me about the nearest location to hang out?": {
            "text": "Yes! I can show you the best hangout spots. For restaurants, please see my sister Google!",
            "options": ["Back to main menu"]
        },
        "Attractions": {
            "text": "Here are some queries related to attractions:",
            "options": ["How do I view details about an attraction?", "What are some lesser-known but amazing spots to visit for a solo traveler?", "Can I get directions to an attraction?", "My attraction is not listed", "Back to main menu"]
        },
        "How do I view details about an attraction?": {
            "text": "Tap on the attraction to see its picture, description, and map.",
            "options": ["Back to main menu"]
        },
        "What are some lesser-known but amazing spots to visit for a solo traveler?": {
            "text": "You can select a category, and I will suggest some options.",
            "options": ["Back to main menu"]
        },
        "Can I get directions to an attraction?": {
            "text": "Yes, view the details of the attraction and use the integrated map for directions.",
            "options": ["Back to main menu"]
        },
        "My attraction is not listed": {
            "text": "You can go to the hamburger menu - Request Attraction and type the place you want to add!",
            "options": ["Back to main menu"]
        },
        "App Features": {
            "text": "I can provide information on our app features. What would you like to know?",
            "options": ["Can it store data like contacts or history of locations we travel?", "Is Xplore Muni available in multiple languages?", "How can I update the app to the latest version?", "Back to main menu"]
        },
        "Can it store data like contacts or history of locations we travel?": {
            "text": "We only store your Gmail.",
            "options": ["Back to main menu"]
        },
        "Is Xplore Muni available in multiple languages?": {
            "text": "We are currently working on this feature.",
            "options": ["Back to main menu"]
        },
        "How can I update the app to the latest version?": {
            "text": "You can update the app using the Play Store.",
            "options": ["Back to main menu"]
        },
        "AR Experience": {
            "text": "The AR experience is an exciting feature! What would you like to know?",
            "options": ["How to see AR experience", "Do I need special equipment to use the AR Experience?", "How do I take a photo with an AR Avatar?", "What is AR?", "Back to main menu"]
        },
        "How to see AR experience": {
            "text": "Click on your attraction spot and view the AR experience.",
            "options": ["Back to main menu"]
        },
        "Do I need special equipment to use the AR Experience?": {
            "text": "Absolutely not! You can experience the AR using your mobile phone.",
            "options": ["Back to main menu"]
        },
        "How do I take a photo with an AR Avatar?": {
            "text": "This feature is coming soon.",
            "options": ["Back to main menu"]
        },
        "What is AR?": {
            "text": "AR is augmented reality. It adds images and models to your environment.",
            "options": ["Back to main menu"]
        },
        "Booking": {
            "text": "Need help with booking? What would you like to know?",
            "options": ["How do I book a ticket for an attraction?", "Can I sign in with my Google or Facebook account?", "Can I change my booking date?", "Can I postpone booking?", "Back to main menu"]
        },
        "How do I book a ticket for an attraction?": {
            "text": "Tap 'Book Now' on the attraction's details page and follow the booking process.",
            "options": ["Back to main menu"]
        },
        "Can I sign in with my Google or Facebook account?": {
            "text": "Yes, you can easily log in using any of these options.",
            "options": ["Back to main menu"]
        },
        "Can I change my booking date?": {
            "text": "Yes, sure! Just follow the steps below.",
            "options": ["Back to main menu"]
        },
        "Can I postpone booking?": {
            "text": "If you are 2 hours away from the booking time, you can!",
            "options": ["Back to main menu"]
        },
        "Support": {
            "text": "I can help you with customer support. What do you need?",
            "options": ["How do I contact customer support?", "Payment not successful", "How to get connected to customer service", "Back to main menu"]
        },
        "How do I contact customer support?": {
            "text": "Here is our email and WhatsApp number.",
            "options": ["Back to main menu"]
        },
        "Payment not successful": {
            "text": "Kindly enter your ticket number, and we will contact you soon.",
            "options": ["Back to main menu"]
        },
        "How to get connected to customer service": {
            "text": "Here is our email and WhatsApp number.",
            "options": ["Back to main menu"]
        },
        "General Queries": {
            "text": "Do you have a general question? Let me help you.",
            "options": ["Who are you?", "Are you real?", "How much money should I carry for recreational activities?", "Can I use the app without creating an account?", "Can I save favorite places for later?", "Back to main menu"]
        },
        "Who are you?": {
            "text": "I am Apsara! Your customer support chatbot.",
            "options": ["Back to main menu"]
        },
        "Are you real?": {
            "text": "No, I am Apsara, a virtual assistant here to help you with customer support.",
            "options": ["Back to main menu"]
        },
        "How much money should I carry for recreational activities?": {
            "text": "What attractions do you wish to visit? The total comes to be X.",
            "options": ["Back to main menu"]
        },
        "Can I use the app without creating an account?": {
            "text": "No, you need to create an account to use all features.",
            "options": ["Back to main menu"]
        },
        "Can I save favorite places for later?": {
            "text": "Currently, we are working on this feature.",
            "options": ["Back to main menu"]
        }
    }

    st.set_page_config(page_title="🤖 Chat Bot", layout="wide")
    st.title("Xplore-City Chatbot")
    st.subheader("Double-Tap options to proceed!")

    if "step" not in st.session_state:
        st.session_state.step = ""
        st.session_state.history = []

    current_step = st.session_state.step

    if st.session_state.history == [] or st.session_state.history[-1] != current_step:
        st.session_state.history.append(current_step)

    for idx, step in enumerate(st.session_state.history):
        if idx == 0:
            st.chat_message("bot", avatar="apsara.png").write("Welcome to Xplore-City! 👋")
            st.chat_message("bot", avatar="apsara.png").write(conversation_flow[step]['text'])
            if step == "":
                continue
            st.chat_message("user").write(step)
        else:
            st.chat_message("user", avatar="user.png").write(step)
            st.chat_message("bot", avatar="apsara.png").write(conversation_flow[step]['text'])

    options = conversation_flow[current_step]["options"]
    cols = st.columns(3)
    for i, option in enumerate(options):
        if cols[i % 3].button(option):
            if option == "Back to main menu":
                st.session_state.step = ""
                st.session_state.history = []
            else:
                st.session_state.step = option

    if st.button("Reset Conversation"):
        st.session_state.step = ""
        st.session_state.history = []

    st.markdown("""
    <style>
        body {
            background-color: #121212; /* Dark background */
            color: #e0e0e0; /* Light text color */
        }
        .stButton button {
            width: 100%;
            margin: 2px 0;
            background: linear-gradient(45deg, #1e90ff, #00bfff); /* Blue gradient */
            border: none;
            color: #e0e0e0; /* Light text color */
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;
            border-radius: 12px;
        }
        .stButton button:hover {
            background: linear-gradient(45deg, #00bfff, #1e90ff); /* Swap gradient direction for hover */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Add shadow for better hover effect */
        }
        .stChatMessage[data-author="bot"] {
            background-color: #1f1f1f; /* Dark background for bot messages */
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            color: #e0e0e0; /* Light text color */
            text-align: left; /* Align bot messages to the left */
            margin-right: auto; /* Push bot messages to the left */
            width: fit-content; /* Adjust width to fit content */
        }
        .stChatMessage[data-author="user"] {
            background-color: #333333; /* Darker background for user messages */
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            color: #e0e0e0; /* Light text color */
            text-align: right; /* Align user messages to the right */
            margin-left: auto; /* Push user messages to the right */
            width: fit-content; /* Adjust width to fit content */
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

