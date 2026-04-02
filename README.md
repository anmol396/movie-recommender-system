# 🎬 Movie Recommender System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NLP-TF--IDF%20%2B%20Cosine-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

---

## 📌 Overview

This project is a **Content-Based Movie Recommendation System** built using **Machine Learning and NLP techniques**.

It recommends movies based on similarity using:
- Genres  
- Keywords  
- Cast  
- Director  
- Tagline  

The system is implemented with an **interactive Streamlit web application**.

---

## ✨ Features

- 🎬 Recommend similar movies instantly  
- 🔍 Search using dropdown or manual input  
- ⭐ Filter by rating  
- 📊 Sort by popularity or rating  
- 🔥 Highlight top recommendation  
- 🎨 Clean and modern UI  
- ⚡ Fast performance using caching  

---

## 🛠️ Tech Stack

| Category        | Tools / Libraries Used |
|----------------|----------------------|
| 🐍 Programming  | Python |
| 📊 Data Handling| Pandas, NumPy |
| 🤖 ML / NLP     | Scikit-learn (TF-IDF, Cosine Similarity) |
| 📈 Visualization| Matplotlib, Seaborn |
| 🌐 Web App      | Streamlit |

---

## 🧠 How It Works

1. Combine features (genres, keywords, cast, director, tagline)  
2. Convert text into vectors using **TF-IDF**  
3. Compute similarity using **Cosine Similarity**  
4. Recommend top similar movies  

---

## 📂 Project Structure

```

movie-recommendation-system/
│
├── data/
│   └── movies.csv
│
├── app/
│   └── app.py
│
├── src/
│
├── notebook/
│   └── movie_recommendation.ipynb
│
├── requirements.txt
├── README.md
└── LICENSE

````

---

## ⚙️ Installation

```
git clone https://github.com/anmol396/movie-recommender-system.git
cd movie-recommender-system
```
pip install -r requirements.txt

---

## ▶️ Run the Application

```
streamlit run app/app.py
```

👉 Open in browser:
[http://localhost:8501](http://localhost:8501)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) file.





