import os
import ast
from git import Repo

REPO_PATH = "C:\\Users\\Ranjan Prainila\\Desktop\\github\\firstrepo"


def extract_imports_and_calls(file_path):
    """Extracts function calls, imports, and class inheritance from a Python file."""
    dependencies = set()

    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    for node in ast.walk(tree):
        # Detect direct imports
        if isinstance(node, ast.Import):
            for alias in node.names:
                dependencies.add(alias.name + ".py")
        elif isinstance(node, ast.ImportFrom):  
            if node.module:
                dependencies.add(node.module.replace(".", "/") + ".py")
        # Detect function calls
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                dependencies.add(node.func.attr)
            elif isinstance(node.func, ast.Name):
                dependencies.add(node.func.id)
        # Detect class inheritance
        elif isinstance(node, ast.ClassDef):
            for base in node.bases:
                if isinstance(base, ast.Name):
                    dependencies.add(base.id + ".py")

    return dependencies

def find_dependency_files(repo_path, changed_files):
    """Finds all files that the modified code depends on."""
    repo = Repo(repo_path)
    all_python_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(repo_path) 
                        for f in filenames if f.endswith(".py")]

    dependency_map = {}

    for file in all_python_files:
        dependencies = extract_imports_and_calls(file)
        dependency_map[file] = dependencies

    dependent_files = set()
    
    for changed_file in changed_files:
        for file, dependencies in dependency_map.items():
            if changed_file in dependencies:
                dependent_files.add(file)

    return list(dependent_files)

if __name__ == "__main__":
    changed_files = ["file1.py", "file2.py"]  # Use the output from `get_code_diff.py`
    dependent_files = find_dependency_files(REPO_PATH, changed_files)
    print("Dependent files:", dependent_files)
