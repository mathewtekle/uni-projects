//
//  Route.h
//  Project 3 - Linked Lists
//
//  Created by Nathenael Dereb on 9/9/20.
//  Copyright © 2020 Nathenael Dereb. All rights reserved.
//

#ifndef ROUTE_H
#define ROUTE_H

#include <string>
#include <fstream>
#include <iostream>
#include "Stop.cpp"
using namespace std;

//Routes are the route a train would take from stop to stop
//In this case, it is a linked lists that is made up of stops (nodes)
class Route {
public:
  // Name: Route() - Default Constructor
  // Desc - Creates a new empty route
  // Preconditions - None
  // Postconditions - Sets everything to either nullptr or 0
  Route();
  
  // Name: ~Route - Destructor
  // Desc - Removes all of the stops from the route
  // Preconditions - Route must have nodes
  // Postconditions - Route will be empty and m_head and m_tail and m_currentStop
  //                  will be nullptr and m_totalStops will be 0
  ~Route();

  // Name: LoadRoute(string)
  // Desc - Reads the route file and calls AddStop once per line. Increments m_totalStops.
  // Preconditions - Route allocated and file available
  // Postconditions - Populates route with stops. Sets m_currentStop to m_head when load completed.
  void LoadRoute(string);
  
  // Name: AddStop(string, int)
  // Desc - Allocates new stop and inserts in end of route
  // Preconditions - Route allocated and data for stop available
  // Postconditions - New stop inserted in end of route
  void AddStop(string, int);
  
  // Name: PrintRouteDetails()
  // Desc - Prints information about the next stop on the route
  // Preconditions - Route allocated and data for next stop available
  // Postconditions - Outputs data only
  void PrintRouteDetails();
  
  // Name: GetCurrentStop
  // Desc - Returns the m_currentStop
  // Preconditions - m_currentStop has been assigned
  // Postconditions - Returns the pointer
  Stop* GetCurrentStop();

  // Name: SetCurrentStop
  // Desc - Updates m_currentStop
  // Preconditions - m_currentStop is available
  // Postconditions - Updates m_currentStop as the train moves
  void SetCurrentStop(Stop*);


  // Name: ReverseRoute
  // Desc - At the end of a route, the route can be reversed (as in the train turns around)
  // Recommendations - Code this function last (dead last)
  // Preconditions - Route has been completed
  // Postconditions - Replaces old route with new reversed route.
  void ReverseRoute();
 
private:
  Stop* m_head; //Head of the route linked list
  Stop* m_tail; //End of the route linked list
  Stop* m_currentStop; //Stop of the current route
  int m_totalStops; //Total stops on the route (size of linked list)
};

#endif /* ROUTE_H */
