import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from pylab import mpl
import matplotlib.font_manager
def plotting(graph, matrix_transform,vertice,edges) :
    '''networkx will automatically scale the data to fit the screen, I find it until now (TT) '''
    # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    # mpl.rcParams['font.sans-serif'] = ['SimHei']
    # mpl.rcParams['axes.unicode_minus'] = False
    G = nx.Graph()
    G.add_edges_from(edges)
    labels = {}
    for node in G.nodes() :
        labels[node] = node
    pos = {}
    for i in range(len(vertice)) :
        pos[vertice[i]] = matrix_transform[i]
    plt.rcParams['figure.figsize'] = (18,12)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_labels(G,pos,labels,font_family='Microsoft JhengHei')
    plt.show()
    # print(matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf'))
    return 0
    # wondering how to use chinese font，use "Microsoft JhengHei" to solve it
def stress_plot(stress_col) :
    stress_col = stress_col[0:]
    
    indices = list(range(len(stress_col)))
    plt.figure(figsize=(10, 5))  # Set the figure size (optional)
    plt.plot(indices, stress_col, marker='o', linestyle='-', color='b')  # Line plot
    
    # Setting x-axis ticks to be more sparse
    tick_spacing = 100  # Define tick spacing
    plt.xticks(np.arange(min(indices), max(indices)+1, tick_spacing))
    
    plt.title('stress per iteration')  # Title of the plot
    plt.xlabel('Iteration Index')  # X-axis label
    plt.ylabel('Stress')  # Y-axis label
    plt.grid(True)  # Show grid lines
    plt.xticks(indices)  # Set x-ticks to be every index where we have data
    plt.show()