from fastapi import FastAPI, HTTPException
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import os
from fastapi.responses import JSONResponse

app = FastAPI()

os.environ["OPENAI_API_KEY"] = os.environ.get('APIKEY') 
loader = TextLoader('app/competition_results.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

@app.get("/search_department/{query}")
async def search_department(query: str):
    try:
        modified_query = query + " department"
        response =  index.query(modified_query)
        return JSONResponse(content={"query": query, "response": response})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/search_employee/{query}")
async def search_employee(query: str):
    try:
        modified_query = query + " employee"
        response =  index.query(modified_query)
        return JSONResponse(content={"query": query, "response": response})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))