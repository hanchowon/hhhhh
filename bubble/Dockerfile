FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cloud Run 기본 포트
ENV PORT=8080

# ⚠️ 배열 형태가 아닌 아래와 같이 문자열 형태로 작성해야 $PORT가 8080으로 제대로 치환됩니다.
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
