import os
import platform
import subprocess

def create_and_activate_venv():
    # Create a virtual environment
    subprocess.run(['python', '-m', 'venv', 'venv'])

    # Activate the virtual environment
    if platform.system() == "Windows":
        activate_script = os.path.join('venv', 'Scripts', 'activate')
    else:
        activate_script = os.path.join('venv', 'bin', 'activate')

    # Activation needs to be done in shell, so we write a separate script
    if platform.system() == "Windows":
        activate_command = f'{activate_script} && '
    else:
        activate_command = f'source {activate_script} && '

    return activate_command

def install_requirements_and_run_template(activate_command):
    # Define commands to run 
    commands = [
        'cd modular_git_template',
        'pip install -r requirements.txt',
        'python template.py'
    ]
    
    # Combine activate command with other commands
    full_command = activate_command + " && ".join(commands) if activate_command else " && ".join(commands)

    # Run the combined command in new shell
    subprocess.run(full_command, shell=True, check=True)

if __name__ == "__main__":
    activate_cmd = create_and_activate_venv()
    install_requirements_and_run_template(activate_cmd)
