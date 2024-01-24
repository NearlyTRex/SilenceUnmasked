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
import RoomAreaCar
import RoomDriveway2

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomDriveway1(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityDriveway1Door1":
        self.RoomSpeak("Back towards my wrecked car...")
      
      # Door2
      elif entity == "EntityDriveway1Door2":
        self.RoomSpeak("It looks like the path ends soon up ahead.")
      
      # Object1
      elif entity == "EntityDriveway1Object1":
        self.RoomSpeak("I can see a cabin over the hill... seems to be separate from the house I saw earlier.")
      
      # Object2
      elif entity == "EntityDriveway1Object2":
        self.RoomSpeak("There's a gate of some sort over there.  I guess this is probably the house's driveway then.")
      
      # HidingSpot1
      elif entity == "EntityDriveway1HidingSpot1":
        self.RoomSpeak("There are some rocks here, covered in snow and ice.")
      
      # HidingSpot2
      elif entity == "EntityDriveway1HidingSpot2":
        self.RoomSpeak("A big pile of snow.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityDriveway1Door1":
        app.ChangeState(RoomAreaCar.RoomAreaCar())
      
      # Door2
      elif entity == "EntityDriveway1Door2":
        app.ChangeState(RoomDriveway2.RoomDriveway2())
      
      # Object1
      elif entity == "EntityDriveway1Object1":
        self.RoomSpeak("I wonder if anyone still lives there?")
      
      # Object2
      elif entity == "EntityDriveway1Object2":
        self.RoomSpeak("I'd better find another way to get there than trudging through huge amounts of snow.")
      
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
    Room.Room.initialize(self, RoomDriveway1(), "RoomDriveway1", "Storm")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway1Door1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway1Door2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway1Object1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway1Object2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway1HidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityDriveway1HidingSpot2"), self.EventHandler])
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
