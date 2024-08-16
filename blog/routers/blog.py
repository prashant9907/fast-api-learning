from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import  schemas
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/')
def all(db: Session=Depends(get_db)):
    return blog.show_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session=Depends(get_db)):
    return blog.create(request, db)
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)
    



@router.get('/{id}', status_code=200)
def show(id: int, db:Session=Depends(get_db)):
    return blog.show(id, db)
    

# Update is not working for now we have resolve the error

# @app.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
# def update(id, request: schemas.Blog, db :Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} is not found")
    
#     blog.update(request)
#     db.commit()
#     return "updated"
