from networkx import *
import os
import pylab as plt
import matplotlib.pyplot as plt
from operator import itemgetter
os.getcwd()


#модуль для анализа графа
#позволяет визуализировать и анализировать граф
#находит общую информацию о графе, высчитывает такие метрики как pagerank, коэффициент кластеризации, находит доминантное множество,
#триадическое закрытие. Данные значения могут быть полезны для выявления наиболее сплоченных и влиятельных пользователей в рассматриваемой сети

def GetLabels():
    file = open('Vertex.txt', 'rt', encoding='utf8')
    list = []
    dict = {}
    for i in file:
        list.append(i)
    for i in list:
        s = i.split('\t')
        s[0] = int(s[0])
        s[1] = str(s[1][0:(len(s[1]) - 1)])
        dict[s[0]] = s[1]
    file.close()
    return dict

def GetGraphInfo(gr):
    s = ''
    ss = nx.info(gr).split('\n')
    ss[0] = 'Анализ графа\n\n'
    ss[1] = 'Тип:\t\tГраф'
    ss[2] = 'Количество вершин: \t ' + ss[2][17:len(ss[2])]
    ss[3] = 'Количество ребер: \t ' + ss[3][17:len(ss[3])]
    ss[4] = 'Средняя степень:\t' + ss[4][16:len(ss[4])]
    for i in ss:
        s = s + i + '\n'
    if (is_connected(gr)):
        s = s + 'Радиус:\t\t' + str(radius(gr)) + \
            '\nЦентр:\t\t' + str(center(gr)) + \
            '\nДиаметр:\t\t' + str(diameter(gr))
    s = s + '\nТранзитивность:\t' + str(nx.transitivity(gr))+\
        '\nСр. коэф. кластеризации:\t'+ str(nx.average_clustering(gr))+\
        '\nКоличество клик:\t' + str(graph_clique_number(gr)) + \
        '\nСвязность графа:\t' + str(is_connected(gr)) + \
        '\nКол-во связных компонентов:\t' + str(number_connected_components(gr))
    return s

def getPagerank(gr):
    pr = nx.pagerank(gr)
    pr1 = sorted(pr.items(), key=itemgetter(1), reverse=True)
    prcount = len(pr1) * 0.2
    prnodes = []
    s = ''
    i = 0
    while (i < prcount):
        s = s + str(pr1[i][0]) + ': \t' + str(pr1[i][1]) + '\n'
        prnodes.append(pr1[i][0])
        i = i + 1
    s = 'PageRank\n\n' + s
    pos = nx.spring_layout(gr)
    labels = GetLabels()
    nx.draw_networkx_nodes(gr, pos, node_color='b', node_size=20, alpha=0.8)
    nx.draw_networkx_edges(gr, pos, width=0.5, alpha=0.8)
    nx.draw_networkx_nodes(prnodes, pos, node_color='r', node_size=20, alpha=0.8)
    plt.axis('off')
    plt.title('VK Network')
    plt.show()
    plt.savefig('VK Network.png')
    return s

def getClustering(gr):
    cl = nx.clustering(gr)
    cl1 = sorted(cl.items(), key=itemgetter(1), reverse=True)
    clcount = len(cl1) * 0.2
    clnodes = []
    s = ''
    i = 0
    while (i < clcount):
        s = s + str(cl1[i][0]) + ': \t' + str(cl1[i][1]) + '\n'
        clnodes.append(cl1[i][0])
        i = i + 1
    s = 'Коэффициент кластеризации\n\n' + s
    pos = nx.spring_layout(gr)
    labels = GetLabels()
    nx.draw_networkx_nodes(gr, pos, node_color='b', node_size=40, alpha=0.8)
    nx.draw_networkx_edges(gr, pos, width=0.5, alpha=0.8)
    nx.draw_networkx_nodes(clnodes, pos, node_color='r', node_size=40, alpha=0.8)
    plt.axis('off')
    plt.title('VK Network')
    plt.show()
    plt.savefig('VK Network.png')
    return s

def getDominant(gr):
    dom = dominating_set(gr)
    s = ''
    for i in dom:
        s = s + str(i) + '\n'
    s = 'Доминантное множество\n\n' + s
    pos = nx.spring_layout(gr)
    labels = GetLabels()
    nx.draw_networkx_nodes(gr, pos, node_color='b', node_size=20, alpha=0.8)
    nx.draw_networkx_edges(gr, pos, width=0.5, alpha=0.8)
    nx.draw_networkx_nodes(dom, pos, node_color='r', node_size=20, alpha=0.8)
    plt.axis('off')
    plt.title('VK Network')
    plt.show()
    plt.savefig('VK Network.png')
    return s

def getTrian(gr):
    tr = nx.triangles(gr)
    tr1 = sorted(tr.items(), key=itemgetter(1), reverse=True)
    trcount = len(tr1) * 0.2
    trnodes = []
    s = ''
    i = 0
    while (i < trcount):
        s = s + str(tr1[i][0]) + ': \t' + str(tr1[i][1]) + '\n'
        trnodes.append(tr1[i][0])
        i = i + 1
    s = 'Триадическое закрытие\n\n' + s
    pos = nx.spring_layout(gr)
    labels = GetLabels()
    nx.draw_networkx_nodes(gr, pos, node_color='b', node_size=20, alpha=0.8)
    nx.draw_networkx_nodes(trnodes, pos, node_color='r', node_size=20, alpha=0.8)
    nx.draw_networkx_edges(gr, pos, width=0.5, alpha=0.8)
    plt.axis('off')
    plt.title('VK Network')
    plt.show()
    plt.savefig('VK Network.png')
    return s

def DrawG(gr):
    pos = nx.spring_layout(gr)
    nx.draw_networkx_nodes(gr, pos, node_color='b', node_size=40, alpha=0.8)
    nx.draw_networkx_edges(gr, pos, width=0.5, alpha=0.8)
    nx.draw_networkx_edges(gr, pos, width=0.5, alpha=0.8)
    plt.axis('off')
    plt.title('VK Network')
    plt.show()
    plt.savefig('VK Network.png')