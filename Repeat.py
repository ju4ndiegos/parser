class RepeatTimes:
    def __init__(self, times, block):
        self.times = times
        self.block = block

    def execute(self):
        for _ in range(self.times):
            self.block.execute()