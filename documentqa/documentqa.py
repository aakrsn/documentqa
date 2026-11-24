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
def chunk_text(text, chunk_size=10, overlap=2):
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
print(chunks)
print("**********************")
print("Number of chunks:", len(chunks))










from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

embeddings = model.encode(
    chunks,
    normalize_embeddings=True
)

print("******************************")
print("Number of embeddings:", len(embeddings))