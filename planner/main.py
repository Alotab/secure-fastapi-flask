from fastapi import FastAPI
from routes.users import user_router
import uvicorn


#create a fastapi instance and register the route and the application
app = FastAPI()

app.include_router(user_router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main.app", host="0.0.0.0", port=8080, reload=True)