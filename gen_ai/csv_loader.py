import pandas as pd
import chromadb



def get_collection():
    # Initialize ChromaDB in-memory instance
    chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Change path for persistence

    # Create a collection (will auto-use default embedding model)
    collection = chroma_client.get_or_create_collection(name="my_collection")

    # Load CSV file
    # df = pd.read_csv("D:\\Programs\\Web Python\\fast_api_learning\\customers-1000.csv", low_memory=False)  # Change to your file name

    # # Insert data into ChromaDB
    # for i, row in df.iterrows():
    #     collection.add(
    #         ids=[str(i)],  # Unique ID for each entry
    #         documents=[str(row.to_dict())],  # Convert row to string format
    #         metadatas=[row.to_dict()]  # Store metadata for filtering later
    #     )

    print("Data successfully loaded into ChromaDB!")
    return collection

# collection = get_collection()
# # Example: Perform a simple search
# results = collection.query(
#     query_texts=["d794Dd48988d2ac"],  # Replace with your actual query
#     n_results=5, where_document={"$contains":  "d794Dd48988d2ac"}
# )


# print(results)
