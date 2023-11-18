import lib.openaiapi as openaiapi
import pandas as pd
import lib.constants as constants
import lib.evaluate as evaluate

patents_df = pd.read_parquet(constants.PROCESSED_FILE)

# Open AI API parameters
temp_value = 1
max_tokens_value = 256
top_p_value = 1
frequency_penalty_value = 0
presence_penalty_value = 0

abstract_prompt = 'Generate a patent abstract from the provided claim that is suitable for use in a patent application. In the abstract, do not make reference to itself, or the words "abstract", "invention", "patent", "patent application", or "document". Avoid discussing the advantages or improvements of what is described. Use simple and plain language, but avoid using slang. Limit the abstract to 150 words.'

for i, patent in patents_df.iloc[:2].iterrows():
    print("--------------------------------------------------")
    # print(patent)

    ground_truth_abstract = patent["abstract"]
    first_claim = patent["claim_data"][0]

    api_response = openaiapi.sendAPIRequest(abstract_prompt, first_claim, temp_value, max_tokens_value, top_p_value, frequency_penalty_value, presence_penalty_value)
    generated_abstract = api_response.choices[0].message.content

    # evaluate generated abstract text (using sentence-transformers semanting embedding and cosine similarity)
    score_result = evaluate.evaluateGeneratedText(generated_abstract, ground_truth_abstract)
    
    print('Ground truth abstract: ', ground_truth_abstract)
    print('Generated abstract: ' , generated_abstract)
    print('Cosine similarity score: ', score_result)
    

# print(len(patents_df))
