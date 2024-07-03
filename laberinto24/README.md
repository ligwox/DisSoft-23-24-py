# Maze Game 2024
Proyecto del laberinto del curso 23-24

The code (maze.py) in this repository has been developed with the assistance of SourceGraph Cody

Initial prompt:
```
Write a python program with the next objects: Maze, Wall, Door and Room. 
The Maze object has a collection of Room objects. 
The Room object has four sides (north, east, west, south), initially each side is a Wall object. 
The Door object has two sides that might be Room objects. 
The Maze object has an operation addRoom with a Room object as parameter.
```
Decorator prompt:
```
include a new class named Decorator. This new class is subclass of MapElement
```	
Composite prompt:
```	
apply the Composite design pattern to this solution: MapElement is the Component class, Container is subclass of MapElement and Room is subclass of Container class. 
A new class Leaf is subclass of MapElement.
Decorator class is now subclass of Leaf
```
Prompt to create a maze of 4 rooms and 4 beasts
```
Duplicate the createMaze2RoomFM in Game. Change the name of the duplicated method to create4Room2BeastFM, which will create 4 rooms (Room). Room 1 connects to Room 2 by a Door in the south of Room 1. Room 1 connects to Room 3 by the east of Room 1. Room 3 connects to Room 4 by the south of Room 3. Room 2 connects to Room 4 by the east of Room 3. Also include 4 beast instances (Beast class), two aggressive mode and two lazy. The aggressive beast will be in rooms 1 and 3. Lazy beasts will be in rooms 2 and 4.
```
Prompt to correct the result:
```
Use the existing methods in Game to create aggressive and lazy beasts
```