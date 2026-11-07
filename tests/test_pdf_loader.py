from core.pdf_loader import extract_text_from_pdf


pdf_path = "data/sample_notes.pdf"

pages = extract_text_from_pdf(pdf_path)

print("Type of pages:", type(pages))
print("Number of pages:", len(pages))

print("\nFirst page data:")
print(pages[0])

print("\nType of first page:", type(pages[0]))