import re

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def update_personal_access_token(file_path):
    file_contents = read_file(file_path)

    # Locate the authentication section
    auth_section = re.search(r'### Authentication\n\n(.+?)\n\n', file_contents, re.DOTALL)

    if auth_section:
        instructions = auth_section.group(1)
        new_token = input("Enter the new personal access token: ")

        # Replace the existing token in the instructions
        updated_instructions = instructions.replace('<existing_token>', new_token)

        # Update the configuration file
        update_configuration_file(updated_instructions, 'path/to/configuration/file')

        # Replace the existing instructions with the updated instructions
        updated_contents = file_contents.replace(instructions, updated_instructions)
        write_file(file_path, updated_contents)
        return updated_contents
    else:
        raise ValueError("Authentication section not found in the file.")

def update_configuration_file(updated_instructions, config_file_path):
    config_contents = read_file(config_file_path)

    # Replace the existing token in the configuration file
    new_config_contents = config_contents.replace('<existing_token>', updated_instructions)

    write_file(config_file_path, new_config_contents)

# Example usage
updated_file_contents = update_personal_access_token('positron-network-architect-agent/github-integration/api-interaction.md')
print(updated_file_contents)
