import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import lib.constants as constants

print("reading from file", constants.PROCESSED_FILE)
patents_df = pd.read_parquet(constants.PROCESSED_FILE)

print("patents_df", patents_df)

# on which model to use: https://www.sbert.net/examples/applications/semantic-search/README.html
encoder = SentenceTransformer("paraphrase-mpnet-base-v2")

print("start encoding")
# encode using the abstract
text = patents_df['abstract']
vectors = encoder.encode(text)

print("done encoding", vectors.shape)

vector_dimension = vectors.shape[1]
index = faiss.IndexFlatL2(vector_dimension)
faiss.normalize_L2(vectors)

index.add(vectors)

print("index.ntotal", index.ntotal)

print("writing to file", constants.INDEX_FILE)
faiss.write_index(index, constants.INDEX_FILE)
