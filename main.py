import sonoff
import config
import time
from device import Device


def show_devices(devices):
    for i in range(len(devices)):
        print(" * Device " + str(i) + ":")
        print("      - Name: " + devices[i]["name"])
    print()


def select_deviceId():
    return int(input("Introduce the number of the device you want to select: "))


def show_menu():
    print()
    print("Action Menu:")
    print(" 1.- Turn on")
    print(" 2.- Turn off")
    print(" 3.- Check status (not implemented yet)")
    print(" 4.- Turn on, wait 3 seconds, turn off")
    print()
    print(" 0.- Exit")
    print()


def read_action():
    option = int(input("Introduce the option you want to perform"))
    result = "not_implemented"
    if option == 0:
        result = "exit"
    elif option == 1:
        result = "on"
    elif option == 2:
        result = "off"
    elif option == 3:
        result = "status"
    elif option == 4:
        result = "wait3"
    else:
        result = "not_implemented"
    return result


def execute(device: Device, action):
    if action != "not_implemented":
        if action == "on" or action == "off":
            device.switch(action)
        elif action == "wait3":
            device.on()
            time.sleep(3)
            device.off()
        elif action == "status":
            status = device.get_status()
            print()
            print("----------------")
            print(str(status))
            print("----------------")
            print()
            print()


s = sonoff.Sonoff(config.username, config.password, config.api_region)
devices = s.get_devices()
print("Found " + str(len(devices)) + " devices.")

end = False

while not end:
    show_devices(devices)
    device_id = select_deviceId()
    device = Device.device_from_info(s, devices[device_id])
    show_menu()
    action = read_action()
    execute(device, action)
    if action == "exit":
        end = True

