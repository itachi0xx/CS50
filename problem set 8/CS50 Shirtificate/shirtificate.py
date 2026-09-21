from fpdf import FPDF

def main():

    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    pdf.set_font("helvetica", style="B", size=24)

    pdf.cell(0, 20, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')

    pdf.image("shirtificate.png", x=15, y=55, w=180)


    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(15, 140)
    pdf.cell(180, 10, name, align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()