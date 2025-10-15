# Medical Device Inventory Management System
# This script allows users to manage a list of Medical devices.

devices = [] # List to store device information

# Functions
# Function to add a new device
def add_device(name, brand, year):
    device = {
        'name': name,
        'brand': brand,
        'year': year
    }
    devices.append(device)

# Function to list all devices
def list_devices():
    print("\nInventario actual:")
    for device in devices:
        print(f"Name: {device['name']} Brand: {device['brand']}, Year: {device['year']}")

# Function to find a device by name
def find_device(name):
    for device in devices:
        if device['name'].lower() == name.lower():
            return device
    return None

# Function to update device information
def update_device(name, brand=None, year=None):
    device = find_device(name)
    if device:
        if brand:
            device['brand'] = brand
        if year:
            device['year'] = year
        return True
    return False

# Function to remove a device by name
def remove_device(name):
    device = find_device(name)
    if device:
        devices.remove(device)
        return True
    return False

# Execution
add_device("ECG Machine", "Philips", 2020)
add_device("X-Ray Machine", "Siemens", 2018)
list_devices()
update_device("ECG Machine", year=2021)
list_devices()
found_device = find_device("X-Ray Machine")
if found_device:
    print(f"\nFound Device: Name: {found_device['name']} Brand: {found_device['brand']}, Year: {found_device['year']}")
remove_device("ECG Machine")
list_devices()
