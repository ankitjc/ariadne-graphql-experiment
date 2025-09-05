from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from resolvers import query

# Load schema and create executable schema
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query)

# ASGI app exported directly — no need for asgi_adapter
app = GraphQL(schema, debug=True)
