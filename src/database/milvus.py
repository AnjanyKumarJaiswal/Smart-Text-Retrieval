from pymilvus import connections, utility, FieldSchema, CollectionSchema, DataType, Collection

def connect_milvus():
    connections.connect("default", host="localhost", port="19530")

    fields = [
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
        FieldSchema(name="summary", dtype=DataType.STRING),
        FieldSchema(name="book_title", dtype=DataType.STRING),
        FieldSchema(name="page_number", dtype=DataType.INT64)
    ]

    schema = CollectionSchema(fields, "RAPTOR index for textbook summaries")

    collection_name = "raptor_index"
    if utility.has_collection(collection_name):
        collection = Collection(collection_name)
    else:
        collection = Collection(name=collection_name, schema=schema)
    return collection

def insert_data(collection, summaries, embeddings, book_title, page_numbers):
    data = [
        embeddings,
        summaries,
        [book_title] * len(summaries),
        page_numbers
    ]
    collection.insert(data)

def create_index(collection):
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128}
    }
    collection.create_index(field_name="embedding", index_params=index_params)
    collection.load()
