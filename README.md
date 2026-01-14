# Automated-PubMed-Research-Digest

**An automated pipeline to fetch, analyze, and report biomedical research.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Bioinformatics](https://img.shields.io/badge/Focus-Bioinformatics-green?logo=dna)
![Status](https://img.shields.io/badge/Status-Portfolio_Ready-orange)

## 📌 Overview

Literature review is a bottleneck in biomedical research. **Auto-PubMed Digest** is a Python-based automation tool designed to streamline this process.

It connects directly to the **NCBI PubMed Database** via API, fetches research papers based on user-defined keywords, and automatically generates a comprehensive **PDF Report**. The tool transforms unstructured metadata into actionable insights, providing researchers with a structured CSV dataset and a visual Word Cloud of trending topics.

## 🚀 Key Features

* **🔍 Automated Scraping:** Uses `Bio.Entrez` to query the PubMed API for real-time data.
* **📊 Data Structuring:** Parses complex Medline files into clean, analysis-ready **Pandas DataFrames**.
* **🎨 Semantic Visualization:** Generates high-resolution **Word Clouds** to instantly identify research trends.
* **📑 Smart Reporting:** Auto-generates a professional **PDF Digest** containing summaries and metadata, ready for distribution.
* **📁 Dynamic File Management:** Automatically organizes outputs into keyword-specific directories.

## 🛠️ Tech Stack

* **Core:** Python 3.x
* **Bioinformatics:** `Biopython` (Entrez API, Medline Parsing)
* **Data Science:** `Pandas` (Data Manipulation), `Matplotlib` (Plotting)
* **NLP & Viz:** `WordCloud`
* **Reporting:** `FPDF` (PDF Generation)

## 📂 Project Structure

```text
├── src/
│   ├── fetcher.py       # Handles NCBI API connection and data retrieval
│   ├── parser.py        # Cleans and structures raw Medline data
│   ├── visualizer.py    # Generates semantic word cloud images
│   └── reporter.py      # Compiles data into a polished PDF report
├── main.py              # CLI Entry point and pipeline orchestrator
├── requirements.txt     # Dependencies
└── README.md            # Documentation