"""Render G6 BRO PDFs to PNGs for visual reading.

pdftotext mangles many of these PDFs because of embedded fonts. Render to
images so we can see the Содржини directly.
"""
import fitz
import os
import sys

SRC = r"C:\Users\User\OneDrive\Desktop\Super zvezda\6to oddelenie BRO"
OUT = r"C:\Users\User\super-dzvedza\audit_g6_png"

os.makedirs(OUT, exist_ok=True)

# Render only the requested subject if argument given
subject = sys.argv[1] if len(sys.argv) > 1 else None

pdfs = sorted([f for f in os.listdir(SRC) if f.endswith('.pdf')])
for pdf in pdfs:
    if subject and subject.lower() not in pdf.lower():
        continue
    base = pdf.replace('.pdf', '').replace(' ', '_')
    src_path = os.path.join(SRC, pdf)
    print(f'Rendering: {pdf}')
    doc = fitz.open(src_path)
    n = len(doc)
    for i, page in enumerate(doc):
        mat = fitz.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat)
        out_path = os.path.join(OUT, f'{base}_p{i+1:02d}.png')
        pix.save(out_path)
    doc.close()
    print(f'  -> {n} pages saved')

print('\nDone.')
