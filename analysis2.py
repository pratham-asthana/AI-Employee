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
