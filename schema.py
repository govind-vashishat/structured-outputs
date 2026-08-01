from pydantic import BaseModel

class LineItem(BaseModel):
    name: str
    price: float

class Invoice(BaseModel):
    invoice_number: str
    seller: str 
    issue_date: str
    items: list[LineItem]
    subtotal: float
    tax: float
    total: float
    due_date: str