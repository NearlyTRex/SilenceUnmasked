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
import RoomDriveway1
import RoomHouseFront
import RoomHouseGarage

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomDriveway2(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityDriveway2Door1":
        self.RoomSpeak("That goes back down the driveway")
      
      # Door2
      elif entity == "EntityDriveway2Door2":
        self.RoomSpeak("There's a path besides the garage here that leads to the front of the house.")
      
      # Door3
      elif entity == "EntityDriveway2Door3":
        self.RoomSpeak("Apparently this is the garage door.")
      
      # Object1
      elif entity == "EntityDriveway2Object1":
        self.RoomSpeak("It's the gate for the driveway.  It's been left open in the storm, now it's just swinging in the wind...")
      
      # Object2
      elif entity == "EntityDriveway2Object2":
        self.RoomSpeak("The folding door to let cars inside.  Seems like it's been bolted closed.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityDriveway2Door1":
        app.ChangeState(RoomDriveway1.RoomDriveway1())
      
      # Door2
      elif entity == "EntityDriveway2Door2":
        app.ChangeState(RoomHouseFront.RoomHouseFront())
      
      # Door3
      elif entity == "EntityDriveway2Door3":
        if Globals.Flags["UNLOCKED_GARAGE"]:
          app.ChangeState(RoomHouseGarage.RoomHouseGarage())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectGarageKey":
            Globals.Flags["UNLOCKED_GARAGE"] = True
            self.RoomSpeak("The key fit!  It's unlocked now.")
          else:
            self.RoomSpeak("It's locked tight, I can't open it.")
      
      # Object1
      elif entity == "EntityDriveway2Object1":
        self.RoomSpeak("I guess I could close it, but there doesn't seem to be much point to it.")
      
      # Object2
      elif entity == "EntityDriveway2Object2":
        self.RoomSpeak("The bolt seems to be frozen, I don't think I'm going to be unlocking this until it warms up.")
      
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
    Room.Room.initialize(self, RoomDriveway2(), "RoomDriveway2", "Storm")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway2Door1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway2Door2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway2Door3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway2Object1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway2Object2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway2HidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway2HidingSpot2"), self.EventHandler])
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
