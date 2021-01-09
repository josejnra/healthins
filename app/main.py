from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes import router


app = FastAPI()

app.include_router(router=router)


@app.get('/')
def index():
    return RedirectResponse(url='/redoc')
