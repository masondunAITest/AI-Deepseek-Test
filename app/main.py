from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from model import ValuationModel
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

model = ValuationModel()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/valuate")
async def valuate(
    request: Request,
    years: int = Form(...),
    employees: int = Form(...),
    revenue: float = Form(...)
):
    valuation = model.predict(years, employees, revenue)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "valuation": f"${valuation:,.2f}",
        "years": years,
        "employees": employees,
        "revenue": revenue
    })
