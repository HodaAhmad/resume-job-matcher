from fastapi import FastAPI

app = FastAPI(title="Resume Job Matcher")


@app.get("/")
def read_root():
    return {"message": "Resume Job Matcher API is running"}