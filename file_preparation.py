import PyPDF2


def extract_text_from_pdf(pdf_path, output_path):
    """Extracts text from a PDF and saves it to a .txt file."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

    print(f"Text extracted and saved to {output_path}")


pdf_path = "2023_10_01_RS_ENG.pdf"
output_path = "../regulamin_agh.txt"

extract_text_from_pdf(pdf_path, output_path)