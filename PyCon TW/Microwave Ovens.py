class MicrowaveBase:
    def __init__(self):
        self.clock = '00:00'


class Microwave1(MicrowaveBase):
    def __init__(self):
        super().__init__()

    @property
    def time(self):
        return '_' + self.clock[1:]


class Microwave2(MicrowaveBase):
    def __init__(self):
        super().__init__()

    @property
    def time(self):
        return self.clock[:-1] + '_'


class Microwave3(MicrowaveBase):
    def __init__(self):
        super().__init__()

    @property
    def time(self):
        return self.clock


class RemoteControl:
    def __init__(self, microwave):
        self.microwave = microwave

    def set_time(self, time):
        self.microwave.clock = time

    def add_time(self, time):
        seconds = int(self.microwave.clock[:2]) * \
            60 + int(self.microwave.clock[3:])
        if seconds < 5400:
            if time[-1] == 's':
                seconds += int(time[:-1])
            else:
                seconds += int(time[:-1]) * 60
        seconds = 5400 if seconds > 5400 else seconds
        mins, secs = divmod(seconds, 60)
        mins = '0' + str(mins) if mins < 10 else str(mins)
        secs = '0' + str(secs) if secs < 10 else str(secs)
        self.microwave.clock = mins + ':' + secs

    def del_time(self, time):
        seconds = int(self.microwave.clock[:2]) * \
            60 + int(self.microwave.clock[3:])
        if seconds > 0:
            if time[-1] == 's':
                seconds -= int(time[:-1])
            else:
                seconds -= int(time[:-1]) * 60
        seconds = 0 if seconds < 0 else seconds
        mins, secs = divmod(seconds, 60)
        mins = '0' + str(mins) if mins < 10 else str(mins)
        secs = '0' + str(secs) if secs < 10 else str(secs)
        self.microwave.clock = mins + ':' + secs

    def show_time(self):
        return self.microwave.time


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
