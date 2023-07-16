class Testbench:
    def __init__(self, name, desc, tests = []) -> None:
        self.name = name
        self.desc = desc
        self.tests = tests

    def __str__(self) -> str:
        return f"\n==========================================\nTESTBENCH: {self.name}\n=========================================="



class Test:
    def __init__(self, name, desc, order, func) -> None:
        self.name = name
        self.desc = desc
        self.func = func  
        self.order = order  
        
    def runTest(self):
        ret = self.func() 
        assert ret == True, f"{self.name} - {ret}"
        print(f"{self.name} - Success")

    def __str__(self) -> str:
        return f"\n----------------------------\nTEST {self.order}: {self.name}\n----------------------------"