# #core logic comes here


# # Take the input from the user and process it

# 1. Text File Input
with open("input.txt", "r") as f:
    text = f.read()

#print("Input Text:", text)


# # 2. Chunk the text into smaller pieces

# # learn about chunking and it's different staregies.
# #Chunking is the process of segmenting text into smaller, manageable portions based on length, structure or semantic meaning. It allows vector search to focus on precise information rather than entire documents


# # Fixed Size Chunking
# # Semantic Chunking (Every line in a chunk should be semantically related to each other, So cosine similarity btw each line is very similar.)
# # Document Structrure based Chunking (Chunking based on the structure of the document, like paragraphs, sections, headings, etc.)
# # Token based Chunking (Chunking based on the number of tokens, which is useful for models with token limits.)

# #a chunk is supposed to represent one meaningful unit of information
# #If the chunk is too small, you may split a concept across multiple chunks and lose the surrounding facts that explain it.


# # The best chunk size is not “smallest possible” or “largest possible.”
# # It is:

# # large enough to preserve a complete fact or topic
# # small enough to avoid mixing unrelated information
# # A good chunk usually contains:

# # one idea,
# # one paragraph or section,
# # or a few related sentences with overlap

# Fixed Size Chunking
def chunk_text(text, chunk_size=500, overlap=50):
    """ Chunk the input text into smaller pieces of specified size. """
    chunks = []
    for i in range(0, len(text), chunk_size):
        #print(i)
        #print(text[i])
        start = i-overlap if i-overlap>=0 else i
        end = i+chunk_size
        chunks.append(text[start:end])
    return chunks

# text = "#If the chunk is too small, you may split a concept across multiple chunks and lose the surrounding facts that explain it."
chunks = chunk_text(text)
#print(chunks)
print("**********************")
print("Number of chunks:", len(chunks))
print("Lenght of 1st chunks: ", len(chunks[0]))










from sentence_transformers import CrossEncoder, SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
     local_files_only=True
)

embeddings = model.encode(
    chunks,
    normalize_embeddings=True,
    show_progress_bar=True
)

print("******************************")
print("Number of embeddings:", len(embeddings))
print("type of the member in embeddings:", type(embeddings[0]))
print(len(embeddings[0])) # 384, 384 dimension, the respective chunk is scaterred around 384 dimensions. 

# the coloum in which we are storing the embeddings, the dimension of that column should be same as the dimensions produced by the model.

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ragapp",
    user="ajaykrishna22",
    password=""
)

cursor = conn.cursor()

# cursor.execute("SELECT * FROM documents;")

# records = cursor.fetchall()

# print(type(records))

# print(records)
# print("******************************")

# ----------------------- Insert Query ------------------------
# query = """
#     INSERT INTO documents (workspace_id, body, embedding)
#     VALUES (%s, %s, %s::vector);
# """
#---------------------------------------------------------------

#-----------------------Update Query ---------------------------
# query = """
#     Update documents set body = %s, embedding = %s::vector where id = %s
# """
# #---------------------------------------------------------------
# workspace_id = 1

# chunk_id = 1
# for chunk, embedding in zip(chunks, embeddings, strict=True):
#     values = (chunk, embedding.tolist(), chunk_id)
#     cursor.execute(query, values)
#     conn.commit()
#     chunk_id = chunk_id + 1

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM documents;")

# records = cursor.fetchall()

# print(type(records))

# print(records)

# conn.close()


query = "What is the key reason behind our dreams?"

# convert query into embeddings

import json
import numpy as np

queries = []
queries.append(query)
query_embeddings = model.encode(
    queries,
    normalize_embeddings=True,
    show_progress_bar=True
)

cursor.execute("""
    SELECT id, body, embedding
    FROM documents
    WHERE embedding IS NOT NULL AND body IS NOT NULL
""")

records = cursor.fetchall()
cursor.close()
conn.close()

similarity_scores = []

for _, _, embedding_values in records:
    embedding_record = np.asarray(json.loads(embedding_values), dtype=np.float32)
    similarity_score = np.dot(embedding_record, query_embeddings[0])
    similarity_scores.append(similarity_score)

top_k = 20
nearest_indices = np.argsort(similarity_scores)[::-1][:top_k]

if nearest_indices.size:
    # The cross-encoder scores the query against each candidate's original text.
    reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
    pairs = [(query, records[index][1]) for index in nearest_indices]
    relevance_scores = reranker.predict(pairs)

    final_k = 5
    reranked_positions = np.argsort(-relevance_scores, kind="stable")[:final_k]
    for rank, position in enumerate(reranked_positions, start=1):
        index = nearest_indices[position]
        chunk_id, chunk, _ = records[index]
        print(f"\nRank {rank} | Chunk ID {chunk_id}")
        print(f"Relevance: {relevance_scores[position]:.4f}")
        print(f"Embedding similarity: {similarity_scores[index]:.4f}")
        print(chunk)
else:
    print("No chunks found to rerank.")
