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
import RoomHouseFrontHallLower
import RoomHouseBedHall

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseFrontHallUpper(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseFrontHallUpperDoor1":
        self.RoomSpeak("Behind me are the stairs going back down to the front hall.")
      
      # Door2
      elif entity == "EntityHouseFrontHallUpperDoor2":
        self.RoomSpeak("There's a large door leading to the upstairs hallway.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseFrontHallUpperDoor1":
        app.ChangeState(RoomHouseFrontHallLower.RoomHouseFrontHallLower())
      
      # Door2
      elif entity == "EntityHouseFrontHallUpperDoor2":
        if Globals.Flags["UNLOCKED_BEDROOMHALL"]:
          app.ChangeState(RoomHouseBedHall.RoomHouseBedHall())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectBedroomHallKey":
            Globals.Flags["UNLOCKED_BEDROOMHALL"] = True
            self.RoomSpeak("I unlocked the door.")
          else:
            self.RoomSpeak("It's locked, I can't enter.")
      
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
    Room.Room.initialize(self, RoomHouseFrontHallUpper(), "RoomHouseFrontHallUpper", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallUpperDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallUpperDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallUpperObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallUpperObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallUpperHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallUpperHidingSpot2"), self.EventHandler])
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
