class Car:

    wheel=4 # class variable

    def __init__(self,model,year,color) :
        self.model=model  #instance variable
        self.year=year    #instance variable
        self.color=color  #instance variable

    def start(self):
        print("car started!")

car1=Car("Alto",2000,"white")

print(car1.wheel)
    