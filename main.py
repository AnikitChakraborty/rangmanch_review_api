from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    """LIFESPAN EVENT HANDLER FOR FASTAPI APPLICATION."""
# Its gives control to the application to run startup code before the application starts serving requests. 
# All the code before the yield statement will be executed before the application starts serving requests,
# and all the code after the yield statement will be executed when the application is shutting down.
    
    create_tables()  # Create tables when the application starts
    print ("Tables created successfully.")
    yield  
    print ("Application is shutting down. Cleanup can be done here if needed.")
    # Control is returned to the application
    # Any cleanup code can be added here if needed

app = FastAPI(  
    title="Rangmanch Review API", 
    description="An API for managing reviews of plays in Rangmanch",
    version="1.0.0",
    lifespan = lifespan 
)

@app.get("/")
def root():
    """ROOT ENDPOINT TO CHECK IF THE API IS RUNNING."""
    return {"message": "Welcome to the Rangmanch Review API!"}