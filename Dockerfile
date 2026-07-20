FROM python:3.12

# Copiar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY requirements.txt .

# Ahora pasará sin errores porque la imagen ya tiene zlib
RUN uv pip install --system --no-cache -r requirements.txt

COPY . .

CMD ["python", "add_app.py"]
