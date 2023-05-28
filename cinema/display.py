import graphviz

dot_file_path = 'graph.dot'
with open(dot_file_path, 'r', encoding='utf-8') as file:
    dot_data = file.read()

graph = graphviz.Source(dot_data)

graph.render(filename='graph.png', cleanup=True)
