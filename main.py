from read_csvfile import *
from data_processing import *
from data_to_graph import *
#from expanding import *
#from mds_sklearn import *
#from mds_stress_majorization import *
from Chen_Shih_Liang_method_data import *
from directed_mds import *
#from plotting import *
from debug import *

from spring import *

# from leave_one_out import *
# TODO : directional MDS, chatgpt4.0 api, finding for landmark MDS
datanum = ["C:\\Users\\justi\Desktop\\project\\csv doc utf8\\GPT-4_史記_numerals_utf8.csv",
           "C:\\Users\\justi\Desktop\\project\\csv doc utf8\\GPT-4_漢書_numerals_utf8.csv",
           "C:\\Users\\justi\Desktop\\project\\csv doc utf8\\GPT-4_後漢書_numerals_utf8.csv"]
'''
pre_data = read_csvfile(datanum)
c_data,disset = data_process(pre_data)
#graph,vertice,dni,edges = return_connected_graph(c_data,disset)
graph,vertice,dni,edges,data= Chen_csv_and_graph()
tmp = vertice
pos_matrix = stress_majorization(graph,dni,vertice,edges)
plotting(graph,pos_matrix,vertice,edges)

n= len(graph)

pos_matrix = filter(n,pos_matrix,tmp,dni)
tmp = numpy.array(pos_matrix)
pos_matrix,n,s,m,t,weight,veight,in_direct_flag,dni,edges,sel_data,dis = directed_MDS(c_data,data,graph,vertice,dni,edges) # which graph is from Chen~.py

#pos_matrix = expand_ac_edgenum(graph,dni,vertice,edges)

nostress = vectorized_stress(n,s,m,t,tmp, weight,veight,in_direct_flag,dni,edges,sel_data,dis)
print(nostress)
plotting(graph,pos_matrix,vertice,edges)
'''
pre_data = read_csvfile(datanum)
c_data,disset = data_process(pre_data)
#graph,vertice,dni,edges = return_connected_graph(c_data,disset)
graph,vertice,dni,edges,data= Chen_csv_and_graph()
pos_matrix = directed_MDS(c_data,data,graph,vertice,dni,edges) # which graph is from Chen~.py
#pos_matrix = expand_ac_edgenum(graph,dni,vertice,edges)
#pos_matrix = stress_majorization(graph,dni,vertice,edges)
model_cmp(vertice,dni,pos_matrix)
#plotting(graph,pos_matrix,vertice,edges)
