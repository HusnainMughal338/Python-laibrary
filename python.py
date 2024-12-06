import streamlit as st

# Function to display details
def details(question):
    # Dictionary of questions with their details
    questions = {
        "What is Python": { 
            "Definition": "Python is a high-level, general-purpose programming language that emphasizes readability and simplicity, making it one of the most popular programming languages in the world. It supports multiple programming paradigms, such as object-oriented, procedural, and functional programming, and is widely used in a variety of fields.",
            "Image": "https://www.ntuclearninghub.com/documents/39367/7251794/python-programming+fundamentals.jpg/0f980a00-ced6-85e7-3d57-fa1651dd572b?t=1720163859849",
            "Video": None  # No video for this entry
        },
        "Python Video": {
            "Definition": None,  # No definition for this entry
            "Image": None,  # No image for this entry
            "Video": "https://youtu.be/t2_Q2BRzeEE?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0"
        },
        "Who created the Information Cell app": {
            "Definition": "This app was made by Husnain Mughal using Python. This application was created using machine learning libraries. It is designed to provide all Python-related information and is available for all users. The app was created on 5 December 2024.",
            "Image": None,  # Replace with a valid URL or local image path
            "Video": None
        },
        "Who is Husnain": {
            "Definition": "Husnain Mughal is the creator of the Information Cell app. He developed this app using Python and machine learning tools to provide Python-related knowledge.",
            "Image": None,  # Replace with a valid URL or local image path
            "Video": None
        },
        "Explain Python": {
            "Definition": (
                "Key Features of Python:\n"
                "- **Easy to Learn and Use**: Python has a clean and simple syntax.\n"
                "- **Interpreted Language**: Python code is executed line by line.\n"
                "- **Dynamic Typing**: No need to declare variable types explicitly.\n"
                "- **Cross-Platform**: Runs on Windows, macOS, and Linux.\n"
                "- **Extensive Standard Library**: Rich set of modules for tasks like web development, data manipulation, and file handling.\n"
                "- **Wide Range of Applications**: Web development, data analysis, machine learning, game development, and more.\n"
                "- **Strong Community Support**: Extensive documentation and resources."
            ),
            "Image": None,
            "Video": None
        }
    }

    # Return the question details or a message if not found
    return questions.get(question, None)

# Streamlit app layout
st.title(":rainbow[Information Cell]")

# Input field for the user's question
question = st.text_input("Enter your Question:")

# Display details when the button is clicked
if st.button("Get Details"):
    question_info = details(question)
    if question_info is None:
        st.error("Question not found. Please try another.")
    else:
        st.write("### :red[Details]")
        
        # Display the definition if available
        if question_info.get("Definition"):
            st.write(f"**:blue[Definition]:** {question_info['Definition']}")
        
        # Display the image if available
        if question_info.get("Image"):
            try:
                if question_info["Image"].startswith("http"):
                    st.image(question_info["Image"], caption="Image", use_column_width=True)
                else:
                    st.image(question_info["Image"], caption="Image", use_column_width=True)
            except Exception as e:
                st.error(f"Error loading image: {e}")
        
        # Display the video if available
        if question_info.get("Video"):
            st.video(question_info["Video"])
