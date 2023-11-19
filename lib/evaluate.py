# evaluate the generated text as compared to the ground truth, using sentence_transformers

import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util
from . import openaiapi
import json

def evaluateGeneratedTextCosSim(generated_text, ground_truth):

    # initialize encoder
    encoder = SentenceTransformer("paraphrase-mpnet-base-v2")

    # encode generated text
    generated_embedding = encoder.encode(generated_text, convert_to_tensor=True)

    # encode ground truth text
    ground_embedding = encoder.encode(ground_truth, convert_to_tensor=True)

    # use cosine-similarity as a score
    cos_score = util.cos_sim(generated_embedding, ground_embedding)[0].item()

    return cos_score

def evaluateGeneratedTextEucDist(generated_text, ground_truth):

    # initialize encoder
    encoder = SentenceTransformer("paraphrase-mpnet-base-v2")

    # encode generated text
    generated_embedding = encoder.encode(generated_text, convert_to_tensor=True)

    # encode ground truth text
    ground_embedding = encoder.encode(ground_truth, convert_to_tensor=True)

    # use dot_score as a score
    cos_score = util.dot_score(generated_embedding, ground_embedding)[0].item()

    return cos_score

def evaluateUsingGPT4(generated_text):
    prompt = f'''
You are a patent lawyer and you are judging the quality of the given abstract. Give it a score from 1-5, 1 being the lowest and 5 being the best.

Give the result in pure json with two keys: "score" and "rational". Start and end the reply with curly braces. Do not use markdown syntax.
'''

    resp = openaiapi.sendAPIRequest(prompt, generated_text)

    return json.loads(resp.choices[0].message.content)['score']
