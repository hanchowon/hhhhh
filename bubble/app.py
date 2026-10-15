"""
Google Cloud Run에 배포될 버블 정렬 백엔드 서버 (main.py)

이 스크립트는 FastAPI를 사용하여 HTTP 엔드포인트를 제공하며,
요청받은 숫자 배열에 대해 버블 정렬을 수행합니다.

사용자는 [숫자1, 숫자2, ...] 형태의 JSON 배열을 POST 요청으로 보냅니다.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 1. 데이터 모델 정의
class SortingRequest(BaseModel):
    """
    클라이언트로부터 받을 요청 데이터의 형식을 정의하는 Pydantic 모델입니다.
    numbers: 정렬할 숫자들의 리스트 (예: [5, 1, 4, 2, 8])
    """
    numbers: List[int]

# 2. 버블 정렬 함수 구현
def bubble_sort(arr: List[int]) -> List[int]:
    """
    버블 정렬 알고리즘을 수행하고 정렬된 배열을 반환합니다.
    (단계별 기록 기능은 포함하지 않고 정렬만 수행)
    """
    n = len(arr)
    # n-1번 반복
    for i in range(n):
        # 이미 정렬된 n-1-i개는 건너뜀
        for j in range(0, n - 1 - i):
            # 인접한 두 원소를 비교
            if arr[j] > arr[j + 1]:
                # 앞의 원소가 더 크면 교환 (Swap)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 3. HTTP 엔드포인트 정의
@app.post("/sort/bubble")
async def handle_sorting_request(request_data: SortingRequest):
    """
    /sort/bubble 엔드포인트에 대한 POST 요청을 처리합니다.
    """
    try:
        # 입력 데이터 검증 및 복사
        original_array = request_data.numbers
        if not original_array:
            raise HTTPException(status_code=400, detail="숫자 배열을 입력해주세요.")

        # 복사본을 정렬 (원본 유지)
        sorted_array = bubble_sort(list(original_array))

        # 결과 반환 (JSON 형식)
        return {
            "status": "success",
            "original_array": original_array,
            "sorted_array": sorted_array,
            "message": "버블 정렬을 완료했습니다."
        }

    except Exception as e:
        # 오류 발생 시 상세 내용 반환
        raise HTTPException(status_code=500, detail=str(e))

# 서버 실행 (uvicorn)
if __name__ == "__main__":
    import uvicorn
    # 0.0.0.0으로 바인딩하여 외부 접근 허용, Cloud Run 포트 사용
    uvicorn.run(app, host="0.0.0.0", port=8080)
