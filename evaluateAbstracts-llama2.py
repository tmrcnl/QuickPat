import lib.openaiapi as openaiapi
import pandas as pd
import lib.constants as constants
import lib.evaluate as evaluate

generated_abstracts_df = pd.read_csv(constants.GENERATED_ABSTRACTS_LLAMA2_FILE)

df = pd.DataFrame(columns=['i', 'title', 'ground_truth_abstract','generated_abstract', 'cosine_similarity', 'euclidean_distance', 'gpt4_score'])

for i, patent in generated_abstracts_df.iterrows():
    print("--------------------------------------------------")
    # print(patent)

    ground_truth_abstract = patent["ground_truth_abstract"]
    generated_abstract = patent["generated_abstract"]

    # evaluate generated abstract text (using sentence-transformers semanting embedding and cosine similarity)
    cos_sim = evaluate.evaluateGeneratedTextCosSim(generated_abstract, ground_truth_abstract)
    euc_dist = evaluate.evaluateGeneratedTextEucDist(generated_abstract, ground_truth_abstract)
    gpt4_score = evaluate.evaluateUsingGPT4(generated_abstract)

    print('Ground truth abstract: ', ground_truth_abstract)
    print('Generated abstract: ' , generated_abstract)
    print('Cosine similarity score: ', cos_sim)
    print('Euclidean distance score: ', euc_dist)
    print('GPT4 score: ', gpt4_score)

    df = df._append({
      'i': i,
      'title': patent['title'],
      'ground_truth_abstract': ground_truth_abstract,
      'generated_abstract': generated_abstract,
      'cosine_similarity': cos_sim,
      'euclidean_distance': euc_dist,
      'gpt4_score': gpt4_score,
    }, ignore_index=True)

print("writing to file", constants.EVALUATED_ABSTRACTS_LLAMA2_FILE)
df.to_csv(constants.EVALUATED_ABSTRACTS_LLAMA2_FILE, index=False)
