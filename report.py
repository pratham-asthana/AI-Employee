import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

class ReportGenerator:
    def generate_visualizations(self, data):
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data)
        plt.title("Data Trends")
        plt.savefig("trends.png")
        plt.close()
        print("Visualization generated.")
    
    def generate_report(self, analysis_results, visualizations):
        pdf = FPDF()
        pdf.add_page()
        
        # Title
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Analysis Report", ln=True, align='C')
        
        # Analysis Results
        pdf.set_font("Arial", size=10)
        for key, value in analysis_results.items():
            pdf.multi_cell(0, 10, txt=f"{key}: {value}")
        
        # Add visualization image
        pdf.image("trends.png", x=10, y=50, w=180)
        
        pdf.output("report.pdf")
        print("Report generated.")
