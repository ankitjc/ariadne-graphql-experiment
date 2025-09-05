# 🚀 Ariadne GraphQL API on Vercel

This project is a simple GraphQL API built with [Ariadne](https://ariadnegraphql.org/) and deployed as a serverless function on [Vercel](https://vercel.com/). 
It demonstrates a schema-first approach to GraphQL using Python.

---

## 📦 Features

- GraphQL API with:
  - `hello`: returns a greeting string
  - `books`: returns a static list of books
  - `conversations`: returns a static list of conversations, models, providers etc
- Serverless deployment on Vercel (no backend server needed)
- ASGI-ready using Ariadne's built-in `GraphQL` class

---

## 🧱 Project Structure
```
ariadne-hackathon/
├── api/
│ └── graphql.py # Entry point for Vercel (exports ASGI app)
├── resolvers.py # Query resolvers
├── schema.graphql # GraphQL SDL schema
├── requirements.txt # Python dependencies
└── vercel.json # Vercel configuration
```


##  Getting Started Locally

### 1. Clone the repo

```bash
git clone https://github.com/ankitjc/ariadne-graphql-experiment.git
cd ariadne-graphql-experiment
```
### 2. Create virtual environment (OPTIONAL)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt 

// or use pip3 if using mac 

pip3 install -r requirements.txt
```

### 4. Run locally with Uvicorn
```bash
pip3 install uvicorn

uvicorn api.graphql:app --reload
```

Then open http://localhost:8000 and run GraphQL queries in the playground.


## 🔗 Sample GraphQL Queries

```
query {
  conversations {
    text
    provider
    model
    emoji
  }
}
```

```
query {
  books {
    title
    author
  }
}
```

```
query {
  hello
}
```