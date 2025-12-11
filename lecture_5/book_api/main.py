from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database import SessionLocal, engine, Base
from models import Book as BookModel
from pydantic import BaseModel

app = FastAPI()

# Создать таблицы, если ещё нет
Base.metadata.create_all(bind=engine)

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /books/ - adding the book
@app.post("/books/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookModel(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


# GET /books/ - get all books
@app.get("/books/", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()


# DELETE /books/{id} - delete book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}


# PUT /books/{id} - update book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in book_data.dict().items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


# GET /books/search/ - find the book by name, author name or year
@app.get("/books/search/", response_model=List[Book])
def search_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(BookModel)

    if title:
        query = query.filter(BookModel.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(BookModel.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(BookModel.year == year)

    return query.all()