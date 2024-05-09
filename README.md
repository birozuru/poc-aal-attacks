
## Artefact section for Virtualised Testbed Environment for Proof-of-Concept Attacks on AAL Devices 

### Prerequisites
- A Laptop Machine 16GB Ram 512GB Disk Storage
- [ VirtualBox ](https://www.virtualbox.org/wiki/Downloads) Installed
- [ RaspberryPi ](https://www.raspberrypi.com/software/raspberry-pi-desktop/) Desktop OS
- [ Kali Linux ](https://www.kali.org/get-kali/#kali-virtual-machines)  Iso
- Mosquitto client 2.0.11 ```sudo apt-get install mosquitto```

### Design of the System
The virtualized testbed environment is specifically created to enable the execution of proof-of-concept attacks on virtualized Ambient Assisted Living (AAL) devices that communicate using the MQTT protocol. The system includes emulated AAL devices, such as two MQTT publishers, one MQTT subscriber, one MQTT broker, and an attacker machine. The design strives to replicate authentic AAL device interactions and network communication within a controlled environment.

### Setup
#### Emulated Devices
1. MQTT Publishers: Two Low-powered Raspberry Pi devices are used to emulate MQTT publishers, simulating AAL devices capable of publishing data, such as heart rate and blood pressure, to the MQTT broker.
2. MQTT Subscriber: Another Raspberry Pi device emulates an MQTT subscriber, representing an AAL device capable of receiving and processing data published by the MQTT publishers.
3. MQTT Broker: A separate system running Kali Linux OS serves as the MQTT broker, facilitating message exchange between the publishers and the subscriber within the testbed environment.
4. Attacker Machine: Another system running Kali Linux OS is designated as the attacker machine, responsible for conducting proof-of-concept attacks on the emulated AAL devices and MQTT communication.

#### System Configuration
1. Install and configure MQTT broker software `mosquitto` on the designated broker machine.
         ```sudo apt update -y && sudo apt install mosquitto -y```
         ```sudo systemctl enable mosquitto```
         ```sudo systemctl start mosquitto```
         ```sudo systemctl status mosquitto```
2. Set up and configure MQTT client libraries on the Raspberry Pi devices to emulate MQTT publishers and subscriber functionalities.
         ```sudo apt update -y && sudo apt install mosquitto mosquitto-clients -y```
3. Configure network settings to enable communication between the emulated AAL devices and the MQTT broker.

#### Sequence Diagrams
The Sequence Diagrams which depict the environment setup and attack scenario designs can be found in the `Sequence Diagrams` folder.

### Test Scenario
#### Man-in-the-middle Attack Scenario
Once the environment has been setup and the mqtt publishers data is being received by the subscriber. We can then initiate the man-in-the-middle attack in the following steps.
1. Perform a full scan of the network using the nmap tool on the attacker machine 
2. Identify the mqtt port `1883` and protocol versions
3. Setup `IP_FORWARDING` on the attacker machine using `sysctl -w net.ipv4.ip_forward=1` to ensure transparency of man-in-the-middle attack to the audience
4. Perform the man-in-the-middle attack between the broker and subscriber using 
    `ettercap -Tq -i eth0 -M arp:remote //insert_broker_ip/ //insert_subscriber_ip/ -w dump.pcap
5. Produce the output of the dump.pcap to view the result using 
    `wireshark dump.pcap`

#### Denial of Service Attack Scenario
Following the same pattern as the man-in-the-middle attack with the environment setup, we can initiate the denial-of-service attack in the following steps.
1. Network scanning: Conduct a full network scan using the Nmap tool on the Kali Linux machine to identify potential targets and their open ports using:
                `nmap -sS -p- <target_IP>`
2. After scanning, the attacker discovers a MQTT service operating on port 1883 on the target machine.
3. The attacker readies themselves for the Slowloris DDOS attack by initiating the Slowloris tool from the Kali Linux machine.
4. Slowloris creates numerous HTTP connections to the MQTT service on the designated device, but it deliberately delivers HTTP headers at a sluggish pace, with the intention of prolonging the duration of these sessions.
5. Slowloris maintains connections by transmitting incomplete HTTP requests to the MQTT service, preventing its ability to process valid subscriber requests on the broker.
