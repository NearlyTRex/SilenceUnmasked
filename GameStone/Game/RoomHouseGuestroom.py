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
import RoomHouseLinen
import RoomHouseBedHall

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseGuestroom(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseGuestroomDoor1":
        self.RoomSpeak("This is a connecting door to the linen closet.")
      
      # Door2
      elif entity == "EntityHouseGuestroomDoor2":
        self.RoomSpeak("That door leads back to the bedroom hallway.")
      
      # HidingSpot1
      elif entity == "EntityHouseGuestroomHidingSpot1":
        self.RoomSpeak("Looks like there's plenty of extra space under the bed.  Probably lots of junk there... or rat droppings.")
      
      # HidingSpot2
      elif entity == "EntityHouseGuestroomHidingSpot2":
        self.RoomSpeak("Some ugly looking curtains cover the window.")
      
      # Object1
      elif entity == "EntityHouseGuestroomObject1":
        if not Globals.Flags["PICKED_UP_BATHROOM_KEY"]:
          self.RoomSpeak("I see a small key on the nightstand, I wonder what it goes to?")
        else:
          self.RoomSpeak("Nothing else of value here.")
      
      # Object2
      elif entity == "EntityHouseGuestroomObject2":
        self.RoomSpeak("A strange painting, it looks like someone cutting some vegetables, but the perspective kinda gives me the creeps...")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseGuestroomDoor1":
        app.ChangeState(RoomHouseLinen.RoomHouseLinen())
      
      # Door2
      elif entity == "EntityHouseGuestroomDoor2":
        app.ChangeState(RoomHouseBedHall.RoomHouseBedHall())
      
      # Object1
      elif entity == "EntityHouseGuestroomObject1":
        if not Globals.Flags["PICKED_UP_BATHROOM_KEY"]:
          Globals.Flags["HAVE_BATHROOM_KEY"] = True
          Globals.Flags["PICKED_UP_BATHROOM_KEY"] = True
          self.RoomSpeak("I got a bathroom key.")
        else:
          self.RoomSpeak("The rest of the stuff here is random junk.  Nothing looks important.")
      
      # Object2
      elif entity == "EntityHouseGuestroomObject2":
        self.RoomSpeak("I can't reach it, it's too high up the wall.")
      
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
    Room.Room.initialize(self, RoomHouseGuestroom(), "RoomHouseGuestroom", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGuestroomDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGuestroomDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGuestroomObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGuestroomObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGuestroomHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGuestroomHidingSpot2"), self.EventHandler])
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
