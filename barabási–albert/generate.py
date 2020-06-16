import sys
import networkx as nx
import random
import collections
import json
import matplotlib.pyplot as plt

DEBUG = False

def convert_graph(g, cfactor):
    mg = collections.defaultdict(list)
    for node, alist in g.adjacency():
        for anode in alist:
            mg[node + cfactor].append(anode + cfactor)
    return(mg)


def merge_graphs(g1, g2):
    g_keys = list(g1.keys())
    g_keys.extend(list(g2.keys()))

    range_set = random.sample(range(1, 10000000), len(g_keys))

    mapping = {}

    for i in range(len(g_keys)):
        mapping[g_keys[i]] = range_set[i]

    def get_mapping(i):
        return(mapping[i])
        #return(i)

    ret_g = {}

    def add_graph(g):
        for node, alist in g.items():
            ret_g[get_mapping(node)] = [get_mapping(i) for i in alist]

    add_graph(g1)
    add_graph(g2)

    return(dict(sorted(ret_g.items())))


def visualize_graph(g):
    visual_graph = nx.Graph()
    for node, alist in g.items():
        for anode in alist:
            visual_graph.add_edge(node, anode)
            
    nx.draw(visual_graph, with_labels=True)
    plt.show()


def corrupt_graph(dest_graph, source_graph, corruption_factor, corrupt_all_nodes = False):
    dest_sorted = {k: v for k, v in sorted(dest_graph.items(), key=lambda item: len(item[1]))}

    # Destination has to be corrupted so that nodes with a lower degree are more likely to get corrupted. That's
    # why we are looking at dest_sorted here.
    dest_keys = list(dest_sorted.keys())
    
    source_keys = list(source_graph.keys())

    all_nodes_factor = 1 if corrupt_all_nodes else 1
    
    dest_node_indexes = random.sample(range(round(len(dest_sorted)/all_nodes_factor)), corruption_factor)
    if DEBUG: print(dest_graph)
    if DEBUG: print(source_graph)
    if DEBUG: print(dest_sorted)
    dest_nodes = [dest_keys[i] for i in dest_node_indexes]
    if DEBUG: print(dest_nodes)

    for node in dest_nodes:
        dest_sorted[node].extend(random.sample(source_keys, random.randint(1, 2)))
        
    return dest_sorted

if __name__ == '__main__':
    good_nodes = int(sys.argv[1])
    bad_nodes = int(sys.argv[2])
    corruption_factor = int(sys.argv[3])

    good_graph = nx.barabasi_albert_graph(good_nodes, 3)
    bad_graph = nx.barabasi_albert_graph(bad_nodes, 3)

    cfactor = len(good_graph)
    mgood = convert_graph(good_graph, 0)
    mbad = convert_graph(bad_graph, len(good_graph))

    # Corrupt good graph with some bad nodes.
    good_after_corruption = corrupt_graph(mgood, mbad, corruption_factor)

    # Corrupt bad graph with some good nodes
    bad_after_corruption = corrupt_graph(mbad, mgood, corruption_factor * 2, corrupt_all_nodes = True)

    if DEBUG: print(good_after_corruption)
    if DEBUG: print(bad_after_corruption)

    if DEBUG: print()
    
    full_graph = merge_graphs(good_after_corruption, bad_after_corruption)

    print(json.dumps(full_graph))

    visualize_graph(full_graph)

    

    
