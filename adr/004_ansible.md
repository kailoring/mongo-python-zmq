# Ansible

# Status: accepted

# Context:

Ansible is an open source automation platform that is used for application configuration management, deployment, and other task automation. An application can be executed by running an Ansible playbook which is contained in a yaml file.

# Decision:

Given that Ansible and Docker compose both deal with configuration, it was relatively simple to convert the application from using Docker compose to Ansible. The configuration data had to be converted to support the new syntax and formatting.

# Consequences:

Ansible allows for complex provisioning through playbooks and executes the application with a simple command.
