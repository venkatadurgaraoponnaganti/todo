FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

# pip already included — no need to apt install python3-pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

