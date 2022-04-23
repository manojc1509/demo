import tabula 
pdf_path ="final.pdf"
table = tabula.read_pdf(pdf_path,pages='all')
tabula.convert_into(pdf_path,"final.csv",output_format="csv",pages="all")

