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

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomAreaCar(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door
      if entity == "EntityAreaCarDoor":
        self.RoomSpeak("I can see a path in the snow up ahead, maybe I can follow it somewhere...")
      
      # Object1
      elif entity == "EntityAreaCarObject1":
        self.RoomSpeak("I can see a house in the distance... looks like some lights are on and it has a lit fireplace.")
      
      # Object2
      elif entity == "EntityAreaCarObject2":
        self.RoomSpeak("There are some footsteps already made in the snow... did someone see me crash my car?  Maybe it was that figure on the road!")
      
      # HidingSpot1
      elif entity == "EntityAreaCarHidingSpot1":
        self.RoomSpeak("My car, it's a complete wreck... no way I'm going to be driving with it anytime soon...")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door
      if entity == "EntityAreaCarDoor":
        app.ChangeState(RoomDriveway1.RoomDriveway1())
      
      # Object1
      elif entity == "EntityAreaCarObject1":
        self.RoomSpeak("Looks kinda spooky from this distance, but I might as well head over to it... or I could risk freezing here.")
      
      # Object2
      elif entity == "EntityAreaCarObject2":
        self.RoomSpeak("They seem to have been made by a large boot, but it's hard to tell for sure.")
      
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
    Room.Room.initialize(self, RoomAreaCar(), "RoomAreaCar", "Storm")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityAreaCarDoor"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaCarObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaCarObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaCarHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaCarHidingSpot2"), self.EventHandler])
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
