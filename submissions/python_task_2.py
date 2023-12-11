import pandas as pd
import networkx as nx

def calculate_distance_matrix(file_path):
    df = pd.read_csv(file_path)
    G = nx.from_pandas_edgelist(df, 'id_start', 'id_end', ['distance'])

    all_pairs_distances = dict(nx.all_pairs_dijkstra_path_length(G))
    nodes = sorted(G.nodes)
    distance_matrix = pd.DataFrame(index=nodes, columns=nodes)
    for node1 in nodes:
        for node2 in nodes:
            if node1 == node2:
                distance_matrix.loc[node1, node2] = 0
            elif node2 in all_pairs_distances[node1]:
                distance_matrix.loc[node1, node2] = all_pairs_distances[node1][node2]

    # Ensure the matrix is symmetric
    distance_matrix = distance_matrix + distance_matrix.T

    return distance_matrix

file_path = 'datasets\dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(file_path)
print(result_distance_matrix)