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
