import openpyxl
from reportlab.pdfgen import canvas
from io import BytesIO

def create_pdf(data):
    buffer = BytesIO()

    # Create the PDF object, using BytesIO as its "file."
    p = canvas.Canvas(buffer)

    # Insert the header
    p.drawString(100, 800, 'Name')
    p.drawString(200, 800, 'Age')
    p.drawString(300, 800, 'City')

    y_position = 750  # Initial Y position for the first row of data

    for row in data:
        y_position -= 20  # Adjust vertical position for the next row
        p.drawString(100, y_position, str(row[0]))  # Name
        p.drawString(200, y_position, str(row[1]))  # Age
        p.drawString(300, y_position, str(row[2]))  # City

    # Close the PDF object cleanly and we're done.
    p.showPage()
    p.save()

    # File buffer rewind
    buffer.seek(0)
    return buffer

# Specify the Excel file path
excel_file_path = 'Book1.xlsx'  # Provide the correct Excel file path

# Load the Excel file
wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

# Convert Excel data to a list of lists
data = []
for row in sheet.iter_rows(values_only=True):
    data.append(list(row))

# Remove the header if present (assuming it's in the first row)
if data and data[0] == ['Name', 'Age', 'City']:
    data = data[1:]

# Generate the PDF
pdf_buffer = create_pdf(data)

# Write the PDF to a file
with open('pdf\output.pdf', 'wb') as f:
    f.write(pdf_buffer.read())