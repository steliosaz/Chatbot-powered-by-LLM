from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from openai import OpenAI
from langchain.chains import APIChain
from langchain_openai import OpenAI
import os
import app.doc as doc
import json

chatbot = FastAPI()

class Query(BaseModel):
    question : str

llm = OpenAI(api_key=os.environ.get('APIKEY') )

chain = APIChain.from_llm_and_api_docs(llm=llm,api_docs= doc.NEWS_DOCS,
    verbose=True,
    limit_to_domains=["http://api-service:8000"])

@chatbot.get("/")
def read_root():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'views', 'page.html')
    return FileResponse(file_path)

@chatbot.post("/QnA/")
async def handle_query(query : Query):
    try:
        res =  chain.invoke(query.question)
        return {"Response": json.dumps(res)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

