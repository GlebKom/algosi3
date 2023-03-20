graph_asia = {
    'Afghanistan': {'Iran': 921, 'Pakistan': 682, 'Tajikistan': 1206, 'Turkmenistan': 747, 'Uzbekistan': 1374},
    'Bangladesh': {'India': 1938, 'Myanmar': 193},
    'Bhutan': {'China': 470, 'India': 188},
    'Brunei': {'Indonesia': 1246, 'Malaysia': 83},
    'Cambodia': {'Laos': 541, 'Thailand': 803, 'Vietnam': 1229},
    'China': {'India': 2955, 'Kazakhstan': 1597, 'Kyrgyzstan': 1051, 'Mongolia': 4676, 'Nepal': 1236, 'North Korea': 1416, 'Pakistan': 3006, 'Russia': 3695, 'Tajikistan': 4148, 'Vietnam': 1282},
    'India': {'Nepal': 1035, 'Pakistan': 1066},
    'Indonesia': {'Malaysia': 1075, 'Papua New Guinea': 2196, 'Philippines': 2146},
    'Iran': {'Iraq': 1458, 'Pakistan': 909, 'Turkey': 1943, 'Turkmenistan': 992},
    'Iraq': {'Jordan': 901, 'Kuwait': 272, 'Saudi Arabia': 886, 'Syria': 503, 'Turkey': 1289},
    'Israel': {'Jordan': 100, 'Lebanon': 130, 'Syria': 76},
    'Japan': {'North Korea': 1058, 'Russia': 1880, 'South Korea': 228},
    'Jordan': {'Saudi Arabia': 734, 'Syria': 375},
    'Kazakhstan': {'Kyrgyzstan': 1052, 'Russia': 6616, 'Turkmenistan': 423, 'Uzbekistan': 1112},
    'Kuwait': {'Saudi Arabia': 222},
    'Kyrgyzstan': {'Tajikistan': 996, 'Uzbekistan': 1115},
    'Laos': {'Thailand': 730, 'Vietnam': 808},
    'Lebanon': {'Syria': 83},
    'Malaysia': {'Thailand': 1023},
    'Mongolia': {'Russia': 3499},
    'Myanmar': {'Thailand': 2025},
    'Nepal': {'China': 1236, 'India': 1035},
    'North Korea': {'Russia': 19, 'South Korea': 222},
    'Oman': {'Saudi Arabia': 676, 'Yemen': 585},
    'Pakistan': {'Tajikistan': 1308},
    'Philippines': {'Taiwan': 408},
    'Qatar': {'Saudi Arabia': 743},
    'Russia': {'China': 3695, 'Kazakhstan': 6616, 'North Korea': 19},
    'Saudi Arabia': {'Syria': 1306},
    'Singapore': {'Malaysia': 1},
    'South Korea': {'Russia': 19},
    'Syria': {'Turkey': 822},
    'Taiwan': {'China': 844},
    'Tajikistan': {'Uzbekistan': 488},
    'Thailand': {'Vietnam': 805},
    'Turkey': {'Ukraine': 1705},
    'Turkmenistan': {'Uzbekistan': 1605},
    'United Arab Emirates': {'Oman': 409, 'Saudi Arabia': 654},
    'Uzbekistan': {'Turkmenistan': 1605},
    'Vietnam': {},
    'Papua New Guinea': {},
    'Yemen': {},
    'Ukraine': {}
}


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):  #Метод создан из-за того, что ChatGPT создал граф не полно-ориентированный
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):  #Возвращает узлы графа
        return self.nodes

    def get_outgoing_edges(self, node):  #Возвращает соседей узла
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):  #Возвращает значение ребра между двумя узлами.
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = graph.get_nodes()
    shortest_path = {}
    previous_nodes = {}
    for node in unvisited_nodes:
        shortest_path[node] = float('inf')
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbours = graph.get_outgoing_edges(current_min_node)
        for neighbour in neighbours:
            possible_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbour)
            if possible_value < shortest_path[neighbour]:
                shortest_path[neighbour] = possible_value
                previous_nodes[neighbour] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

nodes = list(graph_asia.keys())
previous_nodes, shortest_path = dijkstra_algorithm(Graph(nodes, graph_asia), 'Russia')

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    print(f"Найден маршрут из {start_node} в {target_node}, протяженностью {shortest_path[target_node]} км.")
    print(" - ".join(reversed(path)))

    
print_result(previous_nodes, shortest_path, 'Russia', 'Ukraine')
