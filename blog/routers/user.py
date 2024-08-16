from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from passlib.context import CryptContext
from ..repository import user


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.get_user(id, db)



@router.post('/', response_model=schemas.ShowUser,  status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)
