import ansible_runner

def run_ansible_playbook(playbook_path, inventory_path):
    r = ansible_runner.run(playbook=playbook_path,
                           inventory=inventory_path,
                           private_data_dir='.'
                           )
    print(f"Status: {r.status}")
    print(f"Return Code: {r.rc}")
    print(f"Stdout: {r.stdout}")

run_ansible_playbook('playbook.yml', 'inventory.ini')

