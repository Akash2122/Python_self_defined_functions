class PythonSelfDefinedFunctions():
    
    def __init__(self) -> None:
        pass

    def ask_and_check_numeric(self,question):
        '''Pass the Question which is excepted to be Numeric,Checks the input given by user is Numeric or not
        if it is Numeric ruturns number
        if not prints "Please gives the input only in numbers"  '''
        try:
            x = float(input(question))
            return x
        except ValueError:
            print("Please gives the input only in numbers!")
            self.ask_and_check_numeric()
  
    
                
