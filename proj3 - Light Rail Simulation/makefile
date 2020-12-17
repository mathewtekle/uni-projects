CXX = g++
CXXFLAGS = -Wall

proj3: Passenger.o Train.o Route.o proj3.cpp
	$(CXX) $(CXXFLAGS) Passenger.o Train.o Route.o proj3.cpp -o proj3

Route.o: Route.h Route.cpp Stop.cpp
	$(CXX) $(CXXFLAGS) -c Route.cpp

Train.o: Train.h Train.cpp Route.o Passenger.o
	$(CXX) $(CXXFLAGS) -c Train.cpp

Passenger.o: Passenger.h Passenger.cpp 
	$(CXX) $(CXXFLAGS) -c Passenger.cpp

clean:
	rm *.o*
	rm *~ 

run:
	./proj3

val:
	valgrind ./proj3
