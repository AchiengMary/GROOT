import pinecone
from sentence_transformers import SentenceTransformer

pinecone.init(api_key="Ysk-abcdef1234567890abcdef1234567890abcdef12", environment="gcp-starter")
index = pinecone.Index("ovarian-cyst-index")
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def query_pinecone(question: str):
    query_vec = embed_model.encode(question).tolist()
    res = index.query(vector=query_vec, top_k=1, include_metadata=True)
    if res.matches:
        return res.matches[0].metadata.get("text", "No relevant answer found.")
    return "No match found."
