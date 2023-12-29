from llama_index import StorageContext, load_index_from_storage
from langchain.chat_models import ChatOpenAI  # Import ChatOpenAI

# Initialize ChatOpenAI (assuming you have access to the API)
llm = ChatOpenAI(temperature=0, model="gpt-4")

# Load knowledge base
index = load_index_from_storage(StorageContext.from_defaults(persist_dir="storage"))
query_engine = index.as_query_engine()

def get_mental_model(query):
    # Construct a prompt to ask ChatGPT for the best mental model for the query
    prompt = f"What is the best mental model to apply to this question: '{query}'?"
    model_suggestion = llm.query(prompt)  # Send the query to ChatGPT
    return model_suggestion.strip()

def answer_question(query):
    # Get the suggested mental model from ChatGPT
    mental_model = get_mental_model(query)

    # Run the query on the query engine, including the mental model in the query
    modified_query = f"{mental_model}: {query}"
    response = query_engine.query(modified_query)

    # Structure the response
    structured_response = f"Answer using {mental_model}: {response}"
    return structured_response

def answer_questions():
    while True:
        query = input("Ask a question: ")
        if query.lower() == "quit":
            break
        response = answer_question(query)
        print(response)
