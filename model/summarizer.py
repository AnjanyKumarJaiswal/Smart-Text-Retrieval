import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

def summarize_book(clustered_chunk,summarizer, max_length=300, min_length=20 , batch_size=10):
    book_summaries = []
    for labels, chunks in clustered_chunk.items():
        batch_summaries=[]
        for i in range(0,len(chunks),batch_size):
            batch = chunks[i:i+batch_size]
            batch_summary = summarizer(batch , max_length=max_length , min_length=min_length, do_sample=False)
            # print(len(batch_summary))
            # print(batch_summary)
            batch_summaries.extend([result['summary_text'] for result in batch_summary])
        final_book_summary = ''.join(batch_summaries)
        print(len(final_book_summary))
        final_summary = summarizer(final_book_summary , max_length=max_length,min_length=min_length, do_sample=False)
        book_summaries.append(final_summary)
    print(book_summaries)
    return book_summaries
    
