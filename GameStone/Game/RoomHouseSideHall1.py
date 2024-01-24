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
import RoomHouseSideHall2
import RoomHouseStudy
import RoomHousePatio
import RoomHouseDen

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseSideHall1(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseSideHall1Door1":
        self.RoomSpeak("Behind me is the other half of the side hall.")
      
      # Door2
      elif entity == "EntityHouseSideHall1Door2":
        self.RoomSpeak("It's a room of some sort...")
      
      # Door3
      elif entity == "EntityHouseSideHall1Door3":
        self.RoomSpeak("I think this is the patio door, I can smell soil of some kind coming from the other side.")
      
      # Door4
      elif entity == "EntityHouseSideHall1Door4":
        self.RoomSpeak("That leads to the den.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseSideHall1Door1":
        app.ChangeState(RoomHouseSideHall2.RoomHouseSideHall2())
      
      # Door2
      elif entity == "EntityHouseSideHall1Door2":
        if Globals.Flags["UNLOCKED_STUDY"]:
          app.ChangeState(RoomHouseStudy.RoomHouseStudy())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectStudyKey":
            Globals.Flags["UNLOCKED_STUDY"] = True
            self.RoomSpeak("The key fit!  I unlocked the door.")
          else:
            self.RoomSpeak("I'm going to need a key to unlock this.")
      
      # Door3
      elif entity == "EntityHouseSideHall1Door3":
        app.ChangeState(RoomHousePatio.RoomHousePatio())
      
      # Door4
      elif entity == "EntityHouseSideHall1Door4":
        app.ChangeState(RoomHouseDen.RoomHouseDen())
      
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
    Room.Room.initialize(self, RoomHouseSideHall1(), "RoomHouseSideHall1", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall1Door1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall1Door2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall1Door3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall1Door4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall1Object1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall1Object2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall1HidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall1HidingSpot2"), self.EventHandler])
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
