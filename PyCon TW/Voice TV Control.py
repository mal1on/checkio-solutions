class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.channel = ''

    def first_channel(self):
        self.channel = self.channels[0]
        return self.channel

    def last_channel(self):
        self.channel = self.channels[-1]
        return self.channel

    def turn_channel(self, N):
        self.channel = self.channels[N - 1]
        return self.channel

    def next_channel(self):
        current = self.channels.index(self.channel)
        for c, n in zip(range(len(CHANNELS)), list(range(1, len(CHANNELS))) + [0]):
            if current == c:
                self.channel = self.channels[n]
                return self.channel

    def previous_channel(self):
        current = self.channels.index(self.channel)
        for c, p in zip(range(len(CHANNELS)), [-1] + list(range(len(CHANNELS) - 1))):
            if current == c:
                self.channel = self.channels[p]
                return self.channel

    def current_channel(self):
        return self.channel

    def is_exist(self, chan):
        if isinstance(chan, int):
            return 'Yes' if chan in range(1, len(self.channels) + 1) else 'No'
        else:
            return 'Yes' if chan in self.channels else 'No'                            


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = VoiceCommand(CHANNELS)

controller.first_channel() == "BBC"
print(controller.channel)
controller.last_channel() == "TV1000"
print(controller.channel)
controller.turn_channel(1) == "BBC"
print(controller.channel)
controller.next_channel() == "Discovery"
print(controller.channel)
controller.previous_channel() == "BBC"
print(controller.channel)
print(controller.current_channel()) == "BBC"
print(controller.is_exist(4)) == "No"
print(controller.is_exist("BBC")) == "Yes"
