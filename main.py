import os
from dotenv import load_dotenv
from data.data_extractor import extract_text_from_pdf
from preprocessing.chunking import chunking_text
from embeddings.embedding import create_embeddings
from preprocessing.clustering import perform_clustering
from preprocessing.chunking import cluster_to_chunks
from model.model import load_summarizer
from model.summarizer import summarize_book

def main():
    book1_path_file = './data/dataset/Book1.pdf'
    book2_path_file = './data/dataset/Book2.pdf'
    book3_path_file = './data/dataset/Book3.pdf'

    book1_text = extract_text_from_pdf(book1_path_file)
    book2_text = extract_text_from_pdf(book2_path_file)
    book3_text = extract_text_from_pdf(book3_path_file)

    book1_sent_chunks = chunking_text(book1_text)
    book2_sent_chunks = chunking_text(book2_text)
    book3_sent_chunks = chunking_text(book3_text)

    book1_embedding = create_embeddings(book1_sent_chunks)
    book2_embedding = create_embeddings(book2_sent_chunks)
    book3_embedding = create_embeddings(book3_sent_chunks)

    book1_clustering, _ = perform_clustering(book1_embedding)
    book2_clustering, _ = perform_clustering(book2_embedding)
    book3_clustering, _ = perform_clustering(book3_embedding)
    
    book1_clustered_chunks = cluster_to_chunks(book1_sent_chunks , book1_clustering)
    book2_clustered_chunks = cluster_to_chunks(book2_sent_chunks,book2_clustering)
    book3_clustered_chunks = cluster_to_chunks(book3_sent_chunks , book3_clustering)
    
    # for labels , chunks in book1_clustered_chunks.items():
    #     print(len(chunks))
    summarizer = load_summarizer()

    book1_summary = summarize_book(book1_clustered_chunks,summarizer)
    # book2_summary = summarize_book(book2_clustered_chunks, model, tokenizer)
    # book3_summary = summarize_book(book3_clustered_chunks, model, tokenizer)

    # print("Book 1 Summary:")
    # print(book1_summary)
    # print("Book 2 Summary:")
    # print(book2_summary)
    # print("Book 3 Summary:")
    # print(book3_summary)

if __name__ == "__main__":
    main()
