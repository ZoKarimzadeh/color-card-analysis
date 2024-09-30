from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Color Card Analysis Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_report(output_path):
    pdf = PDF()
    pdf.add_page()
    # pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    # pdf.add_font('DejaVu', 'B', 'DejaVuSans-Bold.ttf', uni=True)
    
    # Add a title
    pdf.chapter_title('delta E Analysis Results')
    
    # Add a body
    pdf.chapter_body("This section contains the analysis results of delta E values across different targets.")
    
    # Save the PDF to the output path
    pdf.output(output_path)

if __name__ == "__main__":
    generate_report('output/Color_Card_Analysis_Report.pdf')
