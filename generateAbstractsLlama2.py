import lib.constants as constants
import lib.llama as llama
import pandas as pd

patents_df = pd.read_parquet(constants.PROCESSED_FILE)
df = pd.DataFrame(columns=['i', 'title', 'ground_truth_abstract', 'generated_abstract'])

abstract_system = 'Generate a patent abstract from the provided claim that is suitable for use in a patent application. In the abstract, do not make reference to the words "abstract", "invention", "patent", "patent application", or "document". Do not discuss the advantages or improvements. Use simple and plain language, but avoid using slang. Limit the abstract to 150 words.'

for i in constants.PATENT_INDICES:
    print("--------------------------------------------------")
    patent = patents_df.iloc[i]
    # print(patent)

    ground_truth_abstract = patent["abstract"]
    first_claim = patent["claim_data"][0]

    generated_abstract = llama.generate(abstract_system, first_claim)

    print('Ground truth abstract: ', ground_truth_abstract)
    print('Generated abstract: ' , generated_abstract)

    df = df._append({
        'i': i,
        'title': patent["title"],
        'ground_truth_abstract': ground_truth_abstract,
        'generated_abstract': generated_abstract,
    }, ignore_index=True)

print("writing to file", constants.GENERATED_ABSTRACTS_LLAMA2_FILE)
df.to_csv(constants.GENERATED_ABSTRACTS_LLAMA2_FILE, index=False)
