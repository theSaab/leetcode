
graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F', 'G'],
         'D': [''],
         'E': [''],
         'F': [''],
         }

    #       A
    #    /     \
    #   B       C 
    # /   \    /  \
    # D   E   F   G

def iteration(graph, start, end):
    new_start = start
    for element in graph[new_start]:
        if element == end:
            return True
            break
        else:
            continue


def find_path(graph, start, end, path=[]):
    found = False
    path = path + [start]
    new_start = start
    if start == end:
        print(path)
        found == True

    else:
        while found == False:
            for element in graph[new_start]:
                print(str(path) + 'here')
                path = path + [element]

                if iteration(graph, new_start, end) == True:
                    path = path + [end]
                    print('good')
                    found = True
                    print(path)
                    break

                else:
                    print(str(path) + 'there')
                    path = [] + [start]
            new_start = graph[new_start][]
            # break


find_path(graph, 'A', 'F')
