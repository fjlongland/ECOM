from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from .routers import user_router, post_router, images_router
from database import dbModels as models
from database.database import engine
 


models.Base.metadata.create_all(bind=engine)

#starts the app
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

#this handles middleware support.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

#add favicon because browser wants this for some reason.
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

#Test endpoint for when deploying in a new environment.
@app.get("/")
def root():
    return {"Hello": "traveler!"}


#add all the different endpointv routersto the application
app.include_router(user_router.router)
app.include_router(post_router.router)
app.include_router(images_router.router)





