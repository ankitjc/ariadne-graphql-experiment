from ariadne import QueryType

query = QueryType()

# Resolver for hello
@query.field("hello")
def resolve_hello(_, info):
    return "Hello from Ariadne!"

# Resolver for books
@query.field("books")
def resolve_books(_, info):
    return [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Brave New World", "author": "Aldous Huxley"},
        {"title": "Fahrenheit 451", "author": "Ray Bradbury"},
    ]

@query.field("conversations")
def resolve_conversations(_, info):
    return [
        {"text": "I'm doing good", "model": "llama3.0", "provider": "bedrock", "emoji" : "2"},
        {"text": "Its a beautiful day", "model": "gpt4.0", "provider": "openAI", "emoji" : "10"},
        {"text": "Lets do it", "model": "amazon1.0", "provider": "bedrock", "emoji" : "100"},
    ]

