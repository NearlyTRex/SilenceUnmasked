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
import RoomHouseFrontHallLower
import RoomHousePaintingHall
import RoomHouseSideHall1

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseDen(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseDenDoor1":
        self.RoomSpeak("That goes back to the front hall.")
      
      # Door2
      elif entity == "EntityHouseDenDoor2":
        self.RoomSpeak("It looks like it leads to another hallway.")
      
      # Door3
      elif entity == "EntityHouseDenDoor3":
        self.RoomSpeak("I imagine it leads to another hallway or something.")
      
      # Object1
      elif entity == "EntityHouseDenObject1":
        if not Globals.Flags["PICKED_UP_COURTYARD_KEY"]:
          self.RoomSpeak("It's a key of some sort.")
        else:
          self.RoomSpeak("There's some other stuff on the bar here, toothpicks and such.  Not much else seems useful.")
      
      # Object2
      elif entity == "EntityHouseDenObject2":
        self.RoomSpeak("There's a bunch of shelves, all lined with bottles of liquor.")
      
      # HidingSpot1
      elif entity == "EntityHouseDenHidingSpot1":
        self.RoomSpeak("It's a pool table, hasn't been used in a while it seems, guessing from the dust buildup.")
      
      # HidingSpot2
      elif entity == "EntityHouseDenHidingSpot2":
        self.RoomSpeak("There's some bottles and junk underneath the bar and behind the shelves.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseDenDoor1":
        app.ChangeState(RoomHouseFrontHallLower.RoomHouseFrontHallLower())
      
      # Door2
      elif entity == "EntityHouseDenDoor2":
        app.ChangeState(RoomHousePaintingHall.RoomHousePaintingHall())
      
      # Door3
      elif entity == "EntityHouseDenDoor3":
        if Globals.Flags["UNLOCKED_SIDEHALL"]:
          app.ChangeState(RoomHouseSideHall1.RoomHouseSideHall1())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectHanger":
            Globals.Flags["UNLOCKED_SIDEHALL"] = True
            self.RoomSpeak("I was able to pick the lock easily enough with the coat hanger.")
          else:
            self.RoomSpeak("The door is locked, though the lock looks pretty weak...")
      
      # Object1
      elif entity == "EntityHouseDenObject1":
        if not Globals.Flags["PICKED_UP_COURTYARD_KEY"]:
          Globals.Flags["HAVE_COURTYARD_KEY"] = True
          Globals.Flags["PICKED_UP_COURTYARD_KEY"] = True
          self.RoomSpeak("Picked up Courtyard Key.")
        else:
          self.RoomSpeak("Nothing else of value left, just some random junk on the bar.")
      
      # Object2
      elif entity == "EntityHouseDenObject2":
        self.RoomSpeak("No real time to sit down and have a drink.  I'm probably going to need my senses if I'm going to survive this!")
      
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
    Room.Room.initialize(self, RoomHouseDen(), "RoomHouseDen", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseDenDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseDenDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseDenDoor3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseDenObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseDenObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseDenHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseDenHidingSpot2"), self.EventHandler])
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
