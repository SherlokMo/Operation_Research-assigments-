#encoding=utf-8
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pulp

df=pd.read_csv("data.csv")

def draw(df,root):
    x,y = list(df["x"]),list(df["y"])
    plt.scatter(x,y)
    for i in range(len(root)):
        plt.plot([x[i-1],x[i]],[y[i-1],y[i]],c="r")
    plt.show()

def draw_edge(df,edges):
    x,y = list(df["x"]),list(df["y"])
    plt.scatter(x,y)
    for i,j in edges:
        plt.plot([x[i],x[j]],[y[i],y[j]],c="r")
    plt.show()

def add_cut(df,edges,problem,var):
    G = nx.Graph()
    for i,j in edges:
        G.add_edge(i,j)
    List = sorted(nx.connected_components(G), key = len, reverse=True)

    if len(List)==1:
        return True

    temp=[[0] for l in List]
    for i,j in edges:
        for l in range(len(List)):
            if i in List[l] and j in List[l]:
                temp[l] += var[i][j]
                continue

    for l in range(len(List)):
        problem += temp[l] <= len(List[l])-1
    return False

problem = pulp.LpProblem(sense=pulp.LpMinimize)

var = pulp.LpVariable.dicts('x', ([i for i in range(len(df))], [j for j in range(len(df))]), 0, 1, 'Binary')

dist = {}
for i in range(len(df)):
    dist[i]={}
    for j in range(len(df)):
        dist[i][j] = np.linalg.norm(df.ix[i]-df.ix[j])

temp=0
for i in range(len(df)):
    for j in range(len(df)):
        temp += dist[i][j]*var[i][j]
problem += temp

for i in range(len(df)):
    temp = 0
    for j in range(len(df)):
        if i!=j:
            temp += var[i][j]
    problem += temp == 1

for i in range(len(df)):
    temp = 0
    for j in range(len(df)):
        if i!=j:
            temp += var[j][i]
    problem += temp == 1

while True:
    status = problem.solve()
    print("Status", pulp.LpStatus[status])

    edges=[]
    for i in range(len(df)):
        for j in range(len(df)):
            if var[i][j].value() == 1.0:
                edges.append((i,j))

    draw_edge(df,edges)
    if add_cut(df,edges,problem,var):
        break
