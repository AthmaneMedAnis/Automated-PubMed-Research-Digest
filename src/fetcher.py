from Bio import Entrez

def fetch_pubmed(query:str, email:str, max_result:int):
    """
    Searches PubMed and returns a handle to the results.
    """
    
    Entrez.email = email

    search_handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_result
    )
    search_results = Entrez.read(search_handle)
    search_handle.close()

    id_list = search_results["IdList"]

    fetch_handle = Entrez.efetch(
        db="pubmed",
        id=id_list,
        rettype="medline",
        retmode="text"
    )

    return fetch_handle