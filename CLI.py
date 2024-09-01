import argparse
from AI_Employee import DataIngestion, DataPreprocessing, AnalysisEngine, ReportGenerator
class UserInterface:
    
    parser = argparse.ArgumentParser(description='AI Employee Prototype CLI')
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="AI Employee Interface")
        self.parser.add_argument("--file", type=str, help="Path to the data file")
        self.parser.add_argument("--format", type=str, choices=["csv", "json", "excel"], help="Format of the data file")
        self.parser.add_argument("--analysis", type=str, choices=["trend", "pattern", "regression", "clustering", "decision_tree"], help="Type of analysis to perform")
    
    def main():
    parser = argparse.ArgumentParser(description='AI Employee Prototype CLI')
    
    parser.add_argument('--load_csv', type=str, help='Load a CSV file.')
    parser.add_argument('--clean_data', action='store_true', help='Clean the data by removing missing values.')
    parser.add_argument('--run_analysis', action='store_true', help='Run analysis on the loaded data.')
    
    args = parser.parse_args()
    
    if args.load_csv:
        ingestion = DataIngestion()
        data = ingestion.load_csv(args.load_csv)
        print(f"CSV file {args.load_csv} loaded successfully.")
    
    if args.clean_data:
        preprocessing = DataPreprocessing()
        data = preprocessing.remove_missing_values(data)
        print("Missing values removed.")
    
    if args.run_analysis:
        analysis = AnalysisEngine()
        analysis.run_analysis(data)
        print("Analysis performed.")
        
if __name__ == "__main__":
    main()