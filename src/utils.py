import pandas as pd

def clean_text(text):
    """
    Cleans the text by removing extra spaces and special characters.
    
    Parameters:
    text (str): The input text to clean.
    
    Returns:
    str: The cleaned text.
    """
    return ' '.join(text.split()).replace('\n', ' ')

def save_to_csv(df, filename):
    """
    Saves a Pandas DataFrame to a CSV file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    filename (str): The output file name.
    """
    df.to_csv(filename, index=False)

def load_csv(filename):
    """
    Loads a CSV file into a Pandas DataFrame.
    
    Parameters:
    filename (str): The CSV file path.
    
    Returns:
    pd.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(filename)

if __name__ == "__main__":
    sample_text = "  This is   an example text with    extra spaces.  "
    print(clean_text(sample_text))
    
    # Example usage with a DataFrame
    sample_df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']})
    save_to_csv(sample_df, "sample.csv")
    loaded_df = load_csv("sample.csv")
    print(loaded_df)
