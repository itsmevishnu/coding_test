from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fpdf import FPDF
from datetime import datetime



#pydantic model class
class PdfInputValues(BaseModel):
    name: str
    address: str
    favourite_activities: list
    favourite_activity: str

# Controller class
class GeneratePdf:
    def genereate_pdf(values: PdfInputValues):
        file_name = f"{values.name}.pdf"
        activities = ",".join(values.favourite_activities)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(w=75, h=10, txt=f"Name: {values.name}", border=1, ln=0)
        pdf.cell(w=100, h=10, txt=f"Date: {str(datetime.now())}", border=1, ln=1)
        pdf.cell(w=175, h=10, txt=f"Address: {values.address}", border=1, ln=1)
        pdf.cell(w=175, h=10, txt=f"What are your favourite activities? : {activities}", border=1, ln=2)
        pdf.cell(w=175, h=10, txt=f"What is your favourite activity? : {values.favourite_activity}", border=1, ln=2)
        pdf.output(file_name, 'F')
        
        return FileResponse(file_name)

app = FastAPI()

@app.get("/", summary="Sample")
def home_page():
    return {"message": "App is Working"}

@app.post("/generate-pdf", summary="Generate the pdf", status_code=201)
def generate_pdf(input_values: PdfInputValues):
    return GeneratePdf.genereate_pdf(values=input_values)