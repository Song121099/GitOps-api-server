from pydantic import BaseModel #pydantic 모듈에서 BaseModel을 임포트

class Item(BaseModel): #Item의 클래스 정의. BaseModel 상속
    id: int            #정수형 속성
    name: str          #문자열
    price: int
