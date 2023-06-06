import matplotlib.pyplot as plt
from random import randint, sample
import numpy as np


class Graph:
    def __init__(self, nodes=None, edges=None, generate=None):
        if nodes:
            if type(nodes) == int:
                self.nodes = {i: Node() for i in range(nodes)}
            elif type(nodes) == list:
                self.nodes = {i: Node(info) for i, info in nodes}
        if edges:
            self.edges = edges
            self.set_adjacency_by_edges(edges)
        elif generate == 'random':
            self.generate_random_graph()
        else:
            self.nodes = {}
            self.edges = []
        self.independent_nodes = []

    def __len__(self):
        return len(self.nodes)

    def set_adjacency_by_edges(self, edges):
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            self.nodes[node1].neighbours.append(node2)
            self.nodes[node2].neighbours.append(node1)

    def add_node(self, node_id, node_info=''):
        self.nodes[node_id] = Node(node_info)

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))
        self.set_adjacency_by_edges([(node1, node2)])

    def add_edges(self, edges):
        self.edges.extend(edges)
        self.set_adjacency_by_edges(edges)

    def generate_random_graph(self, max_nodes=10):
        n_nodes = randint(1, max_nodes)
        n_edges = randint(0, n_nodes * (n_nodes - 1) // 2)
        self.nodes = {i: Node() for i in range(n_nodes)}
        self.edges = list({tuple(sorted(sample(list(self.nodes.keys()), 2))) for _ in range(n_edges)})
        self.set_adjacency_by_edges(self.edges)

    def max_ivs(self):
        """
        'Обертка' для алгоритма поиска наибольшего независимого множества
        :return: индексы вершин наибольшего независимого множества
        """
        self.independent_nodes = self._graph_sets(self.nodes)
        return self.independent_nodes

    def _graph_sets(self, graph):
        """
        Задача поиска наибольшего независимого множества является NP-полной,
        то есть её врядли можно решить за полиномиальное время.

        Сложность алгоритма O(2^N)
        Занимаемая память O(N)

        Для сравнения:
        Сложность полного перебора O(N^2 * 2^N)
        Сложность алгоритма Робсона O(2^0.276N)
        """
        if (len(graph) == 0):
            return []

        if (len(graph) == 1):
            return [list(graph.keys())[0]]

        vCurrent = list(graph.keys())[0]

        graph2 = dict(graph)
        del graph2[vCurrent]

        res1 = self._graph_sets(graph2)

        for v in graph[vCurrent].neighbours:
            if (v in graph2):
                del graph2[v]

        res2 = [vCurrent] + self._graph_sets(graph2)

        if (len(res1) > len(res2)):
            return res1
        return res2

    def draw_graph(self):
        fig = plt.figure()
        angle = np.arange(0, 1, 1 / len(self)) * np.pi * 2
        x = np.cos(angle)
        y = np.sin(angle)
        keys = list(self.nodes.keys())
        plt.scatter(x, y, s=100)
        # plt.scatter(x[np.where(np.isin(keys, self.independent_nodes))],
        #             y[np.where(np.isin(keys, self.independent_nodes))], s=100)
        plt.scatter(x[[keys.index(i) for i in self.independent_nodes]],
                    y[[keys.index(i) for i in self.independent_nodes]], s=100)

        for i, txt in enumerate(keys):
            plt.annotate(txt, (x[i], y[i]), size=22)
        for edge in self.edges:
            i, j = keys.index(edge[0]), keys.index(edge[1])
            plt.plot((x[i], x[j]), [y[i], y[j]], color='blue')
        plt.axis('off')
        return fig


class Node:
    def __init__(self, info=''):
        self.info = info
        self.neighbours = []


if __name__ == '__main__':
    # инициализация по количеству вершин
    n_vertices = 5
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (3, 4)]
    g1 = Graph(n_vertices, edges)

    g1.add_node('abc', '345345 + some info')
    g1.add_node('qwerty')
    g1.add_edge(1, 'abc')
    g1.add_edges([(1, 'abc'), ('abc', 'qwerty')])
    print(g1.edges)
    g1_ivs = g1.max_ivs()
    g1.draw_graph()
    plt.show()

    # инициализация с произвольными индексами вершин и информацией в них
    nodes = [['a', 'info1'], [2, 'info2'], [3, 'info3']]
    edges1 = [('a', 2), (2, 3)]
    g2 = Graph(nodes, edges1)

    g2.add_node(12, '345345')
    g2.add_edge(12, 'a')
    print(g2.max_ivs())
    g2.draw_graph()
    plt.show()

    # инициализация случайного графа
    g3 = Graph(generate='random')
    print(g3.max_ivs())
    g3.draw_graph()
    plt.show()

    # проверка устойчивости алгоритма поиска независимых множеств на нескольких случайных графах
    for i in range(10):
        g = Graph(generate='random')
        g.max_ivs()
        g.draw_graph()
        plt.savefig(f'./images/graph_{i}')
