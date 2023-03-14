import pprint

g_node = 5
g_from = [4, 5, 4, 1, 3, 4, 4]
g_to = [1, 3, 5, 5, 1, 2, 3]

g_weight = [1, 1, 8, 1, 3, 9, 5]
arr = [9, 11, 3, 2, 10]
a = 3
b = 2

adj_mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i, elem_from in enumerate(g_from):
    adj_mat[elem_from - 1][g_to[i] - 1] = g_weight[i]
    adj_mat[g_to[i] - 1][elem_from - 1] = g_weight[i]
# pprint.pprint(adj_mat)
    # print("\n")


class tree_node:
    def __init__(self,num,refuel_cost):
        self.node_number = num
        self.refuel_cost = refuel_cost
        self.child_list = []

    def add_child(self,child_name):
        self.child_list.append(child_name)

    def print(self):
        print("Node number: ",self.node_number)
        print("refuel_cost: ", self.refuel_cost)
        print("child_list: ", self.child_list)


def create_tree(adj_mat,arr):
    nodes_list = []
    for i,row in enumerate(adj_mat):
        nodes_list.append(tree_node(i+1,arr[i]))
        for idx,elem in enumerate(row):
            if elem != 0:
                nodes_list[i].add_child(idx+1)

    return(nodes_list)


def get_cost(path: list, arr: list, adj_mat: list) -> int:
    path_cost = 0
    path_dist = 0
    dist = 0
    least_refuel_cost = arr[path[0]-1]

    for i in range(len(path) - 1):

        if adj_mat[path[i]-1][path[i + 1]-1] != 0:
            if least_refuel_cost <= arr[path[i]-1]:
                dist = adj_mat[path[i]-1][path[i + 1]-1]
                path_dist += dist
                path_cost += dist * least_refuel_cost
            else:
                least_refuel_cost = arr[path[i]-1]
                dist = adj_mat[path[i] - 1][path[i + 1] - 1]
                path_dist += dist
                path_cost += dist * least_refuel_cost

            # print("index: ", i)
            # print("path_from: ", path[i])
            # print("path_to: ", path[i + 1])
            # print("dist: ", dist)
            # print("least_refuel_cost: ", least_refuel_cost)

        else:
            print("Invalid path")

    return(path_dist,path_cost)


def greedy_path_search(tree,a,b,g_node):
    path_list = []
    level_path_list = [[a]]

    # for _,elem in enumerate(tree[a-1].child_list):
    #     level_path_list.append([elem])
    # print(level_path_list)

    for i in range(g_node):
        for _,elem1 in enumerate(level_path_list):
            # print(elem1)
            for _,elem2 in enumerate(tree[elem1[-1]-1].child_list):
                # print("Appending....")
                path_list.append(elem1+[elem2])
                # print(path_list)

        level_path_list = path_list
        path_list = []
    # print(len(level_path_list))

    for idx,elem in enumerate(level_path_list):
        # print(elem)
        if elem.count(b)>0:
            # print(idx,elem)
            level_path_list.remove(elem)
            # print(elem[:elem.index(b)+1])
            path_list.append(elem[:elem.index(b)+1])
            # print("No end pt!")


    # print(path_list)
    # print(len(level_path_list))
    # print(len(path_list))

    return(path_list)

# From path list determine lowest refuel cost
def least_refuel_cost(path,arr):
    least_cost = 999999
    elem_least_cost = 0
    for i,elem in enumerate(path):
        i = i-1
        if adj_mat[path[i] - 1][path[i + 1] - 1] != 0:
            if arr[elem-1] <= least_cost:
                least_cost = arr[elem-1]
                elem_least_cost = elem
        else:
            print("Invalid path")

    return(least_cost,elem_least_cost)


if __name__ == '__main__':

    tree = create_tree(adj_mat, arr)
    path_list = greedy_path_search(tree, a, b, g_node)
    least_cost = 99999
    for elem in path_list:
        path_dist,path_cost = get_cost(elem,arr,adj_mat)
        if path_cost <= least_cost:
            # print(elem, path_cost, path_dist)
            least_cost = path_cost

    print(least_cost)


