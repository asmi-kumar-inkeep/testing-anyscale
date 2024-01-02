import openai
import pandas as pd
import csv

csv_file_path = '/Users/asmi/Documents/testing-anyscale/2024-01-02-results_rows.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)
# print(df.head())

# Get column names
column_names = df.columns.tolist()
# print("\nColumn names:")
# print(column_names)

input_columns = ['question', 'answer', 'subject_name', 'project_description']

# Choose a specific row to analyze
row = 0
if row < 0 or row >= len(df):
    print("Invalid row number. Please choose a valid row.")
    exit()

# Concatenate text from multiple columns into one big string
user_content = ". ".join(f"{col}: {df.iloc[row][col]}" for col in input_columns)
# print("\User content:")
# print(user_content)

# Prompt
system_content = '''Your job is to provide a summary of the question ONLY. Don't use the answer or any other part of the input, just the question.
                Question summary should be a succinct version of the question that captures the key details but can be expressed 
                as single short question. Imagine this was a google search query framed as a question that you would type into a search bar 
                to find relevant information about the question. **BAD** do not include "in \{subject_name\}" in the summary, it's assumed already.
                '''

# Set up OpenAI client
client = openai.OpenAI(
    base_url="https://api.endpoints.anyscale.com/v1",
    api_key="esecret_miz7vax57b19znd5v9pflkva7y"
)

# Make the OpenAI API call
chat_completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ],
    temperature=0.7
)

# Get the generated product names from the API response
product_names = chat_completion.choices[0].message.content

print("\nResults from Anyscale Endpoint:\n", product_names)
