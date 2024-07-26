from sentence_transformers import SentenceTransformer

def create_embeddings(text_chunks):
    ST_model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = ST_model.encode(text_chunks)
    return embeddings

def re_embed_summaries(summaries):
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    re_embeddings = embedding_model.encode(summaries)
    return re_embeddings
