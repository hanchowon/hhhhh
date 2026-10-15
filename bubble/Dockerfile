# 1. Base Image: Python 3.9 사용
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 종속성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
COPY . .

# 5. Cloud Run PORT 환경변수 기본값 설정
ENV PORT=8080

# 6. Uvicorn 실행 시 환경변수 $PORT를 사용하도록 변경 (exec 형태 사용)
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
