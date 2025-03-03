# Knowledge Graph Construction using Named Entity Recognition (NER)

This repository contains a **Knowledge Graph Construction** pipeline using **Named Entity Recognition (NER)**. It extracts entities from text, builds a knowledge graph, and provides tools for data scraping and text processing.

## 📌 Project Overview
The goal of this project is to extract relationships between named entities from text data and represent them as a **Knowledge Graph**. This is achieved using:
- **NER models** (custom biomedical models from `Bio_Epidemiology_NER`)
- **Graph representation with NetworkX**
- **Text scraping & preprocessing utilities**

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/muditbaid/Semantic-Knowledge-Graph-from-Covid-ResearchCorpus.git
cd Semantic-Knowledge-Graph-from-Covid-ResearchCorpus
```

### 2️⃣ Install Dependencies
Create a virtual environment and install required libraries:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### 3️⃣ Run the Pipeline
You can use the provided scripts to:
- Process text with NER
- Build a knowledge graph
- Scrape data from the web

#### **Run Named Entity Recognition (NER) on Sample Texts**
```python
from src.ner_pipeline import process_text

sample_texts = ["COVID-19 has impacted global healthcare systems."]
ner_results = process_text(sample_texts)
print(ner_results.head())
```

#### **Build & Visualize the Knowledge Graph**
```python
from src.graph_builder import build_knowledge_graph, visualize_graph

knowledge_graph = build_knowledge_graph(ner_results)
visualize_graph(knowledge_graph)
```

#### **Scrape Text from a Website**
```python
from src.scraper import scrape_text

sample_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
scraped_text = scrape_text(sample_url)
print(scraped_text[:500])
```

## 📂 Repository Structure
```
.
├── data/                 # Contains sample text data (if available)
├── src/                  # Core scripts
│   ├── ner_pipeline.py   # Named Entity Recognition pipeline
│   ├── graph_builder.py  # Builds & visualizes the knowledge graph
│   ├── scraper.py        # Web scraping for text data
│   ├── utils.py          # Helper functions
├── notebooks/            # Jupyter notebooks
│   ├── knowledge_graph.ipynb   # Notebook for NER and Knowledge Graph 
├── results/              # Stores generated knowledge graphs & reports
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
├── .gitignore            # Ignore unnecessary files
└── .gitattributes        # If using Git LFS for large files
```

## 🛠️ Future Improvements
- Use **TF-IDF vectorization** for better entity extraction.
- Fine-tune hyperparameters for **higher accuracy**.
- Improve graph relationship extraction with **dependency parsing**.

## 📌 References
- [SpaCy NER](https://spacy.io/usage/linguistic-features#named-entities)
- [NetworkX Graphs](https://networkx.org/)
- [BeautifulSoup for Scraping](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 📝 License
This project is for educational purposes. Free to use with attribution.

---
Feel free to contribute by submitting a pull request! 🚀

