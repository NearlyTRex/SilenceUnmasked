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
import RoomValley

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomCaveExit(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityCaveExitDoor1":
        self.RoomSpeak("It's a dark cave... and not somewhere I really need to go back to...")
      
      # Door2
      elif entity == "EntityCaveExitDoor2":
        self.RoomSpeak("There's a path through this valley, maybe there's a way out to the road!")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityCaveExitDoor1":
        self.RoomSpeak("I can't go back there!  He's after me and there's no place to hide!  I have to get out of here!!")
      
      # Door2
      elif entity == "EntityCaveExitDoor2":
        app.ChangeState(RoomValley.RoomValley())
      
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
    Room.Room.initialize(self, RoomCaveExit(), "RoomCaveExit", "Storm")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityCaveExitDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveExitDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveExitObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveExitObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveExitHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveExitHidingSpot2"), self.EventHandler])
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
