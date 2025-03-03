import spacy
import pandas as pd
from Bio_Epidemiology_NER.bio_recognizer import ner_prediction

def process_text(corpus):
    """
    Process text using a pre-trained Named Entity Recognition (NER) model.
    
    Parameters:
    corpus (list of str): List of sentences or text documents to process.
    
    Returns:
    pd.DataFrame: A DataFrame containing extracted entities and metadata.
    """
    ner_df = pd.DataFrame()
    
    for doc in corpus:
        new_df = ner_prediction(corpus=doc, compute='cpu')
        new_df['sentence'] = doc
        ner_df = pd.concat([ner_df, new_df], ignore_index=True)
    
    return ner_df

if __name__ == "__main__":
    sample_texts = [
        "The aim of this paper is to develop methods for estimating reproduction numbers during an outbreak.",
        "COVID-19 has significantly impacted global healthcare systems."
    ]
    
    result_df = process_text(sample_texts)
    print(result_df.head())