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
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))  # Works with Render's PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
