# 💼 Salary Intelligence System

An end-to-end Machine Learning project that predicts salaries using job postings from Glassdoor.

This project combines:
- Structured tabular data
- Natural Language Processing (TF-IDF)
- Machine Learning regression models (XGBoost)

---

# 🚀 Project Overview

The goal is to predict annual salary based on:
- Job title
- Company rating
- Industry
- Location
- Job description (NLP)

---

# 🧠 Key Features

- Data cleaning & preprocessing
- Salary normalization (hourly → yearly)
- Feature engineering
- TF-IDF text vectorization
- Hybrid ML model (tabular + text)
- Model evaluation with MAE, RMSE, R²

---

# 🏗️ Pipeline Architecture

Raw Data  
→ Cleaning  
→ Feature Engineering  
→ TF-IDF (Job Description)  
→ Encoding Categorical Features  
→ XGBoost Model  
→ Evaluation  

---

# 📊 Model Performance

- MAE: ~9,000
- RMSE: ~18,300
- R²: ~0.78

---

# ⚙️ Tech Stack

- Python
- Pandas
- Scikit-learn
- XGBoost
- TF-IDF (NLP)

---

# 📁 Project Structure

See repository tree above.

---

# ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```
📌 Key Insights

* Job title and industry are strong salary predictors
* Location significantly affects compensation
* Job description improves prediction accuracy via NLP

⸻

📈 Future Improvements

* Hyperparameter tuning (XGBoost)
* SHAP explainability
* Deployment via FastAPI
* Model monitoring system


👩‍💻 Author

Fatemeh Amiri - AI Engineer | Computer Science Student