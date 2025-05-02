from sklearn.manifold import MDS
import numpy as np
def floyd_warshall(graph,dni) :
    inf = float('inf')
    vn = len(graph)
    dis_matrix = [[inf]*vn for i in range(vn)]
    # has_value = [[False]*vn for i in range(vn)]
    for ver in graph :
        for row in ver :
            dis_matrix[dni[row[0]]][dni[row[1]]] = int(row[3])
            # has_value[dni[row[0]]][dni[row[1]]] = True

    for k in range(vn):
        for i in range(vn):
            for j in range(vn):
                dis_matrix[i][j] = min(dis_matrix[i][j], dis_matrix[i][k] + dis_matrix[k][j])
    '''
    for i in range(vn):
            for j in range(vn):
                if has_value[i][j] == False :
                    dis_matrix[i][j] = 0.5 * dis_matrix[i][j]
    '''
    return dis_matrix
def mds_alg(dis_matrix) :
   embedding = MDS(random_state=0,dissimilarity='precomputed',normalized_stress = 'auto')
   matrix_transform = embedding.fit_transform(dis_matrix)
   return matrix_transform
def mds(graph,dni) :
    dis_matrix = floyd_warshall(graph,dni)
    dis_m = np.array(dis_matrix)
    matrix_transform = mds_alg(dis_m)
    return matrix_transform