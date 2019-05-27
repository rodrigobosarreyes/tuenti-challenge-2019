# Author: Rodrigo Bosarreyes
class Map(object):
    def __init__(self, planets: int):
        self.planets = planets
        self.graph = dict()
        self.num_paths = 0
        
    def add_planet(self, start, end):
        if start not in self.graph:
            self.graph[start] = list()
        
        self.graph[start].append(end)
        
    def _calc_all_paths(self, start, end, visited, path):
        
        visited[start] = True
        path.append(start)
        
        for i in self.graph[start]:
            if i not in visited or i is end:
                self.num_paths += 1
                continue
            if not visited[i]:
                self._calc_all_paths(i, end, visited, path)
                
        path.pop()
        visited[start] = False
        
        
    def calc_all_paths(self, source, destiny):
        path = list()
        
        values = [False] * (self.planets - 1)
        keys = self.graph.keys()
        visited = dict(zip(keys, values))
        
        self._calc_all_paths(source, destiny, visited, path)
        
    
def read_from_file(file_input: str, file_output: str):
    with open(file_output, 'w+') as fo:
        with open(file_input, 'r') as fi:
            total_cases = int(fi.readline().rsplit()[0])
            for case in range(total_cases):
                planets = int(fi.readline().rsplit()[0])
                graph = Map(planets)
                start = "Galactica"
                destiny = "New Earth"
                for planet in range(planets):
                    line = fi.readline().rsplit('\n')[0].split(':')
                    s = line[0]
                    paths = line[1].split(',')
                    for p in paths:
                        graph.add_planet(s, p)
                        
                graph.calc_all_paths(start, destiny)
                result = f'Case #{case+1}: {graph.num_paths}'
                print(result)
                fo.write(result+'\n')
                
                graph = None
        
        
if __name__ == "__main__":
    # g = Graph(7)
    # g.add_node("Galactica", "A")
    # g.add_node("Galactica", "B")
    # g.add_node("Galactica", "C")
    # g.add_node("A", "E")
    # g.add_node("A", "D")
    # g.add_node("B", "D")
    # g.add_node("C", "D")
    # g.add_node("C", "F")
    # g.add_node("D", "F")
    # g.add_node("E", "New Earth")
    # g.add_node("F", "New Earth")
    
    # s = "Galactica"
    # d = "New Earth"
    
    # g.calc_all_paths(s, d)
    # print(g.num_paths)
    read_from_file('./2/submitInput', './2/submitOutput.txt')