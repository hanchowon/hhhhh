FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cloud Run 기본 포트
ENV PORT=8080

# sh -c를 explicit하게 배열 형태로 지정
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
