# define a function which accepts a number and return its square.
# user=int(input("Enter the number:"))
# square=pow(user,2)
# print(square)
from fpdf import FPDF
ref=FPDF()
ref.add_page()
ref.set_font("Arial", size=20)
ref.cell(200,100,"Welcome to pdf", align="L")

ref.output("pythonFile.pdf")