from core.docx_loader import extract_text_from_docx


docx_path = "data/sample_notes.docx"

paragraphs = extract_text_from_docx(docx_path)

print("Number of paragraphs extracted:", len(paragraphs))

print("\nFirst paragraph:")
print(paragraphs[0])

print("\nType of paragraphs:", type(paragraphs))
print("Type of first paragraph:", type(paragraphs[0]))