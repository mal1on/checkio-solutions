class MicrowaveBase:
    pass

class Microwave1(MicrowaveBase):
    pass

class Microwave2(MicrowaveBase):
    pass

class Microwave3(MicrowaveBase):
    pass

class RemoteControl:
    pass




microwave_1 = Microwave1()
microwave_2 = Microwave2()
microwave_3 = Microwave3()

RemoteControl(microwave_1).show_time() == "_0:00"
RemoteControl(microwave_2).show_time() == "00:0_"
RemoteControl(microwave_3).show_time() == "00:00"    