## Silence Unmasked
## Waterstone Productions

# Standard imports
import random

# System imports
import Application
import Objects

# Local imports
import Constants
import Globals

# State imports
import Room
import RoomHouseLivingRoom
import RoomHouseFront

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseCourtyard(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseCourtyardDoor1":
        self.RoomSpeak("It's a side entrance of the house, apparently opening into the living room.")
      
      # Door2
      elif entity == "EntityHouseCourtyardDoor2":
        self.RoomSpeak("The gate that leads to the front of the house.")
      
      # Object1
      elif entity == "EntityHouseCourtyardObject1":
        self.RoomSpeak("A boarded up window.")
      
      # Object2
      elif entity == "EntityHouseCourtyardObject2":
        self.RoomSpeak("I can see the inside is brightly lit.")
      
      # HidingSpot1
      elif entity == "EntityHouseCourtyardHidingSpot1":
        self.RoomSpeak("A gazebo, looks like it's in decent shape.")
      
      # HidingSpot2
      elif entity == "EntityHouseCourtyardHidingSpot2":
        self.RoomSpeak("There's quite a lot of space underneath the gazebo, I guess someone could use it for storage.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseCourtyardDoor1":
        app.ChangeState(RoomHouseLivingRoom.RoomHouseLivingRoom())
      
      # Door2
      elif entity == "EntityHouseCourtyardDoor2":
        app.ChangeState(RoomHouseFront.RoomHouseFront())
      
      # Object1
      elif entity == "EntityHouseCourtyardObject1":
        self.RoomSpeak("No real need to take any of the boards off.")
      
      # Object2
      elif entity == "EntityHouseCourtyardObject2":
        self.RoomSpeak("I probably should go inside instead of just looking in, it's freezing out here!")
      
      # HidingSpot
      elif entity.count("HidingSpot") > 0:
        self.RoomHide()
    
    # Clear item holding
    Globals.Flags["HOLDING_ITEM"] = False
    Globals.Flags["CURRENT_ITEM"] = ""
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
    
    # Call parent
    Room.Room.initialize(self, RoomHouseCourtyard(), "RoomHouseCourtyard", "Storm")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseCourtyardDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseCourtyardDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseCourtyardObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseCourtyardObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseCourtyardHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseCourtyardHidingSpot2"), self.EventHandler])
    self.ShowObjects()
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    Room.Room.finalize(self)
    
    # Unload objects
    self.HideObjects()
  
  ######################################################################################
  # Update
  ######################################################################################
  def update(self):
    
    # Call parent
    Room.Room.update(self)
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):
    
    # Call parent
    Room.Room.input(self)
########################################################################################
