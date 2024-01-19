import random

class DeviceNameGenerator:
    def __init__(self):
        self.adjectives = ['Quantum', 'Nano', 'Cyber', 'Plasma', 'Neural', 'FiberWave', 'ElectroPulse', 'SpeedForce', 'ArrowTech', 'Cybernetic']
        self.nouns = ['Router', 'Firewall', 'Mobile', 'Tablet', 'PC', 'Laptop', 'Server', 'NAS', 'Cluster', 'GPU']

        # Marvel and DC characters
        self.marvel_characters = ['Stark', 'Wakanda', 'Webcrawler', 'Xandarian', 'Gamma', 'Jarvis', 'Sentinel', 'Mjolnir', 'BlackWidow']
        self.dc_characters = ['Krypton', 'BatSignal', 'ArrowTech', 'SpeedForce', 'Cybernetic', 'LanternGuard']

    def generate_device_name(self):
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        character = random.choice(self.marvel_characters + self.dc_characters)
        return f'{character} {adjective} {noun}'

def namegen():
    generator = DeviceNameGenerator()
    device_name = generator.generate_device_name()
    print(device_name)