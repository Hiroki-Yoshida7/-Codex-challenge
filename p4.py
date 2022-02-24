import ast
from typing import List

def parse_imports(code):
    return sorted(list(parse_imports_helper(code)))

def parse_imports_helper(code: str) -> List[str]:
    # Parse python source code passed as variable code and return the list of full-qualified paths for all imported symbols, sorted in ascending lexicographic order. Ignore aliases and wildcard imports.
    tree = ast.parse(code)
    for statement in tree.body:
        if isinstance(statement, ast.Import):
            for alias in statement.names:
                yield alias.name
        elif isinstance(statement, ast.ImportFrom):
            if statement.module is None:
                continue
            for alias in statement.names:
                yield f"{statement.module}.{alias.name}"
        else:
            continue

# Examples
print(parse_imports('import os'))
print(parse_imports('import os\nfrom typing import List'))
print(parse_imports('import os\nimport concurrent.futures\nfrom os import path as renamed_path\nfrom typing import (List, Tuple)'))
print(parse_imports('import os\nimport sys\nimport pandas as pd\n\nfrom typing import NamedTuple, Optional, Callable, Any'))

assert parse_imports('import os\nimport sys\nimport pandas as pd\n\nfrom typing import NamedTuple, Optional, Callable, Any') == ['os', 'pandas', 'sys', 'typing.Any', 'typing.Callable', 'typing.NamedTuple', 'typing.Optional']
