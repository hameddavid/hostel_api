from api.endpoints.endpoint_helper import  get_current_user
from sqlalchemy.ext.asyncio import async_sessionmaker
from fastapi.responses import JSONResponse
from dependencies import get_session
from fastapi import APIRouter,Depends
from typing import List
from schemas.userSchema import ReturnSignUpUser
from services import admin_service 

router = APIRouter()

@router.post("/allocate_room_to_student_in_session",response_model="")
async def allocate_room_to_student_in_session_func(mat_no:str, session_id:str, session: async_sessionmaker = Depends(get_session), user: ReturnSignUpUser =Depends(get_current_user)):
#   get student profile such as gender...
  gender = 'M'
  res = await admin_service.random_assign_room_to_student_in_session_service(mat_no,gender,session)
  if not res[0]:
    return JSONResponse(status_code=404, content={"message": res[1]})  
  elif res[0]:
    return res[1]


@router.post("/get_student_room__in_session",response_model="")
async def get_student_room_in_session_func(mat_no:str, session_id:str, session: async_sessionmaker = Depends(get_session), user: ReturnSignUpUser =Depends(get_current_user)):
  res = await admin_service.get_student_room_in_session_service(mat_no, session_id,session)
  if not res[0]:
    return JSONResponse(status_code=404, content={"message": res[1]}) 
  elif res[0]:
    return res[1]