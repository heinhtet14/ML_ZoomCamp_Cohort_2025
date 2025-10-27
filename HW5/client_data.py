# import requests

# url = "http://127.0.0.1:9696/predict"
# client = {
#     "lead_source": "organic_search",
#     "number_of_courses_viewed": 4,
#     "annual_income": 80304.0
# }

# response = requests.post(url, json=client).json()
# print(f"Response: {response}")
# print(f"Probability: {response['probability']:.3f}")


import requests

url = "http://localhost:9696/predict"

client = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

response = requests.post(url, json=client).json()
print(response)