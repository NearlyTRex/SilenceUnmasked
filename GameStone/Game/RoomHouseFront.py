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
import RoomDriveway2
import RoomHouseCourtyard
import RoomHouseFrontHallLower
import CutsceneStevensIntro

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseFront(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseFrontDoor1":
        self.RoomSpeak("The path that leads back to the driveway.")
      
      # Door2
      elif entity == "EntityHouseFrontDoor2":
        self.RoomSpeak("It looks like there's a courtyard of some sort beyond the gate.")
      
      # Door3
      elif entity == "EntityHouseFrontDoor3":
        self.RoomSpeak("The ominous looking front door of the mansion...")
      
      # HidingSpot1
      elif entity == "EntityHouseFrontHidingSpot1":
        self.RoomSpeak("The shadowy front porch of the house.  Gives the house an even spookier look.")
      
      # HidingSpot2
      elif entity == "EntityHouseFrontHidingSpot2":
        self.RoomSpeak("There's a crevice behind the staircase I can see.  I wonder if there are any animals using it as a den or something...")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseFrontDoor1":
        app.ChangeState(RoomDriveway2.RoomDriveway2())
      
      # Door2
      elif entity == "EntityHouseFrontDoor2":
        if Globals.Flags["UNLOCKED_COURTYARD"]:
          app.ChangeState(RoomHouseCourtyard.RoomHouseCourtyard())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectCourtyardKey":
            Globals.Flags["UNLOCKED_COURTYARD"] = True
            self.RoomSpeak("I unlocked the gate.")
          else:
            self.RoomSpeak("The gate is locked.")
      
      # Door3
      elif entity == "EntityHouseFrontDoor3":
        if not Globals.Flags["SEEN_STEVENS_INTRO"]:
          app.ChangeState(CutsceneStevensIntro.CutsceneStevensIntro())
        else:
          app.ChangeState(RoomHouseFrontHallLower.RoomHouseFrontHallLower())
      
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
    Room.Room.initialize(self, RoomHouseFront(), "RoomHouseFront", "Storm")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontDoor3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHidingSpot2"), self.EventHandler])
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
