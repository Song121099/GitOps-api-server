import uvicorn  # uvicorn을 임포트하여 서버 실행

if __name__ == "__main__":  # 스크립트가 직접 실행될 때만 실행
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)  
    # FastAPI 앱을 8000번 포트에서 실행, 코드 변경 시 자동 재시작

