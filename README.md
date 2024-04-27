# Building a Chatbot with API routing with FastAPI.

## Overview:

I implemented the chatbot using LLM from OpenAI, integrated with API keys and Langchain framework for managing dialogue and decision-making processes. 

The user can ask the chatbot a question about content relevant to the context given. 
The core of the system involves the Vector Store which constructs a similarity search index from a context file. This index enables the chatbot to accurately respond to queries about the given context determing releveant department or employee detailes based on users query. The users query is also processed by the LLM and Langchain library, which utilizes API documentation to guide the LLM in making intelligent decisions about which endpoint to invoke based on the user's input.This documentation effectively maps user queries to the appropriate API calls.

![Chatbotflow](https://github.com/steliosaz/Chatbot-powered-by-LLM/assets/139654652/0045137e-9cb6-4701-a951-6a89f70e9a3b)


## Dockerization Details:

Both services are containerized into two seperate containers running at the same network on different ports. I utilized docker compose for achieving communication between containers. 

## How to run:
1. [Download docker compose](https://docs.docker.com/compose/install/)

2. You also need to obtain an OpenAI API key and insert it in both Dockerfiles.

3. Run below command to start the containers:
```shell script
docker-compose up -d
```
4. Your application will start on [localhost:8001](https://localhost:8001)


## Observations:
The chatbot has limited capabilities due to the short amount of context but it's accurate if the user gives the appropriate prompt.





