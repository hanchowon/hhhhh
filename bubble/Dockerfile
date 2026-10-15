# 1. Base Image: Python 3.9 사용
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 종속성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
COPY . .

# 5. 실행 포트 노출
EXPOSE 8080

# 6. Uvicorn 서버 실행 명령 (Cloud Run은 이 명령을 사용하여 컨테이너를 시작)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
