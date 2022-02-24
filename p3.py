from typing import Dict, Union

Tree = Dict[str, Union[str, "Tree"]]


def decompress(compressed: str, tree: Tree) -> str:
    message = []
    
    if compressed == '':
        return ''

    itr = 0
    t = tree[compressed[itr]]
    while itr < len(compressed):
        if isinstance(t, str):
            message.append(t)
            try:
                t = tree[compressed[itr+1]]
            except IndexError:
                break
        else:
            try:
                t = t[compressed[itr+1]]
            except IndexError:
                break

        itr += 1 
    
    return "".join(message)
        

# Examples
print(decompress('110100100', {'0': 'a', '1': {'0': 'n', '1': 'b'}}))
print(decompress('0111010100', {'0': {'0': 'x', '1': 'z'}, '1': 'y'}))
print(decompress('', {'0': 'a', '1': 'a'}))

