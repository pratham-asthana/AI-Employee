import unittest
import pandas as pd
from ingestion import DataIngestion, DataPreprocessing, AnalysisEngine  # Replace `your_module` with the actual module name

class TestAIEmployee(unittest.TestCase):
    def test_load_csv(self):
        ingestion = DataIngestion()
        data = ingestion.load_csv("olympics.csv")
        self.assertIsNotNone(data)  # Ensure data is loaded
    
    def test_remove_missing_values(self):
        preprocessing = DataPreprocessing()
        data = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
        cleaned_data = preprocessing.remove_missing_values(data)
        self.assertEqual(len(cleaned_data), 1)  # Only one row should remain
    
    def test_linear_regression(self):
        analysis = AnalysisEngine()
        X = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        y = pd.Series([7, 8, 9])
        predictions = analysis.linear_regression(X, y)
        self.assertEqual(len(predictions), 3)  # Ensure predictions are made for all inputs

if __name__ == "__main__":
    unittest.main()
