import fitz  # PyMuPDF
import google.generativeai as genai

def extract_text_from_pdf(file):
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in pdf:
        text += page.get_text()
    return text

def summarize_pdf(file):
    text = extract_text_from_pdf(file)
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Summarize the following travel guide:\n{text[:8000]}"  # keep within context limit
    response = model.generate_content(prompt)
    return response.text
