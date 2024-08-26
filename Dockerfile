# 베이스 이미지로 Python을 사용
FROM python:3.9-slim

# 작업 디렉토리를 설정
WORKDIR /app

# requirements.txt 파일을 복사하고 필요 라이브러리 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 현재 디렉토리의 모든 파일을 작업 디렉토리에 복사
COPY . .

# FastAPI 서버를 실행하는 명령어
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

