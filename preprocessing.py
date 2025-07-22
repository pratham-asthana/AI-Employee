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
