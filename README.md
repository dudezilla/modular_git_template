# Git Repository Setup with Submodules

This project demonstrates how to automate the setup of a Git repository with submodules using a configuration file. This is useful when you want to initialize a repository and manage its dependencies through submodules programmatically.

## Prerequisites

- Python 3.x
- `git` command-line tool installed on your system
- `GitPython` library. You can install it via pip:
  ```bash
  pip install gitpython
  ```

## Configuration

The repository configuration is specified in a JSON file named `repos_config.json`. Here is an example configuration:

```json
{
    "parent_dir": "uses_db",
    "submodules": [
        {
            "url": "git@github.com:dudezilla/make_db.git",
            "path": "make_db"
        }
    ]
}
```

- `parent_dir`: Specifies the name of the directory to be created and initialized as a Git repository.
- `submodules`: List of submodules to be added to the repository. Each submodule requires:
  - `url`: Repository URL of the submodule.
  - `path`: File path relative to the `parent_dir` where the submodule will be located.

## Usage Instructions

### 1. Clone the Main Repository

Use this snippet to create an initial repository setup:

```bash

...  git clone (this repo)
Or just look at the script you can copy paste

```

### 2. Running the Script

To use the Python script to automate the process of setting up a Git repository with submodules, follow these steps:

1. **Clone or download this repository** to your local machine.

2. **Ensure `repos_config.json` is correctly configured** according to your needs.

3. **Run the script** to set up the repository and its submodules:
   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the name of your Python file if changed.

### 3. Script Functions

- **`load_config(file_path)`**: Loads the configuration from a JSON file.
- **`initialize_repo(parent_dir)`**: Creates a directory if it doesn't exist, initializes it as a Git repository.
- **`add_submodule(repo, submodule_url, submodule_path)`**: Adds a submodule to the repository.
- **`setup_git_repo_with_dependencies(config_file)`**: Loads the configuration, initializes the main repo, adds submodules, creates a README, stages changes, and commits to the repository.

## Output

Once completed, the script will:
- Create a main repository directory.
- Add defined submodules.
- Generate a `README.md` file listing all the submodules.
- Commit all changes with an initial commit message.

You'll see the following message upon successful completion:

```plaintext
Repository setup complete. You can clone it using:
git clone --recurse-submodules <repository-url>
```

## License

Feel free to use and modify this script as needed. Contributions are welcome!
