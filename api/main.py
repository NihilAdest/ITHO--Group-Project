import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.routers import index as indexRoute
from api.models import model_loader
from api.dependencies.config import conf

from api.routers.promotions import router as promotion_router
from api.routers.recipes import router as recipe_router
from api.routers.resources import router as resource_router
from api.routers.restaurant import router as restaurant_router
from api.routers.resource_management import router as resource_management_router
from api.routers.menu_item import router as menu_item_router

app = FastAPI()

origins = ["*"]

app.include_router(promotion_router)
app.include_router(recipe_router)
app.include_router(resource_router)
app.include_router(restaurant_router)
app.include_router(resource_management_router)
app.include_router(menu_item_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)