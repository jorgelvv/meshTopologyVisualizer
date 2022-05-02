import json
# import time
# import matplotlib.pyplot as plt
# import numpy as np
# import networkx as nx
#
# from serial_rw import Serial

# class NodeMapping:
#
#     meshTopo = """[
#     {
#         "nodeId" : 2147321731,
#         "subs" : [
#             {
#                 "nodeId" : 2147319552,
#                 "subs" : [
#                 ]
#             }
#         ]
#     },
#     {
#         "nodeId" : 2142436483,
#         "subs" : [
#             {
#                 "nodeId" : 2787708644,
#                 "subs" : [
#                 ]
#             }
#         ]
#     }
# ]"""
#     # TODO: more parameters init may be needed
#     def __init__(self, xMapSize=15, yMapSize=15):
#         #self.data = json.loads(NodeMapping.meshTopo)
#         self.xMapSize = xMapSize
#         self.yMapSize = yMapSize
#
#         self.initNode = [int(self.xMapSize / 2), int(self.yMapSize / 2)]                   # initial node position
#         self.initDirection = [0, 1]                                                        # initial direction vector
#         self.nodeMap = BitArray2D.BitArray2D(rows=self.xMapSize, columns=self.yMapSize)    # create 2D bit array of node map
#         self.nodeMap[int(self.xMapSize / 2), int(self.yMapSize / 2)] = 1                   # initialize the starting node position at the window CENTER
#         self.relationList = []                                                             # list holding all relations
#
#     # """
#     # Initializing serial port.
#     # :return: serialObj
#     # """
#     # def init_serial(self, comPort=None, baudRate=115200):
#     #     serialObj = Serial(comPort, baudRate)
#     #     return serialObj
#
#     def find_empty_position(self, neighbourNodeId, currentNode, direction, nodeMap, relationList):
#         found = 0                                                                       # indication that an empty is found
#         allDir = [[1, 0], [0, 1], [-1, 0], [0, -1]]                                     # define North, East, West, South direction vectors
#         newNode = [currentNode[0] + direction[0], currentNode[1] + direction[1]]        # try a new spot according to the preferred direction
#         allDir.remove(direction)                                                        # remove the used direction
#
#         # if available, take it
#         if not nodeMap[ godel (newNode[0], newNode[1])]:
#
#             nodeMap[newNode] = 1                                        # update node_map. the new_node is now taken
#             relationList.append([currentNode[:], newNode[:]])           # put the relation in the list
#             currentNode[:] = newNode                                    # update current_node
#                                                                         # direction unchanged
#             found = 1
#             #pass
#
#         # otherwise, try other directions
#         else:
#             # try every other direction until find an empty one
#             for dir in allDir:
#                 newNode = [currentNode[0] + dir[0], currentNode[1] + dir[1]]         # try a new spot
#
#                 # Got a empty spot. Take it
#                 if not nodeMap[ godel(newNode[0], newNode[1])]:
#                     nodeMap[newNode] = 1                                          # update node_map. the new_node is now taken
#                     relationList.append([currentNode[:], newNode[:]])            # put the relation in the list
#                     currentNode[:] = newNode                                      # update current_node
#                     direction[:] = dir                                              # update the preferred direction
#                     found = 1
#                     break
#
#         # TODO: Cannot find an empty spot
#         # if (found == 0):
#         pass
#
#     def recursive_node_mapping(self, obj, current_node_pos, direction, node_map, relation_list):
#         #TODO: paramters' value can be defaulted to None. Then check if None, assign to predefined values. Otherwise, assign to the passed in values
#
#         # if the object is a dictionary, then it contains its one nodeId, and its one subconnection list
#         if isinstance(obj, dict):
#             # direct neighbour of the current_node
#             neighbourNodeId = obj["nodeId"]
#             # find empty position in node_mapping, update current_node, update direction, update relation_list
#             self.find_empty_position(neighbourNodeId, current_node_pos, direction, node_map, relation_list)
#             #print (neighbourNodeId)
#
#             # go into the node's subconnections
#             for item in obj["subs"]:
#                 self.recursive_node_mapping(item, current_node_pos[:], direction, node_map, relation_list)
#
#         # if the object is a list, then it is a list of dictionaries
#         elif isinstance(obj, list):
#             for item in obj:
#                 self.recursive_node_mapping(item, current_node_pos[:], direction, node_map, relation_list)
#         # else:
#         #     return obj
#             #print (obj)
#
#         class NodeMapping:
#
#             meshTopo = """[
#             {
#                 "nodeId" : 2147321731,
#                 "subs" : [
#                     {
#                         "nodeId" : 2147319552,
#                         "subs" : [
#                         ]
#                     }
#                 ]
#             },
#             {
#                 "nodeId" : 2142436483,
#                 "subs" : [
#                     {
#                         "nodeId" : 2787708644,
#                         "subs" : [
#                         ]
#                     }
#                 ]
#             }
#         ]"""
#
#             # TODO: more parameters init may be needed
#             def __init__(self, xMapSize=15, yMapSize=15):
#                 # self.data = json.loads(NodeMapping.meshTopo)
#                 self.xMapSize = xMapSize
#                 self.yMapSize = yMapSize
#
#                 self.initNode = [int(self.xMapSize / 2), int(self.yMapSize / 2)]  # initial node position
#                 self.initDirection = [0, 1]  # initial direction vector
#                 self.nodeMap = BitArray2D.BitArray2D(rows=self.xMapSize,
#                                                      columns=self.yMapSize)  # create 2D bit array of node map
#                 self.nodeMap[int(self.xMapSize / 2), int(
#                     self.yMapSize / 2)] = 1  # initialize the starting node position at the window CENTER
#                 self.relationList = []  # list holding all relations
#
#             # """
#             # Initializing serial port.
#             # :return: serialObj
#             # """
#             # def init_serial(self, comPort=None, baudRate=115200):
#             #     serialObj = Serial(comPort, baudRate)
#             #     return serialObj
#
#             def find_empty_position(self, neighbourNodeId, currentNode, direction, nodeMap, relationList):
#                 found = 0  # indication that an empty is found
#                 allDir = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # define North, East, West, South direction vectors
#                 newNode = [currentNode[0] + direction[0],
#                            currentNode[1] + direction[1]]  # try a new spot according to the preferred direction
#                 allDir.remove(direction)  # remove the used direction
#
#                 # if available, take it
#                 if not nodeMap[godel(newNode[0], newNode[1])]:
#
#                     nodeMap[newNode] = 1  # update node_map. the new_node is now taken
#                     relationList.append([currentNode[:], newNode[:]])  # put the relation in the list
#                     currentNode[:] = newNode  # update current_node
#                     # direction unchanged
#                     found = 1
#                     # pass
#
#                 # otherwise, try other directions
#                 else:
#                     # try every other direction until find an empty one
#                     for dir in allDir:
#                         newNode = [currentNode[0] + dir[0], currentNode[1] + dir[1]]  # try a new spot
#
#                         # Got a empty spot. Take it
#                         if not nodeMap[godel(newNode[0], newNode[1])]:
#                             nodeMap[newNode] = 1  # update node_map. the new_node is now taken
#                             relationList.append([currentNode[:], newNode[:]])  # put the relation in the list
#                             currentNode[:] = newNode  # update current_node
#                             direction[:] = dir  # update the preferred direction
#                             found = 1
#                             break
#
#                 # TODO: Cannot find an empty spot
#                 # if (found == 0):
#                 pass
#
#             def recursive_node_mapping(self, obj, current_node_pos, direction, node_map, relation_list):
#                 # TODO: paramters' value can be defaulted to None. Then check if None, assign to predefined values. Otherwise, assign to the passed in values
#
#                 # if the object is a dictionary, then it contains its one nodeId, and its one subconnection list
#                 if isinstance(obj, dict):
#                     # direct neighbour of the current_node
#                     neighbourNodeId = obj["nodeId"]
#                     # find empty position in node_mapping, update current_node, update direction, update relation_list
#                     self.find_empty_position(neighbourNodeId, current_node_pos, direction, node_map, relation_list)
#                     # print (neighbourNodeId)
#
#                     # go into the node's subconnections
#                     for item in obj["subs"]:
#                         self.recursive_node_mapping(item, current_node_pos[:], direction, node_map, relation_list)
#
#                 # if the object is a list, then it is a list of dictionaries
#                 elif isinstance(obj, list):
#                     for item in obj:
#                         self.recursive_node_mapping(item, current_node_pos[:], direction, node_map, relation_list)
#                         # else:
#                         #     return obj
#                         # print (obj)


def recursive_node_mapping(obj, currentNodeId, graph):
    #TODO: paramters' value can be defaulted to None. Check if None, then assign predefined values. Otherwise, assign the passed in values

    # if the object is a dictionary, then it contains a "nodeId", and its "subs" subconnection list
    if isinstance(obj, dict):
        # direct neighbour of the current_node
        neighbourNodeId = obj["nodeId"]

        #find empty position in node_mapping, update current_node, update direction, update relation_list
        #self.find_empty_position(neighbourNodeId, current_node_pos, direction, node_map, relation_list)

        print(neighbourNodeId)
        graph.add_edge(currentNodeId, neighbourNodeId)

        subsX = len(obj) #["subs"]

        # go into the node's subconnections
        if (subsX > 1):
            for item in obj["subs"]:
                recursive_node_mapping(item, neighbourNodeId, graph)


    # if the object is a list, then it is a list of dictionaries
    elif isinstance(obj, list):
        for item in obj:
            recursive_node_mapping(item, currentNodeId, graph)
    # else:
    #     return obj
        #print (obj)

meshTopo = """[
    {
        "nodeId" : 2147321731,
        "subs" : [
            {
                "nodeId" : 2147319552,
                "subs" : [
                ]
            }
        ]
    },
    {
        "nodeId" : 2142436483,
        "subs" : [
            {
                "nodeId" : 2787708644,
                "subs" : [
                ]
            }
        ]
    },
    {
        "nodeId" : 2142436495,
        "subs" : [
            {
                "nodeId" : 2787708676,
                "subs" : [
                    {
                        "nodeId" : 2142436497,
                        "subs" : [   
                        ]
                    },
                    {
                        "nodeId" : 2787708620,
                        "subs" : [
                        ]
                    }
                ]
            }
        ]
    }
]"""
meshTopo2 = """[
    {
        "nodeId" : 2147321731,
        "subs" : [
            {
                "nodeId" : 2147319552,
                "subs" : [
                ]
            }
        ]
    },
    {
        "nodeId" : 2142436483,
        "subs" : [
            {
                "nodeId" : 2787708644,
                "subs" : [
                ]
            }
        ]
    },
    {
        "nodeId" : 2142436495,
        "subs" : [
            {
                "nodeId" : 2787708676,
                "subs" : [
                    {
                        "nodeId" : 2142436497,
                        "subs" : [   
                        ]
                    },
                    {
                        "nodeId" : 2787708620,
                        "subs" : [
                        ]
                    }
                ]
            }
        ]
    },
    {
        "nodeId" : 5142436495,
        "subs" : [
            {
                "nodeId" : 6787708676,
                "subs" : [
                    {
                        "nodeId" : 7142436497,
                        "subs" : [   
                        ]
                    },
                    {
                        "nodeId" : 8787708620,
                        "subs" : [
                        ]
                    }
                ]
            }
        ]
    },
    {
        "nodeId" : 9142436495,
        "subs" : [
            {
                "nodeId" : 1787708676,
                "subs" : [
                    {
                        "nodeId" : 3142436497,
                        "subs" : [   
                        ]
                    },
                    {
                        "nodeId" : 3787708620,
                        "subs" : [
                        ]
                    }
                ]
            }
        ]
    }
]"""
jsonString = json.loads(meshTopo2)


# graph = nx.Graph()
# recursive_node_mapping(jsonString, 2323, graph)

# fixed_positions = {2323:(0,0)}
# fixed_nodes = fixed_positions.keys()
# pos = nx.spring_layout(graph, pos=fixed_positions, fixed=fixed_nodes, center=(0,0))
#pos = nx.random_layout(graph, center=(1,1))

#nx.draw_random(graph, pos=pos, with_labels=True)
# nx.draw(graph, with_labels=True)
#
# plt.show()


# nodeMapping = NodeMapping()

# serialObj = nodeMapping.init_serial()
# while True:
#     jsonString = serialObj.read_json_string()
#     if jsonString != None:
#         print (jsonString)
#         break
#     time.sleep(0.5)
#
# #nodeMapping.recursive_node_mapping(data, init_node, init_direction, node_map, relation_list)
#jsonString = json.loads(data)

# nodeMapping.recursive_node_mapping(jsonString, init_node, init_direction, node_map, relation_list)
# print (relation_list)
# print (node_map)
