import time
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(
    api_key="YOUR-API-KEY"
)

# Get python object reference to Index
index = pc.Index("my-index")

# Query the pinecone index passing a query vector
results = index.query(
    vector=[0.1, 0.11, 0.11],
    top_k=1,
    include_values=True
)

# Print the results from fetch operation
print( results )