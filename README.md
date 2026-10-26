
# AI Healthcare Information Assistant

## 1. Project Overview

The AI Healthcare Information Assistant is a web-based educational prototype developed using Python and Streamlit. It provides predefined general health information based on user questions and selected health topics.

The application uses keyword matching to identify common health questions and display relevant information. It is a rule-based prototype and does not use a trained AI model.

## 2. Objectives

- Provide general health information through a simple interface.
- Answer selected common health questions.
- Display health and safety information.
- Promote general health awareness.
- Demonstrate Python programming and web application development.

## 3. Technologies Used

- Python
- Streamlit
- Pytest
- Visual Studio Code

## 4. Features

- Home page
- Health FAQs
- Safety Information page
- General health question input
- Predefined responses using keyword matching
- Fallback response for unsupported questions
- Empty-question validation
- Automated tests for selected health questions

## 5. Project Structure

```text
AI-Healthcare-Assistant/
├── app.py
├── health_answers.py
├── requirements.txt
├── README.md
├── screenshots/
├── tests/
│   └── test_app.py
└── .gitignore
```

## 6. Installation and Setup

### Step 1: Create a virtual environment

```bash
python -m venv .venv
```

### Step 2: Activate the environment on Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually http://localhost:8501.

## 7. Testing

The project includes automated tests written using Pytest.

Run the tests with:

```bash
python -m pytest tests/ -v
```

The tests check:
- Water-related questions
- Sleep-related questions
- Unsupported-question fallback

Three tests passed during development.

## 8. Screenshots

Screenshots of the working application are stored in the `screenshots/` folder. Include screenshots of the features actually implemented.

## 9. Limitations

- Uses predefined responses and keyword matching.
- Does not use a trained AI model.
- Cannot diagnose diseases or prescribe treatments.
- May not recognize questions with unexpected wording.
- Does not replace professional medical advice.

## 10. Future Enhancements

- Integrate a suitable AI language model with health-related safety controls.
- Expand the health FAQ database.
- Improve question matching.
- Add multilingual support.
- Improve accessibility and user experience.
- Add more automated tests.

## 11. Disclaimer

This application is an educational prototype that provides general health information only. It is not a medical diagnostic system and does not replace a qualified healthcare professional. Seek urgent medical attention for emergency symptoms.
