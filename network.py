class Node:
    def __init__(self,name:str, x_cord: int, y_cord: int, 
                 source: bool, destination: bool):
        self.name=name
        self.x_cord=x_cord
        self.y_cord=y_cord
        self.source=source
        self.destination=destination
        self.connected_nodes=[]

        self.connected_edges=[]
        
class Edge:
    def __init__(self,name:str, start_node:Node, end_node:Node):
        self.name=name
        self.start_node=start_node
        self.end_node=end_node


class Network:

    def __init__(self):
        self.list_of_nodes=[]
        self.list_of_edges=[]
        connected_index={0:[1],1:[0]}
        self.list_of_nodes.append(Node("A",10,20, True, True))
        self.list_of_nodes.append(Node("B",10,30, True, True))
        for index in connected_index.keys():
            node_1=self.list_of_nodes[index]
            for ind in connected_index[index]:
             node_2=self.list_of_nodes[ind]
             edge=Edge(node_1.name+" "+node_2.name,node_1, node_2)
             self.list_of_edges.append(edge)
        
        


Network()