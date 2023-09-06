class Conditional:
    def __init__(self, condition, block1, block2):
        self.condition = condition
        self.block1 = block1
        self.block2 = block2

    def execute(self):
        if self.condition:
            self.block1.execute()
        else:
            self.block2.execute()