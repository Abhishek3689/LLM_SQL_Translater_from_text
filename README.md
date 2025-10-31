## Text-to-SQL with RAG

### Project Overview
This project implements a Text-to-SQL system using Retrieval-Augmented Generation (RAG) to translate natural language queries into executable SQL queries. The system leverages RAG to enhance the accuracy of SQL generation by retrieving relevant context (e.g., database schema, example queries) and combining it with a generative model to produce precise SQL statements. This is particularly useful for enabling non-technical users to interact with databases using natural language.
Key Features.
- Natural Language Processing: Converts user questions (e.g., "show me the highest 'Line Total' by customer" ) into valid SQL queries.
- RAG Integration: Uses retrieval mechanisms to fetch relevant schema information or example queries, improving query accuracy.
- Database Compatibility: Works with common SQL databases (e.g. MySQL).


### Technologies Used

Python: Core programming language for implementing the RAG pipeline.
RAG Framework: Combines retrieval  with a generative model (e.g., LLaMA, BERT-based model, or Hugging Face Transformers).
LangChain: Framework for building the RAG pipeline with prompt templates and LLM integration.
SQL Database: MySQL for testing and executing generated queries.
Libraries: pymysql, langchain, langchain-community, langchain-groq.




### Setup Instructions

**Prerequisites**
- Python 3.9 or higher
- MySQL server installed locally or remotely
- A MySQL database (e.g., text_to_sql) with tables for testing
- API key for GroQ (Groq cloud) for LLM access

pip for installing Python dependencies
Installation

Clone the Repository
git clone https://github.com/Abhishek3689/LLM_SQL_Translater_from_text.git
cd Text_to_SQL


Set Up Python Environment
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt


