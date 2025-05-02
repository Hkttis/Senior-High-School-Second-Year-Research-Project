from debug import *
def turn_around(c):
    dirdni = {'東':'西', '西':'東', '北':'南', '南':'北', 
              '東南':'西北', '西北':'東南', '東北':'西南', '西南':'東北'}
    return 'dirdni[c]'
def data_to_graph(cl_data,dis_set) :
    graph = [] # index => 地點1(item) 地點2(item) 方位 里程
    for i in range(len(dis_set)) : # [ row1 row2 ...]
        graph.append([])
    dni = {} #　dict : node to index
    vertice = [] # vertice collects countries
    count = 0 # contry <-> index, being index of graph and corresponding to rows
    for element in dis_set :
        dni[element] = count
        vertice.append(element)
        count = count+1
    
    distance_data = cl_data[0] + cl_data[1]
    edges = [] 
    for row in distance_data :
        edges.append([row[0],row[1]])
    
    for row in distance_data : # fill data into its country row[0]
        graph[ dni[row[0]] ].append(row[0:4])
        graph[ dni[row[1]] ].append([row[1]]+[row[0]]+[turn_around(row[2])]+[row[3]])
    return graph,vertice,dni,edges

def dfs(graph,dni,vertice,index,mark,ct):
    for row in graph[index] :
        if mark[dni[row[1]]]==True :
            mark[dni[row[1]]] = False
            ct = ct +1
            mark,ct = dfs(graph,dni,vertice,dni[row[1]],mark,ct)
    return mark,ct

def find_component(graph,dni,vertice) :
    mark = [True for i in range(len(vertice))]
    top_node = []
    major_mark = []
    pre_ct = 0
    for i in range(len(vertice)) :
        if mark[i]==True :
            top_node.append(graph[i][0])
            mark,ct = dfs(graph,dni,vertice,i,mark,0)
            if ct >= pre_ct :
                major_mark = mark.copy()
                pre_ct = ct
        # ct is the amount of nodes in component
        # print(i)
        # print(ct) 96,3,2,2,2 <=> 0,3,14,49,61
    return top_node,major_mark

def majorize_graph(graph,vertice,dni,major_mark,edges) :
    major_graph = [] # [p1(chi),p2(chi),dir,dis][]
    major_vertice = [] # chi
    major_dni = {} # chi => num
    count = 0
    for i in range(len(major_mark)) :
        if major_mark[i] == False :
            major_vertice.append(vertice[i])
            major_dni[vertice[i]] = count
            count = count + 1
    for i in range(len(major_vertice)) :
        major_graph.append([])
    for i in range(len(graph)) :
        if major_mark[i] == False :
            major_graph[major_dni[graph[i][0][0]]] = graph[i]
    major_edges = []
    for edge in edges :
        if major_mark[dni[edge[0]]]== False :
            major_edges.append(edge)
    tuplever_edges = []
    for edge in major_edges :
        tuplever_edges.append(tuple(edge))
    return major_graph,major_vertice,major_dni,tuplever_edges

def return_connected_graph(c_data,disset) :
  graph , vertice , dni , edges= data_to_graph(c_data,disset)
  # output(graph,3,'pregraph')
  cri_nodes , major_mark = find_component(graph,dni,vertice)
  graph , vertice , dni ,edges= majorize_graph(graph,vertice,dni,major_mark,edges)
  # output(graph,3,'newgraph')
  return graph,vertice,dni,edges