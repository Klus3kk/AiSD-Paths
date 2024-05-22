# XD
def export_to_tikz(graph, filename="graph.tex"):
    print(f"Exporting graph to {filename}...")
    tikz_code = "\\begin{tikzpicture}\n"
    tikz_code += "\\GraphInit[vstyle=Normal]\n"
    tikz_code += "\\SetVertexNoLabel\n"
    
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if node < neighbor:
                tikz_code += f"\\Edge({node})({neighbor})\n"
    
    tikz_code += "\\end{tikzpicture}"
    
    with open(filename, "w") as file:
        file.write(tikz_code)
    
    print(f"Graph exported to {filename}")
