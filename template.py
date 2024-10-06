import os
import json
from git import Repo

def load_config(file_path):
    # Load configuration from a JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def initialize_repo(parent_dir):
    # Create a new directory and initialize it as a Git repository
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    else:
        print("What the **** is this about?")
    repo = Repo.init(parent_dir)
    return repo

def add_submodule(repo, submodule_url, submodule_path):
    # Add submodule to the repository
    repo.create_submodule(name=os.path.basename(submodule_path), path=submodule_path, url=submodule_url)

def setup_git_repo_with_dependencies(config_file):
    # Load the configuration
    config = load_config(config_file)
    parent_dir = config['parent_dir']
    submodules = config['submodules']

    # Initialize the main repository
    repo = initialize_repo(parent_dir)

    # Add each submodule based on the provided configuration
    for submodule_info in submodules:
        submodule_url = submodule_info['url']
        submodule_path = submodule_info['path']
        add_submodule(repo, submodule_url, submodule_path)
    
    # Create a README file in the main repository directory
    readme_path = os.path.join(parent_dir, 'README.md')
    with open(readme_path, 'w') as f:
        f.write("# Main Repo\n\nThis repository includes the following submodules:\n")
        for submodule_info in submodules:
            f.write(f"- {submodule_info['path']} ({submodule_info['url']})\n")

    # Stage changes and make an initial commit
    repo.git.add(A=True)
    repo.index.commit('Initial commit with submodules')

    print("Repository setup complete. You can clone it using:")
    print("git clone --recurse-submodules <repository-url>")

# If the script is executed directly, set up the repository
if __name__ == "__main__":
    setup_git_repo_with_dependencies('repos_config.json')
