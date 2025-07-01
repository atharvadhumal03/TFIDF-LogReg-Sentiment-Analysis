import pickle
import streamlit as st
from function import full_text_preprocessing

with open("model.pkl", "rb") as file:
    pipeline = pickle.load(file)

# GUI code
st.markdown(
    """
    
    <div style='text-align: center; color: gray; font-size: 13px;'>
        © Atharva Dhumal | A movie review sentiment classifier using TF-IDF and Logistic Regression.
    </div>
    <hr style="margin-top: 20px;"/>
    """,
    unsafe_allow_html=True
)
st.markdown(
"""
    <style>
    .stApp {
        background-color: #262e36;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h2 style='text-align: center;'>🎬 IMDB Movie Review Sentiment Classifier</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: left; font-size:18px;'>This is a movie review classifier. "
    "Enter a review of a movie you recently watched to see whether it's classified as positive😁 or negative😔.</p>",
    unsafe_allow_html=True
)

user_review = st.text_area("Enter your movie review below ⬇️ :", height=80)

if 'show_confirm' not in st.session_state:
    st.session_state.show_confirm = False

if 'show_result' not in st.session_state:
    st.session_state.show_result = False

# Submit button
if st.button("Submit Review"):
    if user_review.strip() != "":
        st.session_state.show_confirm = True
        st.session_state.show_result = False
    else:
        st.warning("Please enter a review before submitting.")

# Display review and confirm button
if st.session_state.show_confirm:
    st.markdown("**Please confirm the review you have entered ⬇️ :**")
    st.write(user_review)
    if st.button("Confirm and Predict"):
        st.session_state.show_result = True

if st.session_state.show_result:
    # Replace this with actual model prediction
    X_new = full_text_preprocessing(user_review)
    
    if X_new and X_new[0].strip() != "":
        sentiment = pipeline.predict(X_new)[0]

        if sentiment == 'positive':
            st.success(f"Predicted Sentiment: Positive!", icon="⭐️")
        else:
            st.info(f"Predicted Sentiment: Negative!", icon="💔")
    else:
        st.warning(f"⚠️ Please enter a valid review with meaningful content.")