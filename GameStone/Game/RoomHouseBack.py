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
import RoomHouseKitchen
import RoomCabinFront

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseBack(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseBackDoor1":
        self.RoomSpeak("That goes back into the mansion.")
      
      # Door2
      elif entity == "EntityHouseBackDoor2":
        self.RoomSpeak("I see a path in the back of the mansion, following this wall...")
      
      # Object1
      elif entity == "EntityHouseBackObject1":
        self.RoomSpeak("It's a lamp for the back door.  Seems to be working okay, giving enough light to see by.")
      
      # Object2
      elif entity == "EntityHouseBackObject2":
        self.RoomSpeak("A high stone wall surrounds the back of the property.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseBackDoor1":
        app.ChangeState(RoomHouseKitchen.RoomHouseKitchen())
      
      # Door2
      elif entity == "EntityHouseBackDoor2":
        app.ChangeState(RoomCabinFront.RoomCabinFront())
      
      # Object1
      elif entity == "EntityHouseBackObject1":
        self.RoomSpeak("I don't think it would be easy to take the bulb out or anything, not that it would be a good idea in any case.")
      
      # Object2
      elif entity == "EntityHouseBackObject2":
        self.RoomSpeak("I think I see some woods behind this, but I can't climb up it, it's way too icy and not to mention pretty high.")
      
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
    Room.Room.initialize(self, RoomHouseBack(), "RoomHouseBack", "Storm")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBackDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBackDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBackObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBackObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBackHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBackHidingSpot2"), self.EventHandler])
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
