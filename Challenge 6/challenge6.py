import collections


def topological_sort(nodes_map, nodes):
    def recursion(nodes_map, node, result, visited):
        if node in visited:
            return
        visited.append(node)
        # visited.add(node)
        if node in nodes_map:
            for c in nodes_map[node]:
                recursion(nodes_map, c, result, visited)
        result.appendleft(node)

    visited = []
    # visited = set()
    result = collections.deque()
    for node in nodes.keys():
        recursion(nodes_map, node, result, visited)
    return result


def read_from_file(file_in: str, file_out: str):
    with open(file_out, 'w+') as fo:
        with open(file_in, 'r') as fi:
            total_cases = int(fi.readline().rsplit()[0])
            for case in range(total_cases):
                M = int(fi.readline().rsplit('\n')[0])
                S = []
                for m in range(M):
                    _s = fi.readline()
                    S.append(_s.rsplit('\n')[0])
                r = main(S)
                result = f'Case #{case+1}: {r}'
                
                print(result)
                fo.write(result+'\n')
    
def main(words):
    # words = ("dad", "bad", "cab", 'cda')
    # words = ('u', 'au', 'uu')
    # words = ('ce', 'mmc')
    chars = collections.OrderedDict()
    for word in words:
        for c in word:
            chars[c] = True

    nodes_map = collections.defaultdict(list)
    for i, word in enumerate(words[:-1]):
        nxt = words[i+1]
        for a, b in zip(word, nxt):
            if a != b:
                nodes_map[a] += [b]
                break
        
    r = topological_sort(nodes_map, chars)
    return ' '.join(r)

if __name__ == "__main__":
    read_from_file('./6/submitInput.txt', './6/submitOutput.txt')