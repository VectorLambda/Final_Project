from pdfquery import PDFQuery

pdf = PDFQuery('Route_3.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
#text = [t.text for t in text_elements]

#print(text)

text_file = open("Route_3.txt", "w")
for t in text_elements:
    text_file.write(str(t))
text_file.close()