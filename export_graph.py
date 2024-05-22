def export_to_tikz(graph):
    print("Exporting graph to TikZ picture...")
    tikz_code = "\\begin{tikzpicture}\n"
    tikz_code += "\\GraphInit[vstyle=Normal]\n"
    tikz_code += "\\SetVertexNoLabel\n"
    
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if node < neighbor:
                tikz_code += f"\\Edge({node})({neighbor})\n"
    
    tikz_code += "\\end{tikzpicture}"
    
    with open("graph.tex", "w") as file:
        file.write(tikz_code)
    
    print("Graph exported to graph.tex")

