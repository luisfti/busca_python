def sqrt_sort(arr):
    n = len(arr)
    section_size = int(math.sqrt(n))

    # Dividindo a lista em seções
    sections = [arr[i:i+section_size] for i in range(0, n, section_size)]
    
    # Ordenando cada seção usando insertion sort
    for section in sections:
        insertion_sort(section)
    
    # Mesclando as seções ordenadas
    sorted_arr = []
    while sections:
        # Encontra a maior cabeça de seção
        max_section = max(sections, key=lambda x: x[-1])
        sorted_arr.insert(0,max_section.pop())
        # Remove a seção vazia
        if not max_section:
            sections.remove(max_section)

    return sorted_arr