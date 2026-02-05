import time

class Budget:
    def __init__(self, max_repairs: int, max_seconds: int):
        self.max_repairs = max_repairs
        self.max_seconds = max_seconds
        self.start = time.time()
        self.repairs = 0

    def repair_used(self):
        self.repairs += 1

    def exhausted(self) -> bool:
        if self.repairs >= self.max_repairs:
            return True
        if (time.time() - self.start) > self.max_seconds:
            return True
        return False
