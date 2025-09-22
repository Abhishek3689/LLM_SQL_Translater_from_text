import os
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_core.runnables import RunnablePassthrough
from sql_connector import connect_to_database
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_schema(db):
    return db.get_table_info()
## connect mysql database
host="localhost"
username="root"
password="root"
database="text_to_sql"

mysql_url=f"mysql+pymysql://{username}:{password}@{host}/{database}"
db=SQLDatabase.from_uri(mysql_url,sample_rows_in_table_info=0 )
print(db.get_table_info())



llm=ChatGroq(model="openai/gpt-oss-20b",max_tokens=512)

parser=StrOutputParser()

template=""""Based on the Table Schema as below. write an sql query based on input given by user as question.if it seems inormation is unavailable in the schema, then return 'SELECT NULL'.
Remember: Give SQL query only based on .
Schema:{schema}
Question:{question}
SQL Query:"""
prompt=PromptTemplate(template=template, input_variables=["schema","question"])
## create sql chain
sql_chain=RunnablePassthrough.assign(schema=lambda _:get_schema(db)) | prompt | llm | parser

result=sql_chain.invoke({'question':"what is the customer name which has highest number of  ordered quantity"})
print(result)