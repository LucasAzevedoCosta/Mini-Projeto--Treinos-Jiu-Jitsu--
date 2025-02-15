from ninja import NinjaAPI
from treino.api import treino_router

api = NinjaAPI()
api.add_router('', treino_router)