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
