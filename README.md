📚 Media Library API (FastAPI)

A simple yet extensible Media Library Management API built with FastAPI.
This project demonstrates how to design, build, and test a REST API in Python, with a focus on clean architecture, persistence, and future extensibility.

🚀 Features

Manage Movies and Series (add, update, delete, list).

Search media by title or filter by genre.

Get top-rated items dynamically.

JSON persistence to store data across runs.

Unit tests for both core classes and API endpoints.

Built with FastAPI for high performance and interactive docs (/docs).

🛠 Tech Stack

Python 3.10+

FastAPI – for building APIs

Pydantic – for request validation

Pytest – for testing

Uvicorn – for running the app

📂 Project Structure
python_fastapi_project/
│── api.py # FastAPI entry point
│── library.py # Library management logic
│── movie.py # Movie model
│── series.py # Series model
│── media.py # Base media model
│── mediabase.py # Pydantic schemas
│── tests/ # Unit & API tests
│── library.json # Persistent storage (auto-created)

▶️ Getting Started

1. Clone the repo
   git clone git@github.com:pranjal-lakhotia/python_fastapi_project.git
   cd python_fastapi_project

2. Create & activate virtual environment
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Run the app
   uvicorn api:app --reload

Visit: http://127.0.0.1:8000/docs
for interactive Swagger UI.

✅ Testing

Run all tests using:

pytest -v

📦 Roadmap / Next Steps

Add database integration (SQLite/Postgres).

Build analytics layer using Pandas/Numpy.

Dockerize the app.

Set up CI/CD pipeline.

🤝 Contributing

Pull requests and ideas are welcome! Feel free to open issues for feature requests or bug reports.

📜 License

This project is licensed under the MIT License.
