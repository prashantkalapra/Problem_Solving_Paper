# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:39:25 2026

@author: Prashant
"""

"""
Question 1

* IPL CRICKET — Dream11 Team Builder   You are building a mini Dream11-style app for the IPL. 
Every Player has a name, team, role (Batsman/Bowler/All-rounder/Wicketkeeper), credits (float), and 
points_scored (int). A Captain earns 2× points and a Vice-Captain earns 1.5× points. The app must also track 
how many total players have been added across all teams in the fantasy league. 


* What will Do

Design a Python Player class and a Captain subclass to model the above. Include: a constructor for Player 
with all attributes, a method get_fantasy_points() that returns points_scored, override this method in Captain 
to return 2× points, a class variable total_players that increments with each object created, and a __str__ 
method that prints: 'Rohit Sharma (MI) — Batsman — 9.5 credits'. Write driver code creating 2 players and 1 
captain, print their fantasy points. 
"""

class Player:

    # Class variable (shared by all objects)
    total_players = 0

    # Constructor
    def __init__(self, name, team, role, credits, points_scored):
        self.name = name
        self.team = team
        self.role = role
        self.credits = credits
        self.points_scored = points_scored

        # Increase player count whenever an object is created
        Player.total_players += 1

    # Method to return fantasy points
    def get_fantasy_points(self):
        return self.points_scored

    # String representation of the object
    def __str__(self):
        return f"{self.name} ({self.team}) - {self.role} - {self.credits} credits"


# Captain class inherits Player class
class Captain(Player):

    # Constructor
    def __init__(self, name, team, role, credits, points_scored):

        # Call constructor of Player class
        super().__init__(name, team, role, credits, points_scored)

    # Method overriding
    # Captain gets double fantasy points
    def get_fantasy_points(self):
        return self.points_scored * 2


# Creating Player objects
p1 = Player("Virat Kohli", "RCB", "Batsman", 10.5, 80)
p2 = Player("Jasprit Bumrah", "MI", "Bowler", 9.0, 60)

# Creating Captain object
c1 = Captain("Rohit Sharma", "MI", "Batsman", 9.5, 70)

# Printing player details
print(p1)
print("Fantasy Points:", p1.get_fantasy_points())

print()

print(p2)
print("Fantasy Points:", p2.get_fantasy_points())

print()

print(c1)
print("Fantasy Points:", c1.get_fantasy_points())

print()

# Printing total number of objects created
print("Total Players:", Player.total_players)
