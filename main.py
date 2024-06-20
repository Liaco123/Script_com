from modbus_tk import LOGGER
from RobotCtrl import RobotCtrl

"""
####BEGIN DEFAULT ARGS####
{
    "ID": {
        "value":0,
        "tips": "PlanID",
        "type": "int"
    },
    "speed": {
        "value":50,
        "tips": "Speed",
        "type": "int"
    },
    "start": {
        "value":False,
        "tips": "Start",
        "type": "boolean"
    },
    "stop": {
        "value":False,
        "tips": "stop",
        "type": "boolean"
    },
    "clrFault": {
        "value":False,
        "tips": "clrFault",
        "type": "boolean"
    }

}
####END DEFAULT ARGS####
"""


class Module(RobotCtrl):
    def __init__(self, r, args):
        super().__init__()
        # self.status = MoveStatus.NONE
        self.counter = 0
        # r.setNotice("_"*50)

        self.write_bit_data = None
        self.write_dint_data = None

        self.m_planId1 = 0
        self.m_speed1 = 50
        self.m_start1 = False
        self.m_stop1 = False
        self.m_clrFault1 = False

    def read_bit(self):
        # return self._ModbusTcpProto__read_coil(0,10)
        return self._ModbusTcpProto__read_coil(0, 20)

    #     # return  self.__module__.
    # def read_bit(self):
    #     # self.status = MoveStatus.FINISHED
    #     return self.readmod()

    def read_dint(self):
        return self._ModbusTcpProto__read_register(0, 2)

    def write_bit(self, data: list):
        return self._ModbusTcpProto__write_multi_coil(0, data)

    def write_dint(self, data: list):
        return self._ModbusTcpProto__write_multi_register(16, data)

    def run(self, r, args):
        # self.status = MoveStatus.RUNNING
        # self.counter = r.getCount()

        # modbus comm with robot  read data
        # read_bit_result= self.read_bit()
        read_dint_result = self.read_dint()
        # print(f"read bit={read_bit_result}")
        LOGGER.info(f"\n\tread dint = {read_dint_result}")
        # [rustfmt::skip]
        # self.write_bit_data = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
        # self.write_dint_data=[0xABCD, 0xEF98, 0x56, 0x78, 9, 99]

        # [rustfmt::skip]
        # self.write_dint_data = [9]

        # results = []
        # for _ in range(0,len(self.write_dint_data),2):
        #     result = (self.write_dint_data[_]<<16 )+(self.write_dint_data[_+1])
        #     results.append(result)
        # LOGGER.debug(results)

        # self.write_dint_data=(1891,999)
        # write data
        # self.write_bit(self.write_bit_data)
        # print("write bit ok")
        # self.write_dint(self.write_dint_data)
        # print("wirte dint ok")

        # input 数据对应关系
        # self.i_Estop=read_bit_result[0]
        # self.i_external=read_bit_result[1]
        # self.i_programRequest=read_bit_result[2]
        # self.i_programRunning=read_bit_result[3]
        # self.i_faultSts=read_bit_result[4]
        # self.i_motorOnsts=read_bit_result[5]

        # self.i_planIdSts=read_dint_result[0]
        # self.i_paused=read_dint_result[1]

        # read args     ??读取的参数默认值？

        # self.m_planId1=args.get("ID",None)
        # self.m_speed1=args.get("speed",None)
        # self.m_start1=args.get("start",None)
        # self.m_stop1=args.get("stop",None)
        # self.m_clrFault1=args.get("clrFault",None)

        # start
        # if self.m_start1 :
        #     self.start()
        # if self.m_stop1:
        #     self.stop()
        # if self.m_clrFault1:
        #     self.reset()

        # output 数据对应
        # self.write_bit_data[0]=self.o_startProgram
        # self.write_bit_data[0]=self.o_stopProgram
        # self.write_bit_data[0]=self.o_paueProgram
        # self.write_bit_data[0]=self.o_enableMove
        # self.write_bit_data[0]=self.o_validataPlanNum
        # self.write_bit_data[0]=self.o_clrFault
        # self.write_bit_data[0]=self.o_motorOn
        # self.write_bit_data[0]=self.o_planId
        # self.write_bit_data[0]=self.o_speedRatio

        # self.write_dint_data[0]=self.m_planId1
        # self.write_dint_data[1]=self.m_speed1

        # __________ return self.status

    def cancel(self, r):
        self.counter = r.getCount()
        r.setNotice(f"cancal task -- {self.counter}")
        # self.status = MoveStatus.NONE

    def suspend(self, r):
        self.counter = r.getCount()
        r.setNotice(f"suspend task -- {self.counter}")
        # self.status = MoveStatus.SUSPENDED


if __name__ == "__main__":
    LOGGER.setLevel("INFO")
    runner = Module(" ", " ")
    # while True:
    # time.sleep(1)
    runner.run(" ", " ")
