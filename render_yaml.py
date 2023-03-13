import json

# Load the JSON file
with open('json_files/file1.json', 'r') as f:
    data = json.load(f)

# Create a dictionary to store the output
output = {
    'all': {
        'children': {
            'workers': {
                'hosts': {}
            }
        }
    }
}

# Loop through each entry in the JSON file
for entry in data:
    hostname = entry['Hostname'].strip()
    ip_address = entry['Source  ip address Mask'].strip()
    dest_ip_address = entry['Destination ip address Mask'].strip()
    protocol = entry['Protocole'].strip()
    port = str(entry['Port']).strip()

    # Check if the hostname is already in the output dictionary
    if hostname in output['all']['children']['workers']['hosts']:
        # If the hostname is already in the output dictionary, add the destination IP address and port to the existing value
        output['all']['children']['workers']['hosts'][hostname]['destination_ip'] += f',{dest_ip_address} {port}'
        # Add the protocol to the existing value if it's not already there
        if protocol not in output['all']['children']['workers']['hosts'][hostname]['protocole']:
            output['all']['children']['workers']['hosts'][hostname]['protocole'] += f',{protocol}'
    else:
        # If the hostname is not in the output dictionary, add it along with the IP address and destination IP address and port
        output['all']['children']['workers']['hosts'][hostname] = {
            'ansible_host': ip_address,
            'destination_ip': f'{dest_ip_address} {port}',
            'protocole': protocol
        }

# Print the output in YAML format
import yaml
print(yaml.dump(output, default_flow_style=False))

