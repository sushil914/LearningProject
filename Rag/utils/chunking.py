from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_text(text)

"""
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def semantic_chunking(
    sentences,
    embeddings,
    similarity_threshold=0.75
):
    """
    Splits sentences into semantic chunks based on embedding similarity.

    Parameters:
        sentences (list[str]): List of sentences in document order
        embeddings (list[list[float]]): Sentence embeddings (same order)
        similarity_threshold (float): Threshold to start a new chunk

    Returns:
        list[str]: List of semantic chunks
    """

    chunks = []
    current_chunk = [sentences[0]]

    for i in range(1, len(sentences)):
        prev_emb = np.array(embeddings[i - 1]).reshape(1, -1)
        curr_emb = np.array(embeddings[i]).reshape(1, -1)

        similarity = cosine_similarity(prev_emb, curr_emb)[0][0]

        if similarity < similarity_threshold:
            # Meaning has shifted → start new chunk
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentences[i]]
        else:
            # Same topic → keep accumulating
            current_chunk.append(sentences[i])

    # Add last chunk
    chunks.append(" ".join(current_chunk))

    return chunks
"""

#Kubernetes is a container orchestration platform widely used in cloud native applications.
#It helps automate deployment, scaling and management of containers.

#chunk1 = Kubernetes is a container orchestration platform
#chunk2 = orchestration platform widely used in cloud native
#chunk3 = in cloud native applications.It helps automate


#first breakdown with Recursive text splitter and then apply the concept of slidng window

#Kubernetes is a container orchestration platform,

# widely used in cloud native applications.

#It helps automate deployment, scaling and management of containers.

