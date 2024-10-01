import os

# 定义项目根目录
root_dir = "Blockchain-Project-Repository"

# 定义目录结构
dirs = [
    "/docs",
    "/data/raw",
    "/data/processed",
    "/code/data_analysis",
    "/code/visualization",
    "/code/machine_learning",
    "/code/scripts",
    "/notebooks",
    "/examples",
    "/tests/unit_tests",
    "/tests/integration_tests",
    "/scripts"
]

# 定义文件结构
files = {
    "/docs/README.md": "# Project Overview",
    "/docs/CONTRIBUTING.md": "# Contribution Guidelines",
    "/docs/USER_GUIDE.md": "# User Guide",
    "/docs/PROJECT_OVERVIEW.md": "# Project Overview",
    "/docs/METHODOLOGY.md": "# Research Methodology",
    "/docs/CASE_STUDIES.md": "# Case Studies",
    "/data/DATA_SOURCES.md": "# Data Sources",
    "/notebooks/DATA_ANALYSIS.ipynb": "# Data Analysis Example Notebook",
    "/notebooks/VISUALIZATION.ipynb": "# Visualization Example Notebook",
    "/notebooks/MACHINE_LEARNING.ipynb": "# Machine Learning Example Notebook",
    "/examples/example_analysis.md": "# Example Analysis",
    "/examples/example_visualization.md": "# Example Visualization",
    "/scripts/setup.py": "# Setup Script",
    "/scripts/requirements.txt": "# List of Dependencies",
    "/.gitignore": "# Git Ignore File",
    "/LICENSE": "# License Information",
    "/README.md": "# Main Project Overview"
}

# 创建目录
for dir_path in dirs:
    os.makedirs(root_dir + dir_path, exist_ok=True)
    print(f"Created directory: {root_dir + dir_path}")

# 创建文件并写入初始内容
for file_path, content in files.items():
    full_path = root_dir + file_path
    with open(full_path, 'w') as file:
        file.write(content)
    print(f"Created file: {full_path} with initial content.")

print("Project structure created successfully.")
