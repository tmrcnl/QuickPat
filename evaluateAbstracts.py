import lib.openaiapi as openaiapi
import pandas as pd
import lib.constants as constants
import lib.evaluate as evaluate

generated_abstracts_df = pd.read_csv(constants.GENERATED_ABSTRACTS_FILE)

df = pd.DataFrame(columns=['i', 'title', 'cosine_similarity', 'euclidean_distance'])

for i, patent in generated_abstracts_df.iterrows():
    print("--------------------------------------------------")
    # print(patent)

    ground_truth_abstract = patent["ground_truth_abstract"]
    generated_abstract = patent["generated_abstract"]

    # evaluate generated abstract text (using sentence-transformers semanting embedding and cosine similarity)
    cos_sim = evaluate.evaluateGeneratedTextCosSim(generated_abstract, ground_truth_abstract)
    euc_dist = evaluate.evaluateGeneratedTextEucDist(generated_abstract, ground_truth_abstract)

    print('Ground truth abstract: ', ground_truth_abstract)
    print('Generated abstract: ' , generated_abstract)
    print('Cosine similarity score: ', cos_sim)
    print('Euclidean distance score: ', euc_dist)

    df = df._append({
        'i': i,
          'title': patent['title'],
            'cosine_similarity': cos_sim,
              'euclidean_distance': euc_dist,
            }, ignore_index=True)

print("writing to file", constants.EVALUATED_ABSTRACTS_FILE)
df.to_csv(constants.EVALUATED_ABSTRACTS_FILE, index=False)
