import json

# Load the JSON data from the file
with open('json_files/file1.json', 'r') as f:
    data = json.load(f)

# Create a dictionary to store the filtered data
result = {}

# Loop through the data and filter it
for item in data:
    hostname = item['Hostname'].strip()
    source_ip = item['Source  ip address Mask'].strip()
    protocole = item['Protocole'].strip()
    destination_ip = item['Destination ip address Mask'].strip()
    port = item['Port']

    # If the hostname starts with "idaas", add it to the result dictionary
    #if hostname.startswith('idaas'):
    if hostname not in result:
        result[hostname] = {'ansible_host': source_ip, 'destination_ip': [], 'protocole': set()}
    result[hostname]['destination_ip'].append(f"{destination_ip} {port}")
    result[hostname]['protocole'].add(protocole)

# Output the filtered data in the desired format
for hostname, values in result.items():
    destination_ips = ','.join(values['destination_ip'])
    protocoles = ','.join(values['protocole'])
    print(f"\n{hostname} ansible_host={values['ansible_host']} destination_ip={destination_ips} protocole={protocoles}")

