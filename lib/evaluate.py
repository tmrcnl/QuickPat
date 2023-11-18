# evaluate the generated text as compared to the ground truth, using sentence_transformers

import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util

def evaluateGeneratedText(generated_text, ground_truth):

    # initialize encoder
    encoder = SentenceTransformer("paraphrase-mpnet-base-v2")

    # encode generated text
    generated_embedding = encoder.encode(generated_text, convert_to_tensor=True)

    # encode ground truth text
    ground_embedding = encoder.encode(ground_truth, convert_to_tensor=True)

    # use cosine-similarity as a score
    cos_score = util.cos_sim(generated_embedding, ground_embedding)[0].item()

    return cos_score

