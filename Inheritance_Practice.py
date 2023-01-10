
#This is the parent class.
class Vehicle:
    Engine_Type = 'V8 Engine'
    Steering_System = 'Steering Wheel'
    Braking_System = 'Brake Pedal'
    Number_of_Seats = 5

#This is the first child class adding on two of its own attributes.
class Airplane(Vehicle):
    Number_of_Wing_Flaps = 2
    Avionics_Switch = 'On'

#This is the second child class adding on two of its own attributes.
class Helicopter(Vehicle):
    Number_of_Blades = 7
    Carburetor_Heat = 'Off'
    
    
    
