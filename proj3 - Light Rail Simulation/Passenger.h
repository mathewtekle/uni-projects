//
//  Passenger.h
//  Project 3 - Linked Lists
//
//  Created by Nathenael Dereb on 9/16/20.
//  Copyright © 2020 Nathenael Dereb. All rights reserved.
//
#ifndef PASSENGER_H
#define PASSENGER_H

#include <string>
#include <iostream>
using namespace::std;

class Passenger {
public:
  // Name: Passenger(string, int, string, string)
  // Desc - Overloaded Constructor for a passenger including name, age,
  //        start location (where they board), final destination (where they get off)
  // Preconditions - Data Available
  // Postconditions - Creates a new Passenger
  Passenger(string, int, string, string);
  // Name: GetName
  // Desc - Returns name
  // Preconditions - Data Available
  // Postconditions - Returns passenger name
  string GetName();
  // Name: GetStartLocation
  // Desc - Returns starting location
  // Preconditions - Data Available
  // Postconditions - Returns starting location
  string GetStartLocation();
  // Name: GetFinalDestination
  // Desc - Returns final location
  // Preconditions - Data Available
  // Postconditions - Returns final destination
  string GetFinalDestination();
private:
  string m_fullName; //Name of the Passenger
  int m_age; //Age of the passenger
  string m_startLocation; //Starting location (Where they get on)
  string m_finalDestination; //Final destination (where they get off)
};

#endif /* PASSENGER_H */
