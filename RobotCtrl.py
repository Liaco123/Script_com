import time

from ModbusTcpProto import ModbusTcpProto


class RobotCtrl(ModbusTcpProto):
    def __init__(self):  # -> None:
        super().__init__()
        self.m_speed = 0.0
        self.m_planId = 0

        self.m_start = False
        self.m_stop = False
        self.m_clrFault = False

        self.o_startProgram = False
        self.o_stopProgram = False
        self.o_paueProgram = False
        self.o_enableMove = False
        self.o_validataPlanNum = False
        self.o_clrFault = False
        self.o_motorOn = False
        self.o_planId = 0
        self.o_speedRatio = 50

        self.i_Estop = False
        self.i_external = False
        self.i_programRequest = False
        self.i_programRunning = False
        self.i_faultSts = False
        self.i_motorOnsts = False
        self.i_planIdSts = 0
        self.i_paused = False

        self.startStep = 0
        self.startFlag = False
        self.previousMills = 0

    def start(self):
        if (
            self.m_start
            and self.i_Estop
            and self.o_motorOn
            and self.i_faultSts
            and self.i_external
            and (not self.startFlag)
        ):
            self.o_clrFault = True
            time.sleep(0.5)
            self.o_validataPlanNum = False
            self.startFlag = True
            self.startStep = 10
        if self.startStep == 10:  # transfer plan id
            if self.o_planId == self.m_planId:
                self.startStep = 20
        if self.startStep == 20:  # validata pro
            if self.i_programRequest:
                self.o_validataPlanNum = True
                self.startStep = 30
        if self.startStep == 30:  # verify paln id
            if self.i_planIdSts == self.m_planId:
                self.startStep = 40
        if self.startStep == 40:  # not in request sts
            if not self.i_programRequest:
                self.o_validataPlanNum = False
                self.startStep = 50
        if self.startStep == 50:  # start
            if not self.i_programRequest:
                self.o_startProgram = True
                self.startStep = 60
        if self.startStep == 60:
            if self.i_programRunning:
                self.o_startProgram = False
                self.startStep = 70
        if self.startStep == 70:
            pass

    def stop(self, m_stop: bool):
        if m_stop or not self.i_Estop:
            self.o_stopProgram = True
            self.o_validataPlanNum = False
            self.startFlag = False

    def reset(self, m_clrFault: bool):
        if m_clrFault:
            self.o_clrFault = True

    def motorOn(self):  # motor on robot
        if self.i_Estop and not self.i_faultSts:
            self.o_enableMove = True
            self.o_speedRatio = self.m_speed
            self.o_planId = self.o_planId
            currentMills = time.time()
            if (currentMills - self.previousMills) > 1:
                self.o_motorOn = not self.o_motorOn
                self.previousMills = currentMills

    def errorDisplay(self):
        if not self.i_Estop:
            print("error:em stop button pressed")
        if not self.i_external:
            print("not in external sts")
        if self.i_faultSts:
            print("in fault sts")
