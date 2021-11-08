class HelloWorld():
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return 'Hello ' + self.name + '!' 


if __name__ == '__main__':
    myName = HelloWorld('Kang')
    print(myName)