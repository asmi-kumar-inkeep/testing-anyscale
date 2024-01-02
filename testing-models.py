import openai

system_content = "You will be provided with a product description and seed words. Your task is to generate potential product names. Make them diverse (so don't end with the same word each time)."
user_content = "Product description: A home milkshake maker. Seed words: fast, healthy, compact."

client = openai.OpenAI(
           base_url = "https://api.endpoints.anyscale.com/v1",
           api_key="esecret_miz7vax57b19znd5v9pflkva7y"
        )
chat_completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[{"role": "system", "content": system_content},
              {"role": "user", "content": user_content}],
    temperature=0.7
)

product_names = chat_completion.choices[0].message.content
print("Results from Anyscale Endpoint:\n", product_names)