from fastapi import FastAPI, HTTPException  # FastAPI와 HTTPException 임포트
from typing import List  # List 타입 임포트
from app.models import Item  # Item 모델 임포트

app = FastAPI()  # FastAPI 앱 생성

# 데이터베이스 시뮬레이션 (임시 데이터)
items = [
    Item(id=1, name="apple", price=1000),
    Item(id=2, name="banana", price=1500),
    Item(id=3, name="orange", price=2000)
]

@app.get("/api/hello")  # 단순 인사 메시지 반환
def read_hello():
    return "Hello, World!"

@app.get("/api/items", response_model=List[Item])  # 모든 아이템 반환
def read_items():
    return items

@app.get("/api/items/{item_id}", response_model=Item)  # 특정 아이템 반환
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/api/items", response_model=Item, status_code=201)  # 새로운 아이템 생성
def create_item(item: Item):
    items.append(item)
    return item

@app.put("/api/items/{item_id}", response_model=Item)  # 기존 아이템 수정
def update_item(item_id: int, updated_item: Item):
    for i in range(len(items)):
        if items[i].id == item_id:
            items[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/api/items/{item_id}", status_code=200)  # 아이템 삭제
def delete_item(item_id: int):
    for i in range(len(items)):
        if items[i].id == item_id:
            del items[i]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

