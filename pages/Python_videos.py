import streamlit as st

# Function to get video details
def knowledge(question):
    # Dictionary of questions with video links
    videos = {
        "python full course": {
            "videos": [
                "https://youtu.be/t2_Q2BRzeEE?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
                "https://youtu.be/lIId8IDP6TU?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
                "https://youtu.be/qVyvmzFxF_o?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
                "https://youtu.be/078tYSD7K8E?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
                "https://youtu.be/S73thl0AyFU?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
                "https://youtu.be/OvTH-7ESoRA?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
                "https://youtu.be/jU0cndZziO0?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
                "https://youtu.be/HeW-D6KpDwY?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
                "https://youtu.be/bAwmZVJeO5s?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0",
            ]
        },
        "naveed sarwar videos": {
            "videos": [
                "https://youtu.be/Vw4MGTLbisg?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
                "https://youtu.be/uYwHF7jxWuY?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
                "https://youtu.be/4Gb6pVn3Cig?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
                "https://youtu.be/xwdesyF8Gwk?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
                "https://youtu.be/9gat53-f4cs?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
                "https://youtu.be/nKx3-0LFVJw?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
                "https://youtu.be/JuNJVG3QzbQ?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
                "https://youtu.be/4mE7mdq9Hy0?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
                "https://youtu.be/j2-9n_RUmcQ?list=PLOfLYVXrwqXohRWg_Wbtv9JHFaDc12DmI",
            ]
        }
    }

    # Return the video details or None if not found
    return videos.get(question.lower(), None)

# Streamlit app layout
st.title(":rainbow[Information Cell]")

# Input field for the user's question
question = st.text_input("Enter your Question:")

# Display details when the button is clicked
if st.button("Get Details"):
    question_info = knowledge(question)
    if question_info is None:
        st.error("Question not found. Please try another.")
    else:
        st.write("### Videos")
        for video_url in question_info["videos"]:
            st.video(video_url)  # Display each video

# Additional preloaded videos
st.write("### :red[Additional Videos]")
additional_videos = [
    "https://youtu.be/iHBmMw-8SXo?list=RDiHBmMw-8SXo",
    "https://youtu.be/pWuXWIRzV-g?list=RDiHBmMw-8SXo"
]

for video in additional_videos:
    st.video(video)  # Display each additional video
