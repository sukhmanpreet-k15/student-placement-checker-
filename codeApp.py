

import streamlit as st
import pandas as pd
import pickle
import subprocess
import sys
import tempfile
import os
import ast
import io
import tokenize

from questions import MCQ_QUESTIONS
from coding_q import CODING_PROBLEMS

st.set_page_config(page_title="Student Assessment Platform")



# CODE RUNNER (for Part 2)

def run_student_code(code, test_input, timeout_seconds=5):
    
    temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False)
    temp_file.write(code)
    temp_file.close()
    temp_path = temp_file.name

    try:
        result = subprocess.run(
            [sys.executable, temp_path],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )

        if result.returncode != 0:
            return None, result.stderr.strip()

        return result.stdout.strip(), None

    except subprocess.TimeoutExpired:
        return None, "Time Limit Exceeded"

    except Exception as error:
        return None, str(error)

    finally:
        os.remove(temp_path)


# PROJECT FEATURE EXTRACTOR (for Part 3)

ADVANCED_LIBRARIES = [
    "numpy", "pandas", "sklearn", "matplotlib", "seaborn",
    "tensorflow", "torch", "cv2", "flask", "django", "requests",
    "scipy", "plotly", "streamlit", "keras", "xgboost", "lightgbm",
    "nltk", "bs4", "selenium", "pygame", "pytest",
]


def count_lines(code):
    lines = [line for line in code.splitlines() if line.strip() != ""]
    return len(lines)


def count_functions_and_classes(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return 0, 0

    num_functions = 0
    num_classes = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            num_functions += 1
        elif isinstance(node, ast.ClassDef):
            num_classes += 1

    return num_functions, num_classes


def count_comments(code):
    count = 0
    try:
        tokens = tokenize.generate_tokens(io.StringIO(code).readline)
        for tok in tokens:
            if tok.type == tokenize.COMMENT:
                count += 1
    except (tokenize.TokenizeError, IndentationError, SyntaxError):
        pass
    return count


def get_imported_libraries(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return set()

    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name.split(".")[0].lower())
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported.add(node.module.split(".")[0].lower())

    return imported


def has_error_handling(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False

    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            return True
    return False


def extract_features(code_files):
    
    total_lines = 0
    num_functions = 0
    num_classes = 0
    num_comments = 0
    all_imported_libraries = set()
    any_error_handling = False

    for code in code_files:
        total_lines += count_lines(code)

        functions, classes = count_functions_and_classes(code)
        num_functions += functions
        num_classes += classes

        num_comments += count_comments(code)

        all_imported_libraries |= get_imported_libraries(code)

        if has_error_handling(code):
            any_error_handling = True

    adv_libs = len(all_imported_libraries & set(ADVANCED_LIBRARIES))

    return {
        "total_lines": total_lines,
        "num_functions": num_functions,
        "num_classes": num_classes,
        "num_comments": num_comments,
        "adv_libs": adv_libs,
        "error_handling": 1 if any_error_handling else 0,
    }


# LOAD TRAINED MODELS

@st.cache_resource
def load_project_model():
    with open(r"C:\Users\sukhm\OneDrive\Desktop\pydev\project_ml_place_chk\models\project_eval_model.pkl", "rb") as f:
        return pickle.load(f)


@st.cache_resource
def load_placement_model():
    with open(r"C:\Users\sukhm\OneDrive\Desktop\pydev\project_ml_place_chk\models\placement_model.pkl", "rb") as f:
        return pickle.load(f)


project_model = load_project_model()
placement_model = load_placement_model()


# INITIALIZATION SECTION

if "stage" not in st.session_state:
    st.session_state.stage = "info"

if "name" not in st.session_state:
    st.session_state.name = ""

if "roll" not in st.session_state:
    st.session_state.roll = ""

if "mcq_percentage" not in st.session_state:
    st.session_state.mcq_percentage = 0.0

if "code_test_percentage" not in st.session_state:
    st.session_state.code_test_percentage = 0.0

if "project_eval_score" not in st.session_state:
    st.session_state.project_eval_score = 0.0


# STYLING SECTION

st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 0.2rem;
    }
    .stage-badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        background-color: #4361ee;
        color: white;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">ML-Based Student Assessment Platform</div>', unsafe_allow_html=True)

STAGE_NAMES = {
    "info": "Step 0: Enter Your Details",
    "mcq": "Step 1: MCQ Test",
    "code_test": "Step 2: Code Submission",
    "project_eval": "Step 3: Project Evaluation",
    "placement_prediction": "Step 4: Placement Prediction",
}
st.markdown(
    f'<div class="stage-badge">{STAGE_NAMES[st.session_state.stage]}</div>',
    unsafe_allow_html=True,
)


# SCREEN 1: Student details  (shown only when stage == "info")

if st.session_state.stage == "info":
    name = st.text_input("Full Name")
    roll = st.text_input("Roll Number")

    if st.button("Start Test"):
        if name == "" or roll == "":
            st.warning("Please enter your name and roll number.")
        else:
            st.session_state.name = name
            st.session_state.roll = roll
            st.session_state.stage = "mcq"
            st.rerun()


# SCREEN 2: MCQ questions  (shown only when stage == "mcq")

elif st.session_state.stage == "mcq":
    st.write("Answer all questions below, then click Submit.")

    answers = []

    for i in range(len(MCQ_QUESTIONS)):
        mcq_question = MCQ_QUESTIONS[i]

        with st.container(border=True):
            st.markdown(f"**Q{i + 1}. {mcq_question['question']}**")
            selected_option = st.radio(
                "Choose one:",
                mcq_question["options"],
                key=f"question_{i}",
                index=None,
                label_visibility="collapsed",
            )
        answers.append(selected_option)

    if st.button("Submit Test"):
        if None in answers:
            st.warning("Please answer all questions before submitting.")
        else:
            correct_count = 0
            for i in range(len(MCQ_QUESTIONS)):
                mcq_question = MCQ_QUESTIONS[i]
                correct_option_text = mcq_question["options"][mcq_question["answer"]]
                if answers[i] == correct_option_text:
                    correct_count += 1

            # save silently - nothing shown on screen
            st.session_state.mcq_percentage = round((correct_count / len(MCQ_QUESTIONS)) * 100, 2)

            st.session_state.stage = "code_test"
            st.rerun()


# SCREEN 3: Code Submission  (shown only when stage == "code_test")

elif st.session_state.stage == "code_test":
    st.write("Write code for each problem below, then click Submit.")

    submitted_code = []

    for i in range(len(CODING_PROBLEMS)):
        problem = CODING_PROBLEMS[i]

        with st.container(border=True):
            st.markdown(f"**Problem {i + 1}: {problem['title']}**")
            st.text(problem["description"])
            code_text = st.text_area(
                "Your code:",
                key=f"code_{i}",
                height=150,
            )
        submitted_code.append(code_text)

    if st.button("Submit Code"):
        with st.spinner("Running your code against test cases..."):
            total_passed = 0
            total_cases = 0

            for i in range(len(CODING_PROBLEMS)):
                problem = CODING_PROBLEMS[i]
                code = submitted_code[i]

                for test_case in problem["test_cases"]:
                    total_cases += 1
                    output, error = run_student_code(code, test_case["input"])
                    if error is None and output == test_case["expected_output"]:
                        total_passed += 1

            # save silently - nothing shown on screen
            st.session_state.code_test_percentage = round((total_passed / total_cases) * 100, 2)

            st.session_state.stage = "project_eval"
            st.rerun()


# SCREEN 4: Project Evaluation  (shown only when stage == "project_eval")

elif st.session_state.stage == "project_eval":
    st.write("Upload all the .py files that make up your project, then click Submit.")

    uploaded_files = st.file_uploader(
        "Project files (.py)",
        type=["py"],
        accept_multiple_files=True,
    )

    if st.button("Submit Project"):
        if not uploaded_files:
            st.warning("Please upload at least one .py file.")
        else:
            code_files = []
            for uploaded_file in uploaded_files:
                file_bytes = uploaded_file.read()
                code_text = file_bytes.decode("utf-8", errors="ignore")
                code_files.append(code_text)

            with st.spinner("Evaluating your project..."):
                features = extract_features(code_files)
                features_df = pd.DataFrame([features])
                predicted_marks = project_model.predict(features_df)[0]
                predicted_marks = max(0, min(100, predicted_marks))

            # save silently - nothing shown on screen
            st.session_state.project_eval_score = round(predicted_marks, 2)

            st.session_state.stage = "placement_prediction"
            st.rerun()


# SCREEN 5: Placement Prediction  (shown only when stage == "placement_prediction")

elif st.session_state.stage == "placement_prediction":
    st.write("Enter your academic details below, then click Predict.")

    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
    internships = st.number_input("Number of Internships", min_value=0, max_value=20, step=1)
    projects_done = st.number_input("Number of Projects Done", min_value=0, max_value=50, step=1)
    backlogs = st.number_input("Total Backlogs", min_value=0, max_value=50, step=1)

    if st.button("Predict"):
        input_data = pd.DataFrame([{
            "cgpa": cgpa,
            "mcq_score": st.session_state.mcq_percentage,
            "code_score": st.session_state.code_test_percentage,
            "project_score": st.session_state.project_eval_score,
            "internships": internships,
            "projects_done": projects_done,
            "backlogs": backlogs,
        }])

        prediction = placement_model.predict(input_data)[0]

        st.divider()

        with st.container(border=True):
            if prediction == 1:
                st.success("Prediction: You are likely to be PLACED in the future.")
            else:
                st.warning("Prediction: You are NOT likely to be placed yet, based on your current profile.")
        # Personalized feedback - ONLY on MCQ, code test, internships,

        # backlogs. Deliberately NOT commenting on project quality or CGPA.

        st.subheader("Where You Can Improve")

        WEAK_THRESHOLD = 60  # below this percentage is considered weak

        feedback_given = False

        if st.session_state.mcq_percentage < WEAK_THRESHOLD:
            st.write("- Your MCQ score is on the lower side. Focus on strengthening your core concepts (OOPs, OS, COA, DSA, DAA).")
            feedback_given = True

        if st.session_state.code_test_percentage < WEAK_THRESHOLD:
            st.write("- Your code test score is on the lower side. Practice writing and debugging more code to improve.")
            feedback_given = True

        if internships == 0:
            st.write("- You currently have no internships. Try to take up at least one - it makes a real difference to placement chances.")
            feedback_given = True

        if backlogs > 0:
            st.write("- You have pending backlogs. Try to clear them as soon as possible.")
            feedback_given = True

        if not feedback_given:
            st.write("You're doing well across the board - keep it up!")


# Sidebar: shows only Stage, Name, Roll Number - no marks anywhere

st.sidebar.write("Saved data so far:")
st.sidebar.write("Stage:", st.session_state.stage)
st.sidebar.write("Name:", st.session_state.name)
st.sidebar.write("Roll Number:", st.session_state.roll)