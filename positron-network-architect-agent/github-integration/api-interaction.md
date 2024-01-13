import webbrowser
import yaml

CONFIG_FILE_PATH = "path/to/config.yaml"

def read_config_file():
    with open(CONFIG_FILE_PATH, "r") as file:
        config_data = yaml.safe_load(file)
    return config_data

def write_config_file(config_data):
    with open(CONFIG_FILE_PATH, "w") as file:
        yaml.dump(config_data, file)

def generate_new_token():
    # Open the GitHub website in the default web browser
    webbrowser.open("https://github.com/settings/tokens")

def update_personal_access_token():
    config_data = read_config_file()
    
    # Prompt the user to generate a new personal access token
    print("Please generate a new personal access token from the GitHub website.")
    generate_new_token()
    
    # Update the personal access token in the configuration file
    new_token = input("Enter the new personal access token: ")
    config_data["github"]["personal_access_token"] = new_token
    
    write_config_file(config_data)

# Usage example
update_personal_access_token()
