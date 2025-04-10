from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.agents.recommendation_agent import get_customer_data
from api.agents.product_recommendation_model import recommend_products

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Product Recommendation API is running!"}

@app.get("/recommend/{customer_id}")
def recommend_customer(customer_id: str):
    try:
        customer = get_customer_data(customer_id)
        if not customer:
            return {"error": f"No data found for Customer ID {customer_id}"}

        products = recommend_products(customer["browsing_history"])

        return {
            "customer_info": {
                "ID": customer["customer_id"],
                "Age": customer["age"],
                "Gender": customer["gender"],
                "Location": customer["location"],
                "Segment": customer["segment"],
                "Season": customer["season"],
                "Purchased_Products": customer["purchase_history"]  # ✅ NEW
            },
            "recommended_products": products
        }
    except Exception as e:
        return {"error": "Internal Server Error", "details": str(e)}
