from sonoff import Sonoff


class DeviceStatus:
    """ Device status """

    def __init__(self, ip, brandName, productModel, switch):
        self.ip = ip
        self.brandName = brandName
        self.productModel = productModel
        self.switch = switch

    def get_ip(self):
        return self.ip

    def get_brandName(self):
        return self.brandName

    def get_productModel(self):
        return self.productModel

    def get_switch(self):
        return self.switch

    def __repr__(self):
        """ Unambiguous representation """
        return "Device info:\n   ip: {0}\n   brandName: {1}\n   productModel: {2}\n   switch: {3}"\
            .format(self.ip, self.brandName, self.productModel, self.switch)

    def __str__(self):
        return self.__repr__()


class Device:
    """ sonoff devices """

    def __init__(self, sonoff_ref: Sonoff, deviceid, outlet=None):
        self.sonoff_ref = sonoff_ref
        self.deviceid = deviceid
        self.outlet = outlet

    @classmethod
    def device_from_info(cls, sonoff_ref, device_info):
        deviceid = device_info['deviceid']
        device = Device(sonoff_ref, deviceid)
        return device

    def switch(self, action):
        self.sonoff_ref.switch(action, self.deviceid, self.outlet)

    def on(self):
        self.switch("on")

    def off(self):
        self.switch("off")

    def get_status(self):
        device_info = self.sonoff_ref.get_device(self.deviceid)
        ip = device_info["ip"]
        brandName = device_info["brandName"]
        productModel = device_info["productModel"]
        switch = device_info["params"]["switch"]
        status = DeviceStatus(ip, brandName, productModel, switch)
        return status
