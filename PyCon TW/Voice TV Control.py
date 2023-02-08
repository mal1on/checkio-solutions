class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.channel = channels[0]

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
        for c, n in zip(range(len(self.channels)), list(range(1, len(self.channels))) + [0]):
            if current == c:
                self.channel = self.channels[n]
                return self.channel

    def previous_channel(self):
        current = self.channels.index(self.channel)
        for c, p in zip(range(len(self.channels)), [-1] + list(range(len(self.channels) - 1))):
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


CHANNELS = ['BBC', 'Discovery', 'NickMusic', 'MTV']
controller = VoiceCommand(CHANNELS)
controller.next_channel()
controller.next_channel()
controller.next_channel()
controller.current_channel()
