import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# Customer data
# [Annual Spending, Visits Per Month]
X = np.array([
    [200, 2],
    [220, 3],
    [250, 2],
    [800, 8],
    [850, 9],
    [900, 10],
    [400, 5],
    [420, 6],
    [450, 5]
])

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

# Train model
kmeans.fit(X)

# Cluster labels
labels = kmeans.labels_

# Cluster centers
centroids = kmeans.cluster_centers_

print("Cluster Labels:")
print(labels)

print("\nCentroids:")
print(centroids)

# Plot data points
plt.scatter(X[:, 0], X[:, 1], c=labels)

# Plot centroids
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker='X',
    s=300
)

plt.xlabel("Annual Spending")
plt.ylabel("Visits Per Month")
plt.title("K-Means Customer Segmentation")

plt.show()