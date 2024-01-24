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
import RoomCaveEntrance

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomCabin(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityCabinDoor1":
        self.RoomSpeak("The door that I came from is behind me.")
      
      # Door2
      elif entity == "EntityCabinDoor2":
        self.RoomSpeak("A door to the outside, maybe it opens to the mountains and woods surrounding the estate?")
      
      # Door3
      elif entity == "EntityCabinDoor3":
        self.RoomSpeak("It seems to be a bedroom, but it's locked.")
      
      # Object1
      elif entity == "EntityCabinObject1":
        self.RoomSpeak("It's a safe, normally used for money and such things.  This one is slightly ajar...")
      
      # Object2
      elif entity == "EntityCabinObject2":
        self.RoomSpeak("There are some matches and other junk on the counter.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityCabinDoor1":
        self.RoomSpeak("I can't go back... I have to press on and get out of here!")
      
      # Door2
      elif entity == "EntityCabinDoor2":
        app.ChangeState(RoomCaveEntrance.RoomCaveEntrance())
      
      # Door3
      elif entity == "EntityCabinDoor3":
        self.RoomSpeak("I would need a key to open it.")
      
      # Object1
      elif entity == "EntityCabinObject1":
        if not Globals.Flags["PICKED_UP_DYNAMITE"]:
          Globals.Flags["HAVE_DYNAMITE"] = True
          Globals.Flags["PICKED_UP_DYNAMITE"] = True
          self.RoomSpeak("I found some dynamite inside the safe!  What would Stevens need with this?")
        else:
          self.RoomSpeak("There's nothing else of value inside the safe, not even any money...")
      
      # Object2
      elif entity == "EntityCabinObject2":
        if not Globals.Flags["PICKED_UP_MATCHES"]:
          Globals.Flags["HAVE_MATCHES"] = True
          Globals.Flags["PICKED_UP_MATCHES"] = True
          self.RoomSpeak("I picked up a book of matches.")
        else:
          self.RoomSpeak("I don't think I'll need more than one of these things.")
      
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
    Room.Room.initialize(self, RoomCabin(), "RoomCabin", "Mansion")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityCabinDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinDoor3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinObject2"), self.EventHandler])
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
