from Conditional import*
class Block:
    def __init__(self, block_string):
        self.block_string = block_string.strip()
        self.block_type = self.detect_block_type()

    def detect_block_type(self):
        if self.block_string.startswith("if"):
            
            return "conditional"
        elif self.block_string.startswith("while"):
            return "loop"
        elif self.block_string.startswith("repeat"):
            return "repeat_times"
        else:
            return "unknown"