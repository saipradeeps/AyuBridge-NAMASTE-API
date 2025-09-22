from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List, Dict

app = FastAPI(
    title="NAMASTE-ICD-11 API",
    description="A simple API to map NAMASTE codes to ICD-11 Traditional Medicine codes.",
    version="1.0.0"
)

# --- Add this CORS middleware section ---
# This allows your frontend (running on any origin "*") to communicate with this backend.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- End of CORS section ---


try:
    # Make sure this file is in the same directory as main.py
    with open("namaste_icd_mapping.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("WARNING: namaste_icd_mapping.json not found. The API will return empty results.")
    data = [] 

@app.get("/search", tags=["Search"], response_model=List[Dict])
async def search_codes(query: str):
    """
    Search for a disease by a given query string in both NAMASTE and ICD-11 terms.
    Returns a list of matching entries.
    """
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required.")
    
    query = query.lower()
    
    results = [
        item for item in data 
        if query in item["namaste_term"].lower() or query in item["icd11_term"].lower()
    ]
    
    # Returning an empty list is more user-friendly than a 404 for search
    return results


@app.get("/map/namaste/{namaste_code}", tags=["Mapping"], response_model=Dict)
async def map_namaste_to_icd11(namaste_code: str):
    """
    Retrieve ICD-11 details for a given NAMASTE code.
    """
    namaste_code_lower = namaste_code.lower()
    
    for item in data:
        if item["namaste_code"].lower() == namaste_code_lower:
            return {
                "namaste_code": item["namaste_code"],
                "icd11_code": item["icd11_code"],
                "icd11_term": item["icd11_term"]
            }
            
    raise HTTPException(status_code=404, detail=f"NAMASTE code '{namaste_code}' not found.")
    

@app.get("/map/icd11/{icd11_code}", tags=["Mapping"], response_model=Dict)
async def map_icd11_to_namaste(icd11_code: str):
    """
    Retrieve NAMASTE details for a given ICD-11 code.
    """
    icd11_code_lower = icd11_code.lower()
    
    for item in data:
        if item["icd11_code"].lower() == icd11_code_lower:
            return {
                "icd11_code": item["icd11_code"],
                "icd11_term": item["icd11_term"],
                "namaste_code": item["namaste_code"],
                "namaste_term": item["namaste_term"]
            }
            
    raise HTTPException(status_code=404, detail=f"ICD-11 code '{icd11_code}' not found.")
