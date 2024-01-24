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
import RoomCabin
import CutsceneShadowManFinal

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomCaveEntrance(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityCaveEntranceDoor1":
        self.RoomSpeak("A dark and ominous looking cave, but I have no choice but to follow it and find a way out of here...")
      
      # Door2
      elif entity == "EntityCaveEntranceDoor2":
        self.RoomSpeak("Stevens cabin.  Do I really need to go back there?")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityCaveEntranceDoor1":
        app.ChangeState(CutsceneShadowManFinal.CutsceneShadowManFinal())
      
      # Door2
      elif entity == "EntityCaveEntranceDoor2":
        app.ChangeState(RoomCabin.RoomCabin())
      
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
    Room.Room.initialize(self, RoomCaveEntrance(), "RoomCaveEntrance", "Storm")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityCaveEntranceDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveEntranceDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveEntranceObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveEntranceObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveEntranceHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCaveEntranceHidingSpot2"), self.EventHandler])
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
