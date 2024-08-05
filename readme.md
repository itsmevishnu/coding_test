## Approach
1. Developed a pydantic model to read and validate the value through the body of the API
2. Created a simple class instance function to create pdf
3. Return the created pdf as `FileResponse` of Fastapi.(Use Postman for better output)
4. Used pep coding standards, and clean code approach by Robert C Martin

## Instruction to run
1. Install all required package mentioned in the `requirements.txt`
2. Run the app using uvicorn by `uvicorn main:app --reload`
3. Use `localhost:8000/docs` to see API documentation in swagger 

## Package used to develop this module
1. Fastapi -  Backend
2. Pydantic - For validation
3. Uvicon - To run the application
4. FPDF - To create pdf
5. datetime (In built) - To display time

## Tools used
1. Visual studio code - as code editor
2. Postman - To test API

## Disclaimer
- No AI tools such as chatGPT, code generators are used.
- Referred official documentaion of fastapi, fpdf(https://pyfpdf.readthedocs.io/en/latest/reference/cell/index.html)
