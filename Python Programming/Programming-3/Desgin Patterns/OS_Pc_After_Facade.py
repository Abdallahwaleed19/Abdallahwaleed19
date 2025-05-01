class CPU : 
    def start (self) : 
        print("CPU start")
class Memory : 
    def load (self) : 
        print("Memory load")
class HardDrive :
    def read (self) : 
        print("HardDrive read")
class Facade_CPU : 
    def __init__ (self):
        self.cpu = CPU()
        self.memory = Memory()
        self.harddrive = HardDrive()
    def start_Pc (self) : 
        self.cpu.start()
        self.memory.load()
        self.harddrive.read()
Facade_CPU1 = Facade_CPU()
Facade_CPU1.start_Pc()