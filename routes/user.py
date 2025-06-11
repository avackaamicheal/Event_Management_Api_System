from fastapi import APIRouter, HTTPException, status
from schemas.user import UserCreate, User, UserUpdate
from crud.user import user_crud


user_router = APIRouter()


@user_router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    try:
         new_user = user_crud.create_user(user_data)
         return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/", response_model= list[User], status_code=status.HTTP_200_OK)
def get_all_users():
    user = user_crud.get_all_users()
    return user


@user_router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int):
    return user_crud.get_user_by_id(user_id)


@user_router.put("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def update_user(user_id:int, user_data:UserUpdate):
    try:
        updated_user = user_crud.update_user(user_id, user_data)
        return updated_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@user_router.delete("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def delete_user(user_id:int):
    try:
        user_crud.delete_user(user_id)

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@user_router.patch("/{user.id}/deactivate", response_model=User, status_code=status.HTTP_202_ACCEPTED)
def deactivate_user(user_id:int):
    try:
        user = user_crud.deactivate_user(user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=(e))