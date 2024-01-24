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
import RoomHouseBedHall
import RoomHouseGuestroom

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseLinen(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseLinenDoor1":
        self.RoomSpeak("It leads to the main bedroom hall, but it's permanently shut.")
      
      # Door2
      elif entity == "EntityHouseLinenDoor2":
        self.RoomSpeak("I can get back into the guest bedroom via this connecting door.")
      
      # Object1
      elif entity == "EntityHouseLinenObject1":
        self.RoomSpeak("There are some coat hangers here.")
      
      # Object2
      elif entity == "EntityHouseLinenObject2":
        self.RoomSpeak("There are various toiletries here.  Some of these hairnets look pretty filthy though...")
      
      # HidingSpot1
      elif entity == "EntityHouseLinenHidingSpot1":
        self.RoomSpeak("A cabinet full of towels, soap, and other supplies.  Surprisingly, it actually looks somewhat clean in there.")
      
      # HidingSpot2
      elif entity == "EntityHouseLinenHidingSpot2":
        self.RoomSpeak("A couple of shelves full of towels folded up... Quite a lot of space!")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseLinenDoor1":
        self.RoomSpeak("Nope, can't go through there.")
      
      # Door2
      elif entity == "EntityHouseLinenDoor2":
        app.ChangeState(RoomHouseGuestroom.RoomHouseGuestroom())
      
      # Object1
      elif entity == "EntityHouseLinenObject1":
        if not Globals.Flags["PICKED_UP_HANGER"]:
          Globals.Flags["HAVE_HANGER"] = True
          Globals.Flags["PICKED_UP_HANGER"] = True
          self.RoomSpeak("I picked up a coat hanger, might come in handy I guess.")
        else:
          self.RoomSpeak("Some more coat hangers remain, I don't need any more though.")
      
      # Object2
      elif entity == "EntityHouseLinenObject2":
        self.RoomSpeak("No need to pick up one of those at the moment, maybe in a little while.")
      
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
    Room.Room.initialize(self, RoomHouseLinen(), "RoomHouseLinen", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLinenDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLinenDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLinenObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLinenObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLinenHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLinenHidingSpot2"), self.EventHandler])
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
