//
//  Train.h
//  Project 3 - Linked Lists
//
//  Created by Nathenael Dereb on 9/16/20.
//  Copyright © 2020 Nathenael Dereb. All rights reserved.
//

#ifndef TRAIN_H
#define TRAIN_H

#include "Route.h"
#include "Passenger.h"
#include <vector>

using namespace std;

//Global Constants
const int CAR_CAPACITY = 16; //Capacity of each car

//Cars are the nodes of the train linked list
//Each car contains passengers that will need to be removed later (for clean up)
struct Car {
public:
  // Name: Car() - Default Constructor
  // Desc - Rail node
  // Preconditions - None
  // Postconditions - Creates a new Car
  Car() : m_next(nullptr) {}

  // Name: Car(capacity and carNumber) - Overloaded Constructor
  // Desc - Rail node
  // Preconditions - Data Available
  // Postconditions - Creates a new car with a car capacity and number
  Car(int capacity, int carNumber) {
    m_capacity = capacity;
    m_carNumber = carNumber;
    m_next = nullptr;
  }

  // Name: AddPassenger(Passenger)
  // Desc - Adds a passenger to the car
  // Preconditions - Car exists
  // Postconditions - A passenger is added to the car
  void AddPassenger(Passenger* passenger) {
    m_passengers.push_back(passenger);
  }

  // Name: IsFull
  // Desc - Returns if the capacity is equal to m_passenger's size
  // Preconditions - Node exists
  // Postconditions - Returns true if full else false
  bool IsFull() {
    return int(m_passengers.size()) == m_capacity;
  }

  //Public Member variables
  int m_capacity; //Total capacity of the car
  vector<Passenger *> m_passengers; //Vector holding passengers
  int m_carNumber; //Number of the car (it's name)
  Car *m_next; //Pointer to next car
};

//Train is the main linked list of the project.
//Each train has a route and can load/unload passengers
class Train {
public:
  // Name: Train() - Overloaded Constructor
  // Desc - Creates a new train with one car and a size of one. A train is a linked list of cars
  //        The train is passed a route which is a list of stops for the train
  // Preconditions - None
  // Postconditions - Creates a new train
  Train(Route*);
  
  // Name: ~Train() - Destructor
  // Desc - Removes each car from the train and deallocates each passenger in each car.
  //        Resets each of the linked list pointers
  // Preconditions - None
  // Postconditions - Removes all cars and passengers
  ~Train();

  // Name: AddCar
  // Desc - Dynamically allocates a new car and inserts it at the end of the train.
  //        Increments m_totalCars
  // Preconditions - Train must exist
  // Postconditions - New car node inserted at end of train
  void AddCar();

  // Name: RemoveCar(Car*)
  // Desc - Removes a car from either the beginning, middle or end of train linked list
  // Preconditions - Train exists
  // Postconditions - Removes specific car (including passengers)
  // UNUSED - 3 Bonus Pts for completing if rest of project is completed
  void RemoveCar(Car*);
      
  // Name: TrainStatus
  // Desc - Displays number of cars, number of passengers, and the route details
  // Preconditions - Train is populated
  // Postconditions - Displays information at a specific location
  void TrainStatus();
  
  // Name: LoadPassengers(filename)
  // Desc - Iterates through an input file and if the name of the "start location"
  //        matches m_curLocation then creates a new passenger and has them BoardPassenger
  // **Note - If you run this twice at any stop, it will load the same people over
  //          and over again - you do not need to check for this
  // Preconditions - Valid input file with first name, last name, age, start location,
  //                 end location all comma separated with one passenger on each line
  // Postconditions - Loads all passengers at this into cars
  void LoadPassengers(string passName);

  // Name: BoardPassenger(Passenger*)
  // Desc - Checks to see if the capacity of the train has been met. If so,
  //        adds a new car and inserts the passenger in the first open car starting at the front.
  //        Also, displays name and final destination of passenger being loaded.
  // Preconditions - Passenger object already allocated and data populated. Train exists
  // Postconditions - Adds new passenger to a car from front to back
  void BoardPassenger(Passenger*);
  
  // Name: DisembarkPassenger()
  // Desc - For each passenger on the train, checks to see if they are at their final
  //        destination. If they are, the passenger is removed from the train.
  // Note - Deallocate the passenger first then you can use the m_passengers.erase command.
  // Do not remove cars that are now unnecessary based on capacity (if you
  // added a car to hold 17 passengers and one disembarks, do not remove it)
  // Preconditions - Passengers reach their destination
  // Postconditions - Passengers are removed from the m_passengers, deallocated, and erased
  void DisembarkPassengers();
  
  // Name: TravelToNextStop
  // Desc - When chosen from the menu, moves the train to the next stop. If you have
  //        reached last stop, indicate this.
  //        When at end, also recommends turning train around.
  // Preconditions - Valid train on valid route
  // Postconditions - Updates SetCurrentStop to next stop on route
  void TravelToNextStop();
  
  // Name: TurnTrainAround()
  // Desc - When chosen from the menu at the end of the route, reverses the Route by
  //        calling ReverseRoute
  // Preconditions - Valid train on valid route
  // Postconditions - The entire route is reversed and the train starts at the new front
  void TurnTrainAround();

  // Name: IsTrainFull()
  // Desc - Iterates through train to see if total number of passengers is greater
  //        than maximum capacity
  // Preconditions - Valid train on valid route
  // Postconditions - Returns true if full else false
  bool IsTrainFull();
  
private:
  Car* m_head; //Front of the train
  Route* m_route; //Route assigned to the train
  int m_totalCars; //Total cars in the train (number of nodes)
};

#endif /* TRAIN_H */
