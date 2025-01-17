from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    return{
        "message": "Hello World!"
    }


# this is for testing of pull request

