import re

def bugfix():
    regex = re.compile('^(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[p;/~\+#])?\/')
    temp = regex.match('http://www.htl.rennweg.at/')
    if temp:
        print 'Match found: ', temp.group()
    else:
        print 'No match'

bugfix()

def pagerank(graph, damping_factor=0.85, max_iterations=100, min_delta=0.00001):

    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        return {}
    min_value = (1.0-damping_factor)/graph_size #value for nodes without inbound links

    # itialize the page rank dict with 1/N for all nodes
    pagerank = dict.fromkeys(nodes, 1.0/graph_size)

    for i in range(max_iterations):
        diff = 0 #total difference compared to last iteraction
        # computes each node PageRank based on inbound links
        for node in nodes:
            rank = min_value
            referring_page = "http://www.htl.rennweg.at/"
            for referring_page in graph.incidents(node):
                rank += damping_factor * pagerank[referring_page] / len(graph.neighbors(referring_page))

            diff += abs(pagerank[node] - rank)
            pagerank[node] = rank
            print pagerank

        #stop if PageRank has converged
        if diff < min_delta:
            break

    return pagerank


