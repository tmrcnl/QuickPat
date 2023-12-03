import lib.openaiapi as openaiapi
import pandas as pd
import lib.constants as constants
import lib.evaluate as evaluate
import rag

processed_patents_df = pd.read_parquet(constants.PROCESSED_FILE)
generated_abstracts_df = pd.read_csv(constants.GENERATED_ABSTRACTS_FILE)

df = pd.DataFrame(columns=['i', 'title', 'ground_truth_claims', 'generated_US_claims'])

# Open AI API parameters
temp_value = 1
max_tokens_value = 2006
top_p_value = 1
frequency_penalty_value = 0
presence_penalty_value = 0

US_claims_system = 'Based on the provided claim 1, generate 19 additional claims to form a complete set of 20 claims that conform to US patent law for a US patent application. The additional claims include both independent and dependent claims. Number the claims so that the subject matter claim categories are grouped together. All terms in the claims require antecedent basis, meaning that the first instance of a term is introduced with the word "a" and subsequent instances are referred to with "the". Do not include advantages in the claims. Example claim sets from other patents are provided for guidance on terminology. In the response, do not reproduce the instructions or claim 1.'

for _, patent in generated_abstracts_df.iterrows():
    print("--------------------------------------------------")

    generated_abstract = patent["generated_abstract"]
    i = patent["i"]
    first_claim = processed_patents_df.iloc[i]["claim_data"][0]

    # get closest records from DB
    top_k = 5 # 5 closest patent records from DB
    omit_index = i
    results = rag.RAGCall(generated_abstract, top_k, omit_index)
    example_claims = ' '.join(map(str, results['claim_data']))

    ground_truth_claims = processed_patents_df.iloc[i]["claim_data"]
    claims_prompt = 'Claim 1: ' + first_claim + '\n Example claims: ' + example_claims

    api_US_response = openaiapi.sendAPIRequest(US_claims_system, claims_prompt, temp_value, max_tokens_value, top_p_value, frequency_penalty_value, presence_penalty_value)
    generated_US_claims = first_claim + '\n\n' + api_US_response.choices[0].message.content

    # print('Ground truth claims: ', ground_truth_claims)
    # print('Generated US claims: ' , generated_US_claims)

    # append to df
    df = df._append({
        'i': i,
        'title': patent["title"],
        'ground_truth_claims': ground_truth_claims,
        'generated_US_claims': generated_US_claims
    }, ignore_index=True)

print("writing to file", constants.GENERATED_CLAIMS_FILE)
df.to_csv(constants.GENERATED_CLAIMS_FILE, index=False)
