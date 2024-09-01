import pandas as pd

class DataIngestion:
    def load_csv(self, file_path):
        try:
            data = pd.read_csv(file_path)
            print(f"CSV file {file_path} loaded successfully.")
            return data
        except Exception as e:
            print(f"Failed to load CSV file: {e}")
    
    def load_json(self, file_path):
        try:
            data = pd.read_json(file_path)
            print(f"JSON file {file_path} loaded successfully.")
            return data
        except Exception as e:
            print(f"Failed to load JSON file: {e}")
    
    def load_excel(self, file_path):
        try:
            data = pd.read_excel(file_path)
            print(f"Excel file {file_path} loaded successfully.")
            return data
        except Exception as e:
            print(f"Failed to load Excel file: {e}")
from sklearn.preprocessing import StandardScaler

class DataPreprocessing:
    def remove_missing_values(self, data):
        cleaned_data = data.dropna()
        print("Missing values removed.")
        return cleaned_data
    
    def normalize_data(self, data):
        scaler = StandardScaler()
        normalized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
        print("Data normalized.")
        return normalized_data
    
    def handle_outliers(self, data):
        # Example: Removing outliers by clipping data to 1st and 99th percentiles
        clipped_data = data.clip(lower=data.quantile(0.01), upper=data.quantile(0.99), axis=1)
        print("Outliers handled.")
        return clipped_data
class AnalysisEngine:
    def identify_trends(self, data):
        trend = data.mean()  # Simplified example
        print("Trends identified.")
        return trend
    
    def identify_patterns(self, data):
        patterns = data.corr()  # Example: finding correlations
        print("Patterns identified.")
        return patterns
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier

class AnalysisEngine:
    def linear_regression(self, X, y):
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        print("Linear Regression performed.")
        return predictions
    
    def k_means_clustering(self, data, n_clusters=3):
        model = KMeans(n_clusters=n_clusters)
        labels = model.fit_predict(data)
        print("K-Means Clustering performed.")
        return labels
    
    def decision_tree(self, X, y):
        model = DecisionTreeClassifier()
        model.fit(X, y)
        predictions = model.predict(X)
        print("Decision Tree Classification performed.")
        return predictions
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

import argparse
class UserInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="AI Employee Interface")
        self.parser.add_argument("--file", type=str, help="Path to the data file")
        self.parser.add_argument("--format", type=str, choices=["csv", "json", "excel"], help="Format of the data file")
        self.parser.add_argument("--analysis", type=str, choices=["trend", "pattern", "regression", "clustering", "decision_tree"], help="Type of analysis to perform")
    
    def run(self):
        args = self.parser.parse_args()
        ingestion = DataIngestion()
        preprocessing = DataPreprocessing()
        analysis = AnalysisEngine()
        report = ReportGenerator()
        
        # Load data
        if args.format == "csv":
            data = ingestion.load_csv(args.file)
        elif args.format == "json":
            data = ingestion.load_json(args.file)
        elif args.format == "excel":
            data = ingestion.load_excel(args.file)
        
        # Preprocess data
        data = preprocessing.remove_missing_values(data)
        data = preprocessing.normalize_data(data)
        
        # Perform analysis
        if args.analysis == "trend":
            result = analysis.identify_trends(data)
        elif args.analysis == "pattern":
            result = analysis.identify_patterns(data)
        elif args.analysis == "regression":
            X, y = data.iloc[:, :-1], data.iloc[:, -1]  # Assuming last column is the target
            result = analysis.linear_regression(X, y)
        elif args.analysis == "clustering":
            result = analysis.k_means_clustering(data)
        elif args.analysis == "decision_tree":
            X, y = data.iloc[:, :-1], data.iloc[:, -1]  # Assuming last column is the target
            result = analysis.decision_tree(X, y)
        
        # Generate report
        report.generate_visualizations(data)
        report.generate_report({"Analysis Result": result}, "trends.png")
