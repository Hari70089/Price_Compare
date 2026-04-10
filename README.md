# 💊 E-Pharma Price Comparison Tool

A real-time medicine and healthcare product price comparison web app built with **Streamlit** and powered by **SerpApi Google Shopping**.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![SerpApi](https://img.shields.io/badge/SerpApi-Google%20Shopping-green)

---

## 📌 About

**E-Pharma Price Comparison Tool** helps users compare medicine and healthcare product prices across multiple online stores in real time. Instead of manually searching across websites, just type a product name and instantly see the best deals — with charts, buy links, and a clear best-option recommendation.

---

## ✨ Features

- 🔎 **Real-time price search** across multiple online pharmacies and stores
- 🏆 **Best deal detection** — automatically highlights the lowest priced option
- 🛒 **Direct buy links** for each product listing
- 🖼️ **Product thumbnail preview** for quick identification
- 📊 **Bar chart & pie chart** visualizations to compare prices at a glance

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| `Streamlit` | Web app UI |
| `SerpApi` | Google Shopping live data |
| `Pandas` | Data handling |
| `Matplotlib` | Charts & graphs |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Hari70089/Price_compare.git
cd Price_compare
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your SerpApi key

Create a `.streamlit/secrets.toml` file:

```toml
SERPAPI_KEY = "your_serpapi_key_here"
```

> 🔑 Get your free API key at [serpapi.com](https://serpapi.com)

### 4. Run the app

```bash
streamlit run Price_compare.py
```

---

## 📁 Project Structure

```
Price_compare/
├── Price_compare.py       # Main Streamlit app
├── requirements.txt       # Python dependencies
├── e_pharm_logo.png       # App logo
└── README.md              # Project documentation
```

---

## 📦 Requirements

```
serpapi
google-search-results
pandas
streamlit
matplotlib
```

---

## 🌐 Live Demo

Hosted on **Streamlit Community Cloud**:
👉 [Click here to open the app](https://share.streamlit.io/Hari70089/Price_compare/main/Price_compare.py)

---

## ⚠️ Important Notes

- Make sure your `requirements.txt` is named exactly `requirements.txt` (Streamlit Cloud won't detect other spellings)
- Never hardcode your API key in the source code — use `st.secrets` instead
- SerpApi free tier has a limited number of monthly searches

---

## 🙋 Author

**Hari** — [GitHub Profile](https://github.com/Hari70089)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
