from pydantic import BaseModel
from typing import Optional


class City(BaseModel):
    """Модель города"""
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    Area: Optional[str] = None


class Warehouse(BaseModel):
    """Модель отделения"""
    SiteKey: int
    Description: str
    DescriptionRu: Optional[str] = None
    Number: str
    CityRef: str
    TypeOfWarehouse: Optional[str] = None


class Street(BaseModel):
    """Модель улицы"""
    Ref: str
    Description: str
    StreetsTypeRef: str
    StreetsType: str


class Area(BaseModel):
    """Модель области"""
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None


class Settlement(BaseModel):
    """Модель населённого пункта"""
    Ref: str
    Description: str
    DescriptionRu: Optional[str] = None
    AreaRef: str
    Type: str
