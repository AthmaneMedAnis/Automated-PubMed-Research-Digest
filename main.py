import argparse

from os import path, makedirs
from src.fetcher import fetch_pubmed
from src.parser import pubmed_to_df
from src.visualizer import generate_wordcloud
from src.reporter import generate_pdf

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("keywords", nargs="+", help="Input keywords")
	parser.add_argument("-max", default=10, type=int, help="Input maximum number of articles to return")
	parser.add_argument("-email", required=True, help="Input user email")
	parser.add_argument("-o", "--output", help="Output folder for the results")
	return parser.parse_args()

def output_checker(keywords:list, output:str=''):
    if not output:
        output = "Output"
    output = path.join(output, "_".join(keywords))
    if not path.exists(output):
        makedirs(output)
    return output

def main():
    args = parse_arguments()
    keywords = ' '.join(args.keywords)
    output_folder = output_checker( keywords=args.keywords, output=args.output)
    
    fetch_handle = fetch_pubmed(query=keywords, email=args.email, max_result=args.max)
    if fetch_handle:
        res_df = pubmed_to_df(fetch_handle=fetch_handle)
        res_df.to_csv(path.join(output_folder, "results.csv"), index=False, sep="\t")
        
        image_filename = path.join(output_folder, "wordcloud.png")
        
        if "Abstract" in res_df.columns:
            generate_wordcloud(abstract_text=res_df["Abstract"], output_path=image_filename)
        else:
            print("No abstracts found to visualize.")
            
        pdf_filename = path.join(output_folder, "report.pdf")
        generate_pdf(
            df=res_df, 
            query=keywords, 
            image_path=image_filename, 
            output_pdf_path=pdf_filename
        )
    else:
        print("Fetch error.")

if __name__ == "__main__":
	main()