from fpdf import FPDF
import os

def generate_itinerary_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()

    font_path = os.path.join( "fonts", "DejaVuSans.ttf")
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    # Split the text into lines and add them to the PDF
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)

    # Save the PDF to the specified filename
    pdf.output(filename)
    return filename

