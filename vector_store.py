import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

INDEX_NAME = "garagemate-ai"

def create_index_if_not_exists():
    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=INDEX_NAME,
            dimension=1536,  # Assuming 1536 dimensions for the embeddings
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-west-2'  # Replace with your preferred region
            )
        )

def upsert_vectors(vectors):
    index = pc.Index(INDEX_NAME)
    index.upsert(vectors=vectors)

def query_vectors(query_vector, top_k=5):
    index = pc.Index(INDEX_NAME)
    results = index.query(vector=query_vector, top_k=top_k)
    return results

def delete_vectors(ids):
    index = pc.Index(INDEX_NAME)
    index.delete(ids=ids)