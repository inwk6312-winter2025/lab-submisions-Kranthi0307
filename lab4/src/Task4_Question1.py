from netmiko import Netmiko
devices = [{"device_type": "cisco_ios",
          "ip": "192.168.1.101",
          "username": "student",
          "password": "Meilab123",
          "port": "22"},
          {"device_type": "cisco_ios",
          "ip": "192.168.1.102",
          "username": "student",
          "password": "Meilab123",
          "port": "22"},
          {"device_type": "cisco_ios",
          "ip": "192.168.1.103",
          "username": "student",
          "password": "Meilab123",
          "port": "22"}]

for dev in devices:
    net_connect = Netmiko(**dev)
    output = net_connect.send_command("show ip interface brief", use_textfsm=True)
    net_connect.disconnect()
    print(type(output))
    
    for interface in output:
        print(interface['interface'])