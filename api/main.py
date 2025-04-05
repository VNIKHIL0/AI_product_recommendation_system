from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.agents.recommendation_agent import get_customer_preferences
from api.agents.product_recommendation_model import recommend_products

app = FastAPI()

# ✅ CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Product Recommendation API is running!"}

@app.get("/recommend/{customer_id}")
def recommend_customer(customer_id: str):
    return get_product_recommendations(customer_id)

def get_product_recommendations(customer_id: str):
    try:
        print(f"Fetching preferences for customer: {customer_id}")
        preferences = get_customer_preferences(customer_id)

        if not preferences:
            return {"customer_id": customer_id, "recommended_products": ["No recommendations available"]}

        print(f"Customer preferences: {preferences}")
        recommended_products = recommend_products(preferences)

        print(f"Recommended products: {recommended_products}")
        return {"customer_id": customer_id, "recommended_products": recommended_products}

    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": "Internal Server Error", "details": str(e)}
