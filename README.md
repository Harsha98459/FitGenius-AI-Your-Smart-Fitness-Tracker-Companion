# FitGenius AI: Your Smart Fitness Tracker Companion
![FitGenius AI Logo](https://t4.ftcdn.net/jpg/02/18/46/59/360_F_218465980_2JJETZ9wO9rp2obMr8ANLnX00OTfbpjU.jpg)

FitGenius AI is an innovative, AI-powered fitness tracking platform designed to revolutionize the way individuals approach their health and wellness goals. Combining cutting-edge artificial intelligence with user-friendly features, FitGenius AI serves as a personalized fitness companion that adapts to your unique needs, preferences, and progress.
# Download the (app.py)file to get started!
The provided file (`app.py`) is a **Streamlit-based web application** for a fitness tracking and calorie burn prediction tool called **FitGenius AI**. It includes features like user registration, login, input parameter collection (e.g., age, BMI, exercise duration), and a machine learning model (Random Forest Regressor) to predict calories burned. It also provides personalized recommendations and a simple AI chatbot for fitness-related queries.

---

### **How to Run the Application**

1. **Prerequisites**:
   - Install Python (3.7 or higher).
   - Install required libraries:
     ```bash
     pip install streamlit pandas numpy scikit-learn
     ```
   - Ensure you have the following files in the same directory as `app.py`:
     - `calories.csv` (dataset for calories burned).
     - `exercise.csv` (dataset for exercise data).
     - Background images (e.g., `login img.jpeg`, `after login img.jpg`).

2. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `app.py`.
   - Run the following command:
     ```bash
     streamlit run app.py
     ```
   - The app will start, and a local URL (e.g., `http://localhost:8501`) will open in your browser.

3. **Using the App**:
   - **Register**: Create a new account by providing a username and password.
   - **Login**: Use your credentials to log in.
   - **Input Parameters**: Enter your fitness details (age, BMI, exercise duration, etc.) in the sidebar.
   - **Predict Calories**: View the predicted calories burned and personalized recommendations.


### **Markdown Description for GitHub**

Here’s how you can describe the project in a `README.md` file for GitHub:

```markdown
# FitGenius AI: Your Smart Fitness Tracker Companion

![FitGenius AI Logo](https://example.com/path-to-your-logo.png)

FitGenius AI is a **Streamlit-based web application** that helps users track their fitness progress and predict calories burned during exercise. It features user authentication, a machine learning model (Random Forest Regressor), and personalized fitness recommendations.

## Features
- **User Registration & Login**: Secure authentication system.
- **Calorie Burn Prediction**: Predicts calories burned based on user inputs (age, BMI, exercise duration, etc.).
- **Personalized Recommendations**: AI-powered suggestions to improve fitness.
- **AI Chatbot**: Answers fitness-related questions.
- **Interactive UI**: Dynamic background images and user-friendly interface.

## How to Run
1. Install dependencies:
   ```bash
   pip install streamlit pandas numpy scikit-learn
   ```
2. Download the required datasets (`calories.csv` and `exercise.csv`) and place them in the same directory as `app.py`.
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser and navigate to `http://localhost:8501`.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building the web app.
- **Pandas & NumPy**: For data manipulation.
- **Scikit-Learn**: For machine learning (Random Forest Regressor).

## Dataset
- `calories.csv`: Contains calorie burn data.
- `exercise.csv`: Contains exercise-related data.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
```

### **Notes**:
- Replace `https://example.com/path-to-your-logo.png` and other placeholder URLs with actual paths to your images or screenshots.
- Ensure the datasets (`calories.csv` and `exercise.csv`) are included in your repository or provide instructions on how to obtain them.
