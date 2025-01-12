import os

# Define the root project folder
root_folder = "emr_logic_simulation"

# Define the folder structure relative to the root
folders = [
    "docs",
    "src",
    "src/gates",
    "tests",
    "examples",
    "data/sample_results"
]

files = {
    "README.md": "# EMR Logic Simulation\n\nThis project simulates logic gates and circuits using electromagnetic radiation (EMR).",
    "LICENSE": "MIT License\n\nCopyright (c) 2025",
    "requirements.txt": "numpy\nmatplotlib\nscipy",
    ".gitignore": "__pycache__/\n.vscode/\n.DS_Store",
    "docs/overview.md": "# Project Overview\n\nDetailed explanation of the EMR Logic Simulation project.",
    "src/__init__.py": "",
    "src/main.py": "# Entry point for the EMR simulation project",
    "src/gates/__init__.py": "",
    "src/gates/and_gate.py": "# AND gate implementation",
    "src/gates/or_gate.py": "# OR gate implementation",
    "src/gates/not_gate.py": "# NOT gate implementation",
    "src/circuit.py": "# Code for circuit composition",
    "src/wave_utils.py": "# Utility functions for wave generation and analysis",
    "src/visualization.py": "# Visualization tools for simulation results",
    "tests/__init__.py": "",
    "tests/test_gates.py": "# Tests for logic gates",
    "tests/test_circuit.py": "# Tests for circuit behavior",
    "tests/test_wave_utils.py": "# Tests for wave utility functions",
    "examples/basic_gates.py": "# Example script for basic logic gates",
    "examples/passcode_validator.py": "# Example script for passcode validation",
    "examples/sequential_logic.py": "# Example script for sequential logic simulation"
}

# Create the root project folder
os.makedirs(root_folder, exist_ok=True)

# Create folders inside the root
for folder in folders:
    os.makedirs(os.path.join(root_folder, folder), exist_ok=True)

# Create files with initial content inside the root
for filepath, content in files.items():
    full_path = os.path.join(root_folder, filepath)
    with open(full_path, "w") as f:
        f.write(content)

print(f"Project structure created successfully in '{root_folder}'!")
