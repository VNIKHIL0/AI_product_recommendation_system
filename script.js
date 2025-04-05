async function fetchRecommendations() {
    const customerId = document.getElementById("customer-id").value.trim();
    const BASE_URL = "https://ai-product-recommendation-system-6gde.onrender.com";
    const apiUrl = `${BASE_URL}/recommend/${customerId}`;
    const loader = document.getElementById("loader");
    const resultDiv = document.getElementById("result");
    const customerInfo = document.getElementById("customer-info");
    const recommendationsList = document.getElementById("recommendations");

    if (!customerId) {
        alert("Please enter a Customer ID!");
        return;
    }

    loader.style.display = "block"; 
    resultDiv.style.display = "none"; 

    setTimeout(async () => {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

            const data = await response.json();
            loader.style.display = "none";
            resultDiv.style.display = "block";

            customerInfo.innerHTML = `Customer: ${customerId}`;
            recommendationsList.innerHTML = data.recommended_products.map(p => `<li>${p}</li>`).join('');
        } catch (error) {
            loader.style.display = "none";
            resultDiv.style.display = "block";
            customerInfo.innerHTML = "❌ API connection failed!";
            recommendationsList.innerHTML = "";
            console.error("Failed to fetch recommendations!", error);
        }
    }, 5000); 
}
