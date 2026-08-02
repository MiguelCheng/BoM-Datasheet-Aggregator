import requests
import streamlit as st
from typing import Dict, Any, Optional

def search_digikey_sandbox(query: str, access_token: str) -> Optional[Dict[str, Any]]:
    """
    Queries Digi-Key's v4 Sandbox Keyword Search endpoint and validates payload structure.
    """
    url = "https://sandbox-api.digikey.com/products/v4/search/keyword"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-DIGIKEY-CLIENT-ID": st.secrets["digikey"]["CLIENT_ID"],
        "Content-Type": "application/json"
    }
    
    # Digi-Key v4 payload structure
    payload = {
        "Keywords": query,
        "RecordCount": 10
    }
    
    try:
        # /* user implementation: Make the POST request using requests.post */
        response = requests.post(url, headers=headers, json=payload, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        # Application-level validation: Check if payload contains products
        products = data.get("Products", [])
        if not products:
            # Handle empty result set gracefully
            return None
            
        return data

    except requests.exceptions.HTTPError as http_err:
        # /* user implementation: Handle specific status codes like 401 (Unauthorized) or 429 (Rate Limit) */
        return None
    except requests.exceptions.RequestException as req_err:
        # /* user implementation: Handle timeouts or network loss */
        return None