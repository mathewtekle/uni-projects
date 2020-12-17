//
//  main.cpp
//  Project 3 - Linked Lists
//
//  Created by Nathenael Dereb on 9/9/20.
//  Copyright © 2020 Nathenael Dereb. All rights reserved.
//

#include "Train.h"
#include "Route.h"

int main() {
  const string routeFile = "proj3_routes.txt";
  const string passFile = "proj3_passengers.csv";
  Route* link = new Route();
  link->LoadRoute(routeFile);
  Train* rail = new Train(link);
  int choice = 0;
  while (choice != 6) {
    do {
      cout << "What would you like to do?" << endl;
      cout << "1. Board Passengers" << endl;
      cout << "2. Disembark Passengers" << endl;
      cout << "3. Train Details" << endl;
      cout << "4. Go to Next Stop" << endl;
      cout << "5. Turn Train Around" << endl;
      cout << "6. END" << endl;
      cin >> choice;
      if(cin.fail()){
	cout << "Please enter 1 to 6" << endl;
	cin.clear();
	cin.ignore(256,'\n');
      }
    } while (choice < 1 && choice > 6) ;
    
    switch (choice) {
    case 1:
      rail->LoadPassengers(passFile);
      break;
    case 2:
      rail->DisembarkPassengers();
      break;
    case 3:
      rail->TrainStatus();
      break;
    case 4:
      rail->TravelToNextStop();
      break;
    case 5:
      rail->TurnTrainAround();
      break;
    case 6:
      cout << "Thank you for working with the Baltimore Light Rail." << endl;
      cout << "Removing all passengers, trains, and routes" << endl;
      delete link;
      delete rail;
    default:
      break;
    }
  }
  return 0;
}
