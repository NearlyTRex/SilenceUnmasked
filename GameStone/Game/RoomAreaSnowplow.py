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
import CutsceneEnding

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomAreaSnowplow(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityAreaSnowplowDoor1":
        self.RoomSpeak("That goes back to the valley... I really should get out of here while I can though!")
      
      # Door2
      elif entity == "EntityAreaSnowplowDoor2":
        self.RoomSpeak("A snowplow!  Finally, I can get out of this nightmare!")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityAreaSnowplowDoor1":
        app.ChangeState(RoomValley.RoomValley())
      
      # Door2
      elif entity == "EntityAreaSnowplowDoor2":
        app.ChangeState(CutsceneEnding.CutsceneEnding())
      
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
    Room.Room.initialize(self, RoomAreaSnowplow(), "RoomAreaSnowplow", "Storm")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityAreaSnowplowDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaSnowplowDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaSnowplowObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaSnowplowObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaSnowplowHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityAreaSnowplowHidingSpot2"), self.EventHandler])
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
