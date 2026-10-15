FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cloud Run의 PORT 환경변수 대응 (기본 8080)
ENV PORT=8080

# ✅ 환경 변수 $PORT를 직접 참조하도록 변경
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
