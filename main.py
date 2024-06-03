class User:
    _user_id_counter = 1

    def __init__(self,userName:str,userGender:str,userAge:int) -> None:
        self.user_id = User._user_id_counter
        User._user_id_counter += 1
        self.userName = userName
        self.userGender = userGender
        self.userAge = userAge
        self.ride_offered = 0
        self.ride_taken = 0

    def get_user_details(self):

        return {
            "User ID":self.user_id,
            "User Name":self.userName,
            "User Gender":self.userGender,
            "User Age": self.userAge,
            "Ride Offered":self.ride_offered,
            "Ride Taken":self.ride_taken

        }
    
    def getName(self):
        return self.userName
    
    def getUserID(self):
        return self.user_id
    
    def getUserGender(self):
        return self.userGender
    
    def getUserAge(self):
        return self.userAge
    
    def getRideOffered(self):
        return self.ride_offered
    
    def getRideTaken(self):
        return self.ride_taken
    
    def setRideOffered(self):
        self.ride_offered += 1

    def setRideTaken(self):
        self.ride_taken += 1
  
class UserList:

    def __init__(self) -> None:
        self.userList = []

    def add_user(self,user:User):
        self.userList.append(user)

    def find_user(self,userName) -> User:
        for eachUser in self.userList:
            if eachUser.getName() == userName:
                return eachUser
        
        return None
    
    def update_ride_offered(self,userName):
        for eachUser in self.userList:
            if eachUser.getName() == userName:
                eachUser.setRideOffered()

    def update_ride_taken(self,userName):
        for eachUser in self.userList:
            if eachUser.getName() == userName:
                eachUser.setRideTaken()
    
    def display_user(self):
        for eachUser in self.userList:
            print(eachUser.get_user_details())

    def print_stats(self):
        for eachUser in self.userList:
            print(eachUser.getName()+":"+ str(eachUser.getRideOffered())+" Offered "+str(eachUser.getRideTaken())+" Taken")
  
class Vehicle:

    _vehicle_id_counter = 1

    def __init__(self,user:User,vehicleName:str,vehicleNumber:str,seats:int) -> None:
        self.vehicle_id = Vehicle._vehicle_id_counter
        Vehicle._vehicle_id_counter += 1
        self.user = user
        self.vehicleName = vehicleName
        self.vehicleNumber = vehicleNumber
        self.seats = seats

    def get_vehicle_details(self):
        return {
            "Vehicle ID":self.vehicle_id,
            "User":self.user.getName(),
            "Vehicle Name":self.vehicleName,
            "Vehicle Number":self.vehicleNumber,
            "Seats":self.seats
        }
    
    def getVehicleID(self):
        return self.vehicle_id
    
    def getVehicleName(self):
        return self.vehicleName
    
    def getVehicleNumber(self):
        return self.vehicleNumber
    
    def getVehicleSeats(self):
        return self.seats
    
    def getVehicleUser(self):
        return self.user

class VehicleList:

    def __init__(self) -> None:
        self.vehicleList = []

    def add_vehicle(self,vehicle:Vehicle):
        self.vehicleList.append(vehicle)

    def find_vehicle(self,vehicleName) -> Vehicle:
        for eachVehicle in self.vehicleList:
            if eachVehicle.getVehicleName() == vehicleName:
                return eachVehicle
            
        return None
    
    def display_vehicles(self):
        for eachVehicle in self.vehicleList:
            print(eachVehicle.get_vehicle_details())
    
class Ride:

    _ride_id_counter = 1

    def __init__(self,origin,destination,vehicle:Vehicle,offeredBy:User) -> None:
        self.ride_id = Ride._ride_id_counter
        Ride._ride_id_counter += 1
        self.origin = origin
        self.destination = destination
        self.seats=vehicle.getVehicleSeats()
        self.vehicle = vehicle
        self.offeredBy = offeredBy
        self.takenBy:User = None
        self.ride_status = "New"

    def get_ride_details(self):
        return {
            "Ride ID":self.ride_id,
            "Origin":self.origin,
            "Destination":self.destination,
            "Seats":self.seats,
            "Vehicle Name":self.vehicle.getVehicleName(),
            "Offered By":self.offeredBy.getName(),
            "Taken By":None if self.takenBy is None else self.takenBy.getName() ,
            "Ride Status":self.ride_status
        }
    
    def getRideID(self):
        return self.ride_id
    
    def getOrigin(self):
        return self.origin
    
    def getDestination(self):
        return self.destination
    
    def getVehicle(self):
        return self.vehicle.getVehicleName()
    
    def getSeats(self):
        return self.seats
    
    def setTakenBy(self,user:User):
        self.takenBy = user

    def setRideStatus(self,newStatus):
        self.ride_status = newStatus
        
class RideCatalog:

    def __init__(self) -> None:
        self.offered_rides = []
        self.ongoing_rides = []
        self.completed_rides = []

    def new_ride(self,origin,destination,vehicle:Vehicle,user:User):

        ride = Ride(origin,destination,vehicle,user)
        self.offered_rides.append(ride)

    def display_offered_rides(self):
        
        for eachRide in self.offered_rides:
            print(eachRide.get_ride_details())

    def check_new_ride_possible(self,vehicle:Vehicle):
        for eachRide in self.offered_rides:
            if eachRide.getVehicle() == vehicle.getVehicleName():
                return False
            
        for eachRide in self.ongoing_rides:
            if eachRide.getVehicle() == vehicle.getVehicleName():
                return False
            
        return True


    def display_ongoing_rides(self):

        for eachRide in self.ongoing_rides:
            print(eachRide.get_ride_details())

    def display_completed_rides(self):

        for eachRide in self.completed_rides:
            print(eachRide.get_ride_details())

    def add_ongoing_ride(self,ride:Ride,takenby:User):

        selectedRide:Ride = None
        selectedRideIndex = 0

        for index, eachRide in enumerate(self.offered_rides):

            if eachRide.getRideID() == ride.getRideID():

                selectedRideIndex = index
                selectedRide = eachRide
                break

        selectedRide.setTakenBy(takenby)
        selectedRide.setRideStatus("On Going")

        self.ongoing_rides.append(selectedRide)
        self.offered_rides.pop(selectedRideIndex)

    def end_ongoing_ride(self,ride:Ride):

        selectedRide:Ride = None
        selectedRideIndex = 0

        for index, eachRide in enumerate(self.ongoing_rides):

            if eachRide.getRideID() == ride.getRideID():
                selectedRide = eachRide
                selectedRideIndex = index
                break
        
        selectedRide.setRideStatus("Completed")

        self.completed_rides.append(selectedRide)
        self.ongoing_rides.pop(selectedRideIndex)

class RideSharingApp:


    def __init__(self) -> None:
        self.userList = UserList()
        self.vehicleList = VehicleList()
        self.rideCatalog = RideCatalog()

    def onboard_user(self,userName:str,userGender:str,userAge:int):

        self.userList.add_user(User(userName,userGender,userAge))

    def add_vehicle(self,userName:str,vehicleName:str,vehicleNumber:str,seats:int):

        user = self.userList.find_user(userName=userName)
        if user is None:
            print("No User ID found. Cannot Add Vehicle")    
        else:
            self.vehicleList.add_vehicle(Vehicle(user,vehicleName,vehicleNumber,seats))
            
    def getUsers(self):
        self.userList.display_user()

    def getVehicles(self):
        self.vehicleList.display_vehicles()

    def offer_ride(self,origin,destination,vehicleName:str,userName:str):
        
        user = self.userList.find_user(userName)

        vehicleName = self.vehicleList.find_vehicle(vehicleName)

        if vehicleName is not None and user is not None and self.rideCatalog.check_new_ride_possible(vehicleName):

            self.rideCatalog.new_ride(origin,destination,vehicleName,user)

            self.userList.find_user(user.getName()).setRideOffered()


        else:
            print(user.getName()+"'s Vehicle "+vehicleName.getVehicleName()+" is already in use...")
            
    def search_ride_vacant(self,origin,destination,userName):


        selectedRide:Ride = None

        user = self.userList.find_user(userName)
        
        availableRides = [eachRide for eachRide in self.rideCatalog.offered_rides if eachRide.getOrigin() == origin and eachRide.getDestination() == destination]

        if len(availableRides) != 0:
            availableRides.sort(reverse=True,key=lambda x: x.getSeats()) 

            selectedRide = availableRides[0]

            self.rideCatalog.add_ongoing_ride(selectedRide,user)

            self.userList.find_user(user.getName()).setRideTaken()
        else:
            print("No Rides found selected Origin & Destination.....")

    def search_ride_car(self,origin,destination,userName,preferred_car:str):

        selectedRide:Ride = None
        user = self.userList.find_user(userName)
        for eachRide in self.rideCatalog.offered_rides:
            if eachRide.getVehicle() == preferred_car and eachRide.getOrigin() == origin and eachRide.getDestination() == destination:
                selectedRide = eachRide
                break

        if selectedRide:

            self.rideCatalog.add_ongoing_ride(selectedRide,user)

            self.userList.find_user(user.getName()).setRideTaken()
        else:
            print("No Rides found selected Car,Origin & Destination.....")
            
    def end_ride(self,vehicleName):
        
        selectedRide:Ride = None

        for eachRide in self.rideCatalog.ongoing_rides:
            if eachRide.getVehicle() == vehicleName:
                selectedRide = eachRide
                break
        if selectedRide:
            self.rideCatalog.end_ongoing_ride(selectedRide)
        else:
            print("No Ongoing Rides found...")

    def print_stats(self):
        self.userList.print_stats()
        
        

    def list_rides(self):
        print("--------------------------------Offered Rides-------------------------------------------------------------")
        self.rideCatalog.display_offered_rides()
        print("--------------------------------Ongoing Rides-------------------------------------------------------------")
        self.rideCatalog.display_ongoing_rides()
        print("--------------------------------Completed Rides-------------------------------------------------------------")
        self.rideCatalog.display_completed_rides()

        

        

app = RideSharingApp()
app.onboard_user("Rohan","M",29)
app.add_vehicle("Rohan","Swift","KA01-1234",3)
app.onboard_user("Shashank","M",27)
app.add_vehicle("Shashank","Baleno","KA02-1234",2)
app.onboard_user("Nadini","F",26)
app.onboard_user("Shipra","F",27)
app.add_vehicle("Shipra","Polo","KA03-1234",2)
app.add_vehicle("Shipra","Activa","KA04-1234",1)
app.onboard_user("Gaurav","M",27)
app.onboard_user("Rahul","M",35)
app.add_vehicle("Rahul","XUV","KA05-1234",5)
print("---------------------------------------------------------------------------------------------")
app.getUsers()
print("---------------------------------------------------------------------------------------------")
app.getVehicles()
print("---------------------------------------------------------------------------------------------")
app.offer_ride("Hyderbad","Bangalore","Swift","Rohan")
app.offer_ride("Bangalore","Mysore","Activa","Shipra")
app.offer_ride("Bangalore","Mysore","Polo","Shipra")
app.offer_ride("Hyderbad","Bangalore","Baleno","Shashank")
app.offer_ride("Hyderbad","Bangalore","XUV","Rahul")
app.offer_ride("Hyderbad","Pune","Swift","Rohan")
print("---------------------------------------------------------------------------------------------")
app.search_ride_vacant("Bangalore","Mysore","Nadini")
app.search_ride_car("Bangalore","Mysore","Gaurav","Activa")
app.search_ride_vacant("Mumbai","Bangalore","Shashank")
app.search_ride_car("Hyderbad","Bangalore","Rohan","Baleno")
app.search_ride_car("Hyderbad","Bangalore","Shashank","Polo")
print("---------------------------------------------------------------------------------------------")
app.end_ride("Polo")
app.end_ride("Baleno")
print("---------------------------------------------------------------------------------------------")
app.print_stats()
app.list_rides()