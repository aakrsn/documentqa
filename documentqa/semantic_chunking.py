
import nltk
import numpy as np
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer

nltk.download("punkt_tab")

# 1. Read document
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Sentence tokenization
sentences = sent_tokenize(text)

print("Number of sentences:", len(sentences))

if not sentences:
    raise ValueError("No sentences found in input.txt")

# 3. Generate embeddings
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

embeddings = model.encode(
    sentences,
    normalize_embeddings=True
)

print("Number of embeddings:", len(embeddings))

# 4. Calculate cosine similarity between consecutive sentences
# Since embeddings are normalized, dot product = cosine similarity

similarities = []

for i in range(len(embeddings) - 1):
    similarity = np.dot(embeddings[i], embeddings[i + 1])
    similarities.append(float(similarity))

    print(
        f"Sentence {i + 1} and {i + 2}: "
        f"{similarity:.4f}"
    )

# 5. Semantic chunking
threshold = 0.5  # Experiment with this value

chunks = []
current_chunk = [sentences[0]]

for i, similarity in enumerate(similarities):

    if similarity >= threshold:
        # Semantically related: same chunk
        current_chunk.append(sentences[i + 1])

    else:
        # Semantic shift: create new chunk
        chunks.append(" ".join(current_chunk))
        current_chunk = [sentences[i + 1]]

# Add final chunk
chunks.append(" ".join(current_chunk))

# 6. Display chunks
print("\nTotal chunks:", len(chunks))

for i, chunk in enumerate(chunks, 1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)
