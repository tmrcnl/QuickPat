import os
import openai

# OpenAI API key setup (created this key specific for the project)
openai.api_key_path = "openai.apikey"

def sendAPIRequest(system_content, user_content, temp_value, max_tokens_value, top_p_value, frequency_penalty_value, presence_penalty_value):

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": system_content
        },
        {
          "role": "user",
          "content": user_content
        }
      ],
      temperature = temp_value,
      max_tokens = max_tokens_value,
      top_p = top_p_value,
      frequency_penalty = frequency_penalty_value,
      presence_penalty= presence_penalty_value
    )
    
    return response

# claim --> abstract example
# example from US20200354064A1 (Safe vertical take-off and landing aircraft payload assignment)
# https://patents.google.com/patent/US20200354064A1/

system_content = "Generate a patent abstract from the provided claim."
user_content = "Claim: A method, comprising:\nreceiving weight distribution criteria of a vertical take-off and landing (VTOL) aircraft;\nreceiving sensor information from the VTOL aircraft, the sensor information indicating a current payload weight distribution of the VTOL aircraft;\nreceiving a weight estimate of a payload associated with an individual; and\nassigning the individual to a particular location within the VTOL aircraft based, at least in part, on the weight estimate of the payload associated with the individual and the current payload weight distribution of the VTOL aircraft."

temp_value = 1
max_tokens_value = 256
top_p_value = 1
frequency_penalty_value = 0
presence_penalty_value = 0

test_response = sendAPIRequest(system_content, user_content, temp_value, max_tokens_value, top_p_value, frequency_penalty_value, presence_penalty_value)

print(test_response)