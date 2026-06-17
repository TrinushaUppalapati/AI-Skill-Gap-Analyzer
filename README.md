# 🚀 AI Skill Gap Analyzer

A simple, interactive Streamlit web app that helps you find missing skills for your dream job role and generates a prioritized learning roadmap to close the gap.

## 📋 Overview

The AI Skill Gap Analyzer compares the skills you currently have against the skills required for a chosen job role. It calculates a readiness score, highlights skills you already possess, identifies what's missing, and suggests a learning roadmap to help you get job-ready.

## ✨ Features

- **Role Selection** – Choose from a list of predefined job roles to analyze against.
- **Skill Matching** – Enter your skills as a comma-separated list; matching is case-insensitive.
- **Readiness Score** – Get a percentage score showing how well your skills align with the selected role.
- **Matched vs Missing Skills** – Clearly see which required skills you already have and which ones you don't.
- **Learning Roadmap** – A prioritized, numbered list of skills to learn next.
- **Clean UI** – Built with Streamlit, using metrics, columns, and visual feedback (success/info/warning messages, balloons on a perfect match).

## 🛠️ Tech Stack

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – for the web interface

## 📁 Project Structure

```
ai-skill-gap-analyzer/
│
├── app.py              # Main Streamlit application
├── skills_data.py       # Dictionary of job roles and their required skills
├── requirements.txt     # Python dependencies
└── README.md
```

> **Note:** `skills_data.py` must define a `job_roles` dictionary mapping job role names to a list of required skills, for example:
> ```python
> job_roles = {
>     "Data Scientist": ["Python", "Machine Learning", "SQL", "Statistics"],
>     "Frontend Developer": ["JavaScript", "React", "HTML", "CSS"],
> }
> ```

## ⚙️ Installation

1. Clone the repository
   ```bash
   git clone https://github.com/TrinushaUppalapati/AI-Skill-Gap-Analyzer/tree/main ai-skill-gap-analyzer
   ```

2. (Optional) Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install streamlit
   ```

## ▶️ Usage

Run the app with Streamlit:

```bash
streamlit run app.py
```

Then, in the app:

1. Select your dream job role from the dropdown.
2. Enter your current skills as a comma-separated list (e.g., `Python, Machine Learning, Data Analysis, SQL`).
3. Click **📊 Analyze Skills**.
4. Review your readiness score, matched skills, missing skills, and the suggested learning roadmap.

## 🧮 How It Works

1. User-entered skills are cleaned, lowercased, and converted to a set.
2. Required skills for the selected role are fetched from `job_roles` and also lowercased for comparison.
3. Set intersection finds **matched skills**; set difference finds **missing skills**.
4. The readiness score is calculated as:
   ```
   score = (matched skills / total required skills) * 100
   ```
5. If skills are missing, a numbered learning roadmap is generated listing them in order.

## 🔮 Future Improvements

- Add more job roles and keep skill lists up to date with industry trends.
- Support resume upload / parsing instead of manual skill entry.
- Recommend specific courses or resources for each missing skill.
- Allow custom/user-defined job roles.
- Add skill proficiency levels instead of a simple have/don't-have check.

