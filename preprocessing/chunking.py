import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download necessary NLTK data
nltk.download(['punkt'])

def chunking_text(text, chunk_size=100):
    all_sentences = sent_tokenize(text)
    text_chunks = []
    chunks = []
    sent_len = 0

    for sent in all_sentences:
        sent_tokens = word_tokenize(sent)
        if sent_len + len(sent_tokens) <= chunk_size:
            chunks.extend(sent_tokens)
            sent_len += len(sent_tokens)
        else:
            text_chunks.append(' '.join(chunks))
            chunks = sent_tokens
            sent_len = len(sent_tokens)

    if chunks:
        text_chunks.append(' '.join(chunks))
    
    return text_chunks

def cluster_to_chunks(chunks , labels):
  clusters = {label:[] for label in set(labels)}
  for chunk,label in zip(chunks, labels):
    clusters[label].append(chunk)
  return clusters

