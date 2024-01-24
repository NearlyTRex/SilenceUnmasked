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
import RoomHouseBack
import CutsceneStevensFinal

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomCabinFront(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityCabinFrontDoor1":
        self.RoomSpeak("A path back towards the mansion.")
      
      # Door2
      elif entity == "EntityCabinFrontDoor2":
        self.RoomSpeak("A small cabin, probably the living quarters for the caretaker.")
      
      # Object1
      elif entity == "EntityCabinFrontObject1":
        self.RoomSpeak("I can see part of the nearby mountain from over the fence.")
      
      # Object2
      elif entity == "EntityCabinFrontObject2":
        self.RoomSpeak("A lamp for the cabin's front door.")
      
      # Object3
      elif entity == "EntityCabinFrontObject3":
        self.RoomSpeak("A couple of fences partitioning off a yard for the cabin.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityCabinFrontDoor1":
        app.ChangeState(RoomHouseBack.RoomHouseBack())
      
      # Door2
      elif entity == "EntityCabinFrontDoor2":
        app.ChangeState(CutsceneStevensFinal.CutsceneStevensFinal())
      
      # Object1
      elif entity == "EntityCabinFrontObject1":
        self.RoomSpeak("No real way to get to it from here, though would I really need to?")
      
      # Object2
      elif entity == "EntityCabinFrontObject2":
        self.RoomSpeak("It seems to be busted, missing a bulb...")
      
      # Object3
      elif entity == "EntityCabinFrontObject3":
        self.RoomSpeak("There doesn't seem to be any way to get over there from here, short of climbing the fence.  Not something I really want to do right now anyway.")
      
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
    Room.Room.initialize(self, RoomCabinFront(), "RoomCabinFront", "Storm")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityCabinFrontDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinFrontDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinFrontObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinFrontObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinFrontObject3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinFrontHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityCabinFrontHidingSpot2"), self.EventHandler])
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
