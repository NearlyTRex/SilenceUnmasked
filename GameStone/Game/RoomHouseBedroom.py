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

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseBedroom(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door
      if entity == "EntityHouseBedroomDoor":
        self.RoomSpeak("That door heads back to the bedroom hall.")
      
      # Object1
      elif entity == "EntityHouseBedroomObject1":
        if not Globals.Flags["PICKED_UP_CROWBAR"]:
          self.RoomSpeak("I can see the end of something metal sticking out from the bed, I wonder what it is?")
        else:
          self.RoomSpeak("There's nothing else under there but some old boxes.")
      
      # Object2
      elif entity == "EntityHouseBedroomObject2":
        self.RoomSpeak("There's a bureau with a bunch of stuff on top.  Some lipstick and other amenities are in disarray.  Wonder if anything here could be useful.")
      
      # Object3
      elif entity == "EntityHouseBedroomObject3":
        self.RoomSpeak("It's a small nightstand, and someone left a wristwatch on top of it.")
      
      # Object4
      elif entity == "EntityHouseBedroomObject4":
        self.RoomSpeak("All I can see from this viewpoint is the storm swirling snow around outside...")
      
      # HidingSpot1
      elif entity == "EntityHouseBedroomHidingSpot1":
        self.RoomSpeak("There's quite a lot of space under the bed.  I see boxes and other junk stuffed under there.  Probably a fair share of dusty bunnies too.")
      
      # HidingSpot2
      elif entity == "EntityHouseBedroomHidingSpot2":
        self.RoomSpeak("I can see that there's some space between the wall and the bureau.  I wonder what could be back there?")
      
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door
      if entity == "EntityHouseBedroomDoor":
        app.ChangeState(RoomHouseBedHall.RoomHouseBedHall())
      
      # Object1
      elif entity == "EntityHouseBedroomObject1":
        if not Globals.Flags["PICKED_UP_CROWBAR"]:
          Globals.Flags["HAVE_CROWBAR"] = True
          Globals.Flags["PICKED_UP_CROWBAR"] = True
          self.RoomSpeak("Picked up a small crowbar.  I wonder what I could use this on?")
        else:
          self.RoomSpeak("I don't think there's anything else I could use here.")
      
      # Object2
      elif entity == "EntityHouseBedroomObject2":
        self.RoomSpeak("Not really sure that I'll need any of this stuff right now.")
      
      # Object3
      elif entity == "EntityHouseBedroomObject3":
        self.RoomSpeak("No need for it at this time.")
      
      # Object4
      elif entity == "EntityHouseBedroomObject4":
        self.RoomSpeak("I don't think I'd want to open the window, considering how cold it is outside.")
      
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
    Room.Room.initialize(self, RoomHouseBedroom(), "RoomHouseBedroom", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedroomDoor"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedroomObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedroomObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedroomObject3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedroomObject4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedroomHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedroomHidingSpot2"), self.EventHandler])
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
