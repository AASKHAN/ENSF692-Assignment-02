# input_processing.py
# Adeel Ahmed Salman, ENSF 692 P24
# A terminal-based application for determining a course of action based on detected obstacles.

class Sensor:

    # Constructor with default values for traffic light, pedestrian, and vehicle status
    def __init__(self, light='green', pedestrian='no', vehicle='no'):
        self.light = light # Attribute for the color of the traffic light
        self.pedestrian = pedestrian # Attribute for pedestrian presence ('yes' or 'no')
        self.vehicle = vehicle # Attribute for vehicle presence ('yes' or 'no')

    def update_status(self):
        # Method to update sensor status based on user input
        
        print("Are changes detected in the vision input? ") # Prompt for initial detection

        try:
            # Prompt user to select the type of change detected or to end the program
            change = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")

            if change not in ["0", "1", "2", "3"]:
                raise ValueError
            else:
                if change == "1": # Update traffic light status
                    input_1 = input("What change has been identified?: ")
                    if input_1 in ["green", "yellow", "red"]:
                        self.light = input_1
                    else:
                        print("Invalid vision change \n")
                elif change == "2": # Update pedestrian status
                    input_2 = input("What change has been identified?: ")
                    if input_2 in ["yes", "no"]:
                        self.pedestrian = input_2
                    else:
                        print("Invalid vision change \n")
                elif change == "3": # Update vehicle status
                    input_3 = input("What change has been identified?: ")
                    if input_3 in ["yes", "no"]:
                        self.vehicle = input_3
                    else:
                        print("Invalid vision change \n")
                elif change == "0": # End the program
                    print("\n")
        except ValueError:
            print("You must select either 0, 1, 2, 3")
            return "null"
        return change

def print_message(sensor):
    # Function to print an action message based on the current sensor status
    
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        # If the light is red or a pedestrian/vehicle is detected, print STOP
        print("\n STOP \n")
    elif sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        # If the light is yellow and no pedestrian/vehicle is detected, print Caution
        print("\n Caution \n")
    elif sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        # If the light is green and no pedestrian/vehicle is detected, print Proceed
        print("\n Proceed \n")

def main():
    # Main function to run the car vision detector processing program
    
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    vehicle_sensor = Sensor() # Create a Sensor object
    user_entry = " " # Initialize user entry variable

    while True:
        user_entry = vehicle_sensor.update_status() # Update the sensor status based on user input
        if user_entry == "0":
            break # Exit the loop if user enters 0
        elif user_entry != "null":
            print_message(vehicle_sensor) # Print the current action message
            print("Light = " + vehicle_sensor.light + ", Pedestrian = " + 
                  vehicle_sensor.pedestrian + ", Vehicle = " + vehicle_sensor.vehicle + "\n") # Print updated sensor status

if __name__ == '__main__':
    main()
