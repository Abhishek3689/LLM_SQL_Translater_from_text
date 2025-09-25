## Text-to-SQL with RAG

### Project Overview
This project implements a Text-to-SQL system using Retrieval-Augmented Generation (RAG) to translate natural language queries into executable SQL queries. The system leverages RAG to enhance the accuracy of SQL generation by retrieving relevant context (e.g., database schema, example queries) and combining it with a generative model to produce precise SQL statements. This is particularly useful for enabling non-technical users to interact with databases using natural language.
Key Features.
- Natural Language Processing: Converts user questions (e.g., "show me the highest 'Line Total' by customer" ) into valid SQL queries.
- RAG Integration: Uses retrieval mechanisms to fetch relevant schema information or example queries, improving query accuracy.
- Database Compatibility: Works with common SQL databases (e.g. MySQL).


### Technologies Used

Python: Core programming language for implementing the RAG pipeline.
RAG Framework: Combines retrieval (e.g., FAISS, Elasticsearch) with a generative model (e.g., LLaMA, BERT-based model, or Hugging Face Transformers).
Amazon ECR: Storing and managing Docker images.
SQL Database: MySQL for testing and executing generated queries.




Setup Instructions
Prerequisites

AWS account with EC2 and ECR access
Docker installed on your local machine or EC2 instance
Python 3.8+
A SQL database (e.g., PostgreSQL, MySQL) for testing
AWS CLI configured with appropriate credentials

Installation

Clone the Repository
git clone https://github.com/your-username/text-to-sql-rag.git
cd text-to-sql-rag


Set Up Python Environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Configure Database

Set up a local or remote SQL database (e.g., PostgreSQL).
Update database credentials in app/db_connect.py:DATABASE_URL = "postgresql://username:password@localhost:5432/your_db"




Set Up AWS EC2

Launch an EC2 instance (e.g., t3.medium, Ubuntu 20.04).
Configure security groups to allow:
SSH (port 22)
HTTP/HTTPS (ports 80/443) for API access
Database port (e.g., 5432 for PostgreSQL)


SSH into the instance:ssh -i your-key.pem ubuntu@ec2-public-ip




Install Docker on EC2
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker


Set Up Amazon ECR

Create a repository in AWS ECR:aws ecr create-repository --repository-name text-to-sql-rag


Authenticate Docker to ECR:aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com




Build and Push Docker Image

Build the Docker image locally:docker build -t text-to-sql-rag .


Tag and push to ECR:docker tag text-to-sql-rag:latest your-account-id.dkr.ecr.your-region.amazonaws.com/text-to-sql-rag:latest
docker push your-account-id.dkr.ecr.your-region.amazonaws.com/text-to-sql-rag:latest




Deploy on EC2

Pull the image from ECR on the EC2 instance:docker pull your-account-id.dkr.ecr.your-region.amazonaws.com/text-to-sql-rag:latest


Run the container, exposing the application port (e.g., 8000):docker run -d -p 8000:8000 your-account-id.dkr.ecr.your-region.amazonaws.com/text-to-sql-rag:latest





Usage

Start the Application

If running locally, use:python app/rag_pipeline.py


If deployed on EC2, the Docker container should already be running.


Interact with the API

Send a natural language query to the API endpoint (e.g., http://ec2-public-ip:8000/query):curl -X POST -H "Content-Type: application/json" -d '{"query": "Show all employees with salary above 50000"}' http://ec2-public-ip:8000/query


Response example:{
  "sql_query": "SELECT * FROM employees WHERE salary > 50000;"
}




Test with a Database

The generated SQL query can be executed against the configured database to fetch results.



How It Works

Retrieval (RAG):

The retriever (e.g., FAISS) searches a pre-indexed corpus of database schema metadata and example SQL queries.
Relevant context (e.g., table/column names, sample queries) is retrieved based on the input natural language query.


Generation:

The retrieved context is fed into a generative model (e.g., fine-tuned T5 or LLaMA) to produce an SQL query.
The model ensures the query is syntactically correct and aligned with the database schema.


Execution:

The generated SQL query is validated and can be executed against the target database using sqlalchemy.


