# import openai

# openai.api_key = "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"

# ask = input("ask-satori : ")

# response = openai.ChatCompletion.create(
#   model="gpt-4",
#   messages=[],
#   temperature=0.8,
#   max_tokens=1024
# )

# text = response['choices'][0]['text']
# print("satori: " + text)
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[],
  temperature=0.8,
  max_tokens=1024
)