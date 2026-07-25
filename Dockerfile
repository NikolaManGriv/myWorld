FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

COPY . .

RUN mkdir -p /dbdata && ln -s /dbdata/base1.duckdb /app/base1.duckdb

CMD ["streamlit", "run", "interface.py", "--server.port=8501", "--server.address=0.0.0.0"]
