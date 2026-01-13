from Bio import Medline
import pandas as pd

def pubmed_to_df(fetch_handle):
    """
    Parses the Medline handle into a clean DataFrame.
    """
    
    records = Medline.parse(fetch_handle)
    records = list(records)
    fetch_handle.close()

    df = pd.DataFrame(records)
    
    column_map = {
        "TI": "Title",
        "AB": "Abstract",
        "JT": "Journal",
        "DP": "Date of Publication",
        "AU": "Authors",
        "PMID": "PMID"
    }
    
    existing_cols = [c for c in column_map.keys() if c in df.columns]
    df = df[existing_cols].rename(columns=column_map)
    
    if "Abstract" in df.columns:
        df["Abstract"] = df["Abstract"].fillna("No Abstract Available")
        
    return df