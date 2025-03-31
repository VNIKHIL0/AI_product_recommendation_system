import ollama

def generate_recommendations(customer_info):
    query = f"Recommend top 5 products for a {customer_info[2]}-year-old customer in {customer_info[3]}"
    response = ollama.chat("mistral", messages=[{"role": "user", "content": query}])
    return response["message"]["content"]
