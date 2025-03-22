import base64
import streamlit as st
import pandas as pd
import time
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Function to add background image dynamically
def add_bg_from_local(image_file, is_login=False):
    """Adds a background image and applies CSS styles."""
    if os.path.exists(image_file):
        with open(image_file, "rb") as file:
            encoded_string = base64.b64encode(file.read()).decode("utf-8")

        style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-attachment: fixed;
        }}
        h1, h2, h3, h4, h5, h6, p, .stMarkdown {{
            color: white;
        }}
        /* Custom button styling */
        .stButton > button {{
            background-color: #f8f9f9 !important:
            color: black !important; /* black text */
            border-radius: 5px !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            border: none !important;
        }}
        .stButton > button:hover {{
            background-color: #424949 !important; 
        }}
        /* Make the sidebar background transparent */
        section[data-testid="stSidebar"] {{
            background: rgba(10, 173, 146, 0.47); /* Fully transparent */
        }}
        </style>
        """
        st.markdown(style, unsafe_allow_html=True)
    else:
        st.error("Error: Background image file not found!")

# Function to set sidebar text color to white
def set_sidebar_text_color():
    st.markdown("""
        <style>
        .sidebar .sidebar-content {
            color: white;
        }
        .stSlider, .stRadio, .stTextInput, .stSelectbox, .stCheckbox, .stMarkdown {
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# File to store registered users
USERS_FILE = "users.csv"

# Load or create users file
def load_users():
    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)
    else:
        return pd.DataFrame(columns=["Username", "Password"])

def save_users(users_df):
    users_df.to_csv(USERS_FILE, index=False)

# Registration Page
def register():
    """Registration UI for new users."""
    st.markdown("<h1 style='text-align: center; font-size: 50px; color: #FFD700;'>Register</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 30px; color: white;'>Create a new account</h2>", unsafe_allow_html=True)

    with st.form("registration_form"):
        username = st.text_input("Username", key="reg_username")
        password = st.text_input("Password", type="password", key="reg_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm_password")

        if st.form_submit_button("Register"):
            if password != confirm_password:
                st.error("Passwords do not match!")
            else:
                users_df = load_users()
                if username in users_df["Username"].values:
                    st.error("Username already exists!")
                else:
                    new_user = pd.DataFrame({"Username": [username], "Password": [password]})
                    users_df = pd.concat([users_df, new_user], ignore_index=True)
                    save_users(users_df)
                    st.success("Registration successful! Please log in.")

# Login Page
def login():
    """Login UI for authentication."""
    add_bg_from_local("C:/Users/LENOVO/Desktop/login img.jpeg", is_login=True)  # rearrange the path of img file

    # Unique Title
    st.markdown("<h1 style='text-align: center; font-size: 50px; color: #FFD700;'>FitGenius AI</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 30px; color: white;'>Your Smart Fitness Tracker Companion</h2>", unsafe_allow_html=True)

    # Use a unique key for the username input widget
    username = st.text_input("**Username**", key="login_username")
    password = st.text_input("**Password**", type="password", key="login_password")

    if st.button("Login"):
        users_df = load_users()
        user = users_df[(users_df["Username"] == username) & (users_df["Password"] == password)]
        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.current_user = username  # Use a different key for session state
            st.success("Login Successful! Redirecting...")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Invalid credentials, please try again.")

    if st.button("Register New User"):
        st.session_state.register = True
        st.rerun()

# Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    if "register" in st.session_state and st.session_state.register:
        register()
    else:
        login()
else:
    # Main App After Login
    add_bg_from_local("C:/Users/LENOVO/Desktop/after login img.jpg")# rearrange the path of img file

    # Set sidebar text color to white
    set_sidebar_text_color()

    # Unique Title for Main App
    st.markdown("<h1 style='font-size: 50px; color: #FFD700;'>FitGenius AI</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 30px; color: white;'>Your Smart Fitness Tracker Companion</h2>", unsafe_allow_html=True)

    # Display the logged-in user
    st.sidebar.write(f"Logged in as: **{st.session_state.current_user}**")

    st.sidebar.header("**User Input Parameters**")

    def user_input_features():
        """Creates input widgets for the user with added explanations."""
        
        # Adding explanations to each slider
        age = st.sidebar.slider("Age (Years)", 10, 100, 30, help="Select your age between 10 and 100 years.")
        bmi = st.sidebar.slider("BMI (Body Mass Index)", 15, 40, 20, help="Select your Body Mass Index (BMI) value.")
        duration = st.sidebar.slider("Exercise Duration (Minutes)", 0, 60, 15, help="Enter how long you plan to exercise (in minutes).")
        heart_rate = st.sidebar.slider("Heart Rate (bpm)", 60, 200, 80, help="Select your average heart rate during exercise (beats per minute).")
        body_temp = st.sidebar.slider("Body Temperature (°C)", 36, 42, 38, help="Select your body temperature during exercise in Celsius.")
        
        gender = st.sidebar.radio("Gender", ("Male", "Female"), help="Select your gender for the prediction.")
        
        # Convert gender to binary
        gender_value = 1 if gender == "Male" else 0

        data = {
            "Age": age,
            "BMI": bmi,
            "Duration": duration,
            "Heart_Rate": heart_rate,
            "Body_Temp": body_temp,
            "Gender_male": gender_value
        }

        return pd.DataFrame(data, index=[0])

    df = user_input_features()

    st.write("""Welcome to the Calorie Burn Prediction WebApp!🙏
    By entering your parameters such as age, gender, BMI, and more, this tool will predict the number of kilocalories you are likely to burn. Simply input your details and receive an estimated value of your daily calorie expenditure.""")

    # Display input data
    st.write("---")
    st.markdown("## **Your Input Parameters**")
    st.write(f"**Age:** {df['Age'][0]}")
    st.write(f"**BMI:** {df['BMI'][0]}")
    st.write(f"**Duration:** {df['Duration'][0]} minutes")
    st.write(f"**Heart Rate:** {df['Heart_Rate'][0]} bpm")
    st.write(f"**Body Temperature:** {df['Body_Temp'][0]} °C")
    st.write(f"**Gender:** {'Male' if df['Gender_male'][0] == 1 else 'Female'}")

    # Load datasets
    calories_df = pd.read_csv("calories.csv")
    exercise_df = pd.read_csv("exercise.csv")

    # Merge data
    data = exercise_df.merge(calories_df, on="User_ID", how="inner").drop(columns="User_ID")

    # Add BMI column
    data["BMI"] = data["Weight"] / ((data["Height"] / 100) ** 2)
    data["BMI"] = round(data["BMI"], 2)

    # Select relevant features
    data = data[["Gender", "Age", "BMI", "Duration", "Heart_Rate", "Body_Temp", "Calories"]]

    # One-hot encoding for categorical features
    data = pd.get_dummies(data, drop_first=True)

    # Train-test split
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=1)

    # Split features (X) and target variable (y)
    X_train = train_data.drop("Calories", axis=1)
    y_train = train_data["Calories"]
    X_test = test_data.drop("Calories", axis=1)
    y_test = test_data["Calories"]

    # Train Random Forest Model
    model = RandomForestRegressor(n_estimators=1000, max_features=3, max_depth=6, random_state=42)
    model.fit(X_train, y_train)

    # Ensure the user input DataFrame matches the training columns
    df = df.reindex(columns=X_train.columns, fill_value=0)

    # Predict Calories
    prediction = model.predict(df)

    # Display Prediction
    st.write("---")
    st.markdown("## **Predicted Calories Burned**")
    
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
        time.sleep(0.01)

    st.write(f"🔥 You will burn **{round(prediction[0], 2)} kilocalories** during this exercise session!")

    # Display Similar Results
    st.write("---")
    st.markdown("## **Similar Results in Dataset**")
    
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
        time.sleep(0.01)

    # Find and display similar calorie data
    similar_data = data[(data["Calories"] >= prediction[0] - 10) & (data["Calories"] <= prediction[0] + 10)]
    st.write(similar_data.sample(5) if not similar_data.empty else "No similar records found.")

    # General Comparisons
    st.write("---")
    st.markdown("## **Your Performance Compared to Others**")

    # Comparison for age
    age_comparison = (data['Age'] < df['Age'].values[0]).mean() * 100
    st.write(f"🌱 You are **{round(age_comparison, 2)}%** older than the average user.")

    # Comparison for exercise duration
    duration_comparison = (data['Duration'] < df['Duration'].values[0]).mean() * 100
    st.write(f"⏱️ You exercise **{round(duration_comparison, 2)}%** longer than most users.")

    # Comparison for heart rate
    heart_rate_comparison = (data['Heart_Rate'] < df['Heart_Rate'].values[0]).mean() * 100
    st.write(f"💓 Your heart rate is higher than **{round(heart_rate_comparison, 2)}%** of other users during exercise.")

    # Comparison for body temperature
    body_temp_comparison = (data['Body_Temp'] < df['Body_Temp'].values[0]).mean() * 100
    st.write(f"🌡️ Your body temperature is higher than **{round(body_temp_comparison, 2)}%** of others after the workout.")

    # AI-Powered Personalized Recommendations
    st.write("---")
    st.markdown("## **AI-Powered Recommendations**")

    if prediction[0] < 200:
        st.write("💡 **Recommendation:** You burned fewer calories than average. Try increasing your exercise duration or intensity!")
    elif prediction[0] >= 200 and prediction[0] < 400:
        st.write("💡 **Recommendation:** Great job! You're on the right track. Consider adding strength training to your routine.")
    else:
        st.write("💡 **Recommendation:** Amazing work! You're burning a lot of calories. Keep up the good work!")

    # Simple AI Chatbot
    st.write("---")
    st.markdown("## **Fitness Chatbot**")

    chatbot_input = st.text_input("Ask me anything about fitness:")
    if chatbot_input:
        if "calories" in chatbot_input.lower():
            st.write("🤖 **Chatbot:** Calories are a measure of energy. To burn more calories, try high-intensity workouts like running or cycling.")
        elif "diet" in chatbot_input.lower():
            st.write("🤖 **Chatbot:** A balanced diet with proteins, carbs, and healthy fats is key to fitness. Avoid processed foods!")
        elif "workout" in chatbot_input.lower():
            st.write("🤖 **Chatbot:** A good workout plan includes cardio, strength training, and flexibility exercises.")
        else:
            st.write("🤖 **Chatbot:** I'm here to help with fitness-related questions. Ask me about calories, diet, or workouts!")