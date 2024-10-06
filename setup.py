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
    # Change directory
    subprocess.run(['cd', 'modular_git_template'], shell=True, check=True)

    # Install requirements
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], shell=True, check=True)

    # Run the template script
    subprocess.run(['python', 'template.py'], shell=True, check=True)

if __name__ == "__main__":
    activate_cmd = create_and_activate_venv()
    install_requirements_and_run_template(activate_cmd)
