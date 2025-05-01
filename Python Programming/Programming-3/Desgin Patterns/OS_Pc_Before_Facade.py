class CPU : 
    def start (self) : 
        print("CPU start")
class Memory : 
    def load (self) : 
        print("Memory load")
class HardDrive :
    def read (self) : 
        print("HardDrive read")
        
CPU1 = CPU()
Memory1 = Memory()
HardDrive1 = HardDrive()
CPU1.start()
Memory1.load()
HardDrive1.read()