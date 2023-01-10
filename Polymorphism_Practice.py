
#This is the parent class.
class Language:
    def __init__(self):
        self.Origin = 'Unknown'
        self.First_Recorded_Year_of_Use = 'Unknown'

    def information(self):
        msg = '\nOrigin: {}\nFirst Recorded Year of Use: {}'.format(self.Origin,self.First_Recorded_Year_of_Use)
        return msg

    def say_hello(self):
        raise NotImplementedError('Please use the say_hello class in the child class')

    
#This is the first child class.
class French(Language):
    def __init__(self):
        super().__init__()
        self.Origin = 'France'
        self.First_Recorded_Year_of_Use = 842
    
    def say_hello(self):
        print('Bonjour')


#This is the second child class.
class Spanish(Language):
    def __init__(self):
        super().__init__()
        self.Origin = 'Iberian Peninsula'
        self.First_Recorded_Year_of_Use = 1492
    
    def say_hello(self):
        print('Hola')



if __name__ == "__main__":

    #Both of the child classes have the same function (say_hello).
    #But each langauge prints something completely different.
    french = French()
    print(french.information())
    print(french.say_hello())

    spanish = Spanish()
    print(spanish.information())
    print(spanish.say_hello())
