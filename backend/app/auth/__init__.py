from fastapi import APIRouter

auth_router = APIRouter()

from . import views # noqa
