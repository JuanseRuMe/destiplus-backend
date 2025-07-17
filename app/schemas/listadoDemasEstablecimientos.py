from pydantic import BaseModel
from typing import Dict, Any, List, Optional, Union

class ItemBase(BaseModel):
   name: str
   img: str
   description: str 
   calificacion: float
   precio: Union[int, str]
   items: Dict[str, str]
   
class ItemResponse(ItemBase):
   logo: str
   fecha: Optional[str] = None
   equipamento: Optional[Dict[str, Any]]