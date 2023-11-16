import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import lib.constants as constants

df = pd.read_parquet(constants.PROCESSED_FILE)
index = faiss.read_index(constants.INDEX_FILE)

# on which model to use: https://www.sbert.net/examples/applications/semantic-search/README.html
encoder = SentenceTransformer("paraphrase-mpnet-base-v2")

search_query = df.iloc[0]['abstract']
print("search_query:", search_query)

search_vector = encoder.encode(search_query)
_vector = np.array([search_vector])
faiss.normalize_L2(_vector)

k = index.ntotal
distances, ann = index.search(_vector, k=k)

results = pd.DataFrame({'distances': distances[0], 'ann': ann[0]})

merge = pd.merge(results, df, left_on='ann', right_index=True)

print("merge:", merge)

print("closest abstracts:")
for abstract in merge.iloc[:5]['abstract']:
    print("abstract:")
    print(abstract)

# print(ann[0][:5])
# print(df.iloc[ann[0][:5]])
