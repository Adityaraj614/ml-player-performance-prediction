# 🎮 Player Performance Prediction (Machine Learning)

## 📌 What is this?
Before diving into advanced Deep Learning or Game AI, I wanted to master the "bread and butter" of AI: **Classical Machine Learning**. This project is an end-to-end pipeline that predicts player performance levels based on their in-game statistics. 

It’s not just about getting a high accuracy score; it’s about understanding how raw gameplay data is transformed into actionable insights.

---

## 🎯 Why I Built This
As a 3rd-year CS student focusing on AI, I believe you can’t build great Neural Networks without first mastering **Supervised Learning**. 

Player analytics is a massive part of the gaming industry—from matchmaking to performance tracking. I built this to bridge the gap between ML theory and a workflow that I’m actually passionate about.

---

## 🧠 The Challenge
The goal was to see if a model could accurately classify player skill by analyzing:
* **🎯 Accuracy (%)** – Precision under pressure.
* **⏱️ Time Played** – Experience vs. raw skill.
* **☠️ K/D Ratio** – Efficiency in combat.
* **🏆 Total Score** – The final performance metric.

---

## 🛠 What I Learned (The "Hard" Way)
This project went deeper than just running `model.fit()`. My biggest takeaways came from the "boring" parts that actually make or break a model:

* **Feature Scaling:** I discovered firsthand why Logistic Regression struggles when features are on different scales and how `StandardScaler` fixes it.
* **Model Selection:** I realized that "fancier" isn't always better. While Random Forest is powerful, a well-tuned linear model was more suited for this specific dataset.
* **Evaluation Metrics:** Learned that Accuracy is a lie if you don't look at the **Confusion Matrix** and **Precision-Recall** to see where the model is actually failing.

---

## 📂 Project Structure
* `data/` – Synthetic gameplay datasets.
* `notebooks/` – Exploratory Data Analysis (EDA) and visualization.
* `src/` – Clean, modular code for preprocessing and training.

---

## 🤖 The Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy (Data Handling), Scikit-Learn (ML), Seaborn/Matplotlib (Visualization).
* **Models Tested:** Logistic Regression (Winner) and Random Forest.

---

## 🏆 Final Result
I chose **Logistic Regression (with scaling)** as my final model. It provided the best generalization and aligned perfectly with the linear structure of the gameplay scoring logic. It proved that sometimes, a simpler model is the most robust solution.

---

## 🚀 What’s Next?
* Testing the pipeline on real-world datasets (like CS:GO or Valorant API data).
* Implementing **SHAP values** to explain *why* the model flags a player as "High Performance."
