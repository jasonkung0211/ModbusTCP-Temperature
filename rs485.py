from pyModbusTCP.client import ModbusClient

HOST_ADDR = "192.168.8.20"
HOST_PORT = 502


class ModbusClient(ModbusClient):

    def reg_read(self, address, reg=0x0000, length=0x01):
        if address is not None:
            self.unit_id(address)
        return self.read_holding_registers(reg, length * 2)

    @staticmethod
    def reg_dump(temp=None):
        if temp is not None:
            print("Temperature:     {:.1f}".format(float(temp[0]/10)))
            print("Humidity:   {:10.1%}".format(float(temp[1] / 1000)))


if __name__ == '__main__':

    c = ModbusClient(host=HOST_ADDR, port=HOST_PORT, auto_open=True, auto_close=True, timeout=1)

    while True:
        if c.last_error() > 0:
            c.close()
            c = ModbusClient(host=HOST_ADDR, port=HOST_PORT, auto_open=True, auto_close=True, timeout=1)

        c.reg_dump(c.reg_read(address=0x01))

