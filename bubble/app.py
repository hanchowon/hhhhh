from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SortingRequest(BaseModel):
    numbers: List[int]

def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ✅ 1. Cloud Run 헬스체크용 루트 경로 추가 (필수)
@app.get("/")
async def health_check():
    return {"status": "ok", "message": "Bubble Sort API Service Running"}

# 2. 정렬 요청 엔드포인트
@app.post("/sort/bubble")
async def handle_sorting_request(request_data: SortingRequest):
    try:
        original_array = request_data.numbers
        if not original_array:
            raise HTTPException(status_code=400, detail="숫자 배열을 입력해주세요.")

        sorted_array = bubble_sort(list(original_array))

        return {
            "status": "success",
            "original_array": original_array,
            "sorted_array": sorted_array,
            "message": "버블 정렬을 완료했습니다."
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    import os
    # Cloud Run에서 동적으로 할당하는 PORT 환경 변수 수신
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
