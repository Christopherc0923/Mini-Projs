from typing import List, Tuple

import numpy as np
from sklearn.cluster import DBSCAN
import pandas as pd

def calculate_cluster_means(df, x_column, y_column):
    # Extract the x and y coordinates from the dataframe
    points = df[[x_column, y_column]].values

    # Apply the DBSCAN algorithm to the points
    dbscan = DBSCAN(eps=3, min_samples=1)
    clusters = dbscan.fit_predict(points)

    cluster_means = []
    for cluster in set(clusters):
        # Extract the points in the current cluster
        points_in_cluster = points[clusters == cluster]
        # Calculate the mean of the cluster by summing the coordinates of all the points and dividing by the number of points
        cluster_mean = (points_in_cluster[:, 0].mean(), points_in_cluster[:, 1].mean())
        cluster_means.append(cluster_mean)

    return cluster_means, clusters

df = pd.DataFrame({'x': [10.5, 11, 10.64, 19.9, 20.1], 'y': [10.5, 11, 10.64, 20, 21]})

cluster_means, clusters = calculate_cluster_means(df, 'x', 'y')

# Add the cluster labels to the dataframe as a new column
df['cluster'] = clusters

print(df)