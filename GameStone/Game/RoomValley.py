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
import RoomCaveExit
import RoomAreaSnowplow

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomValley(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityValleyDoor1":
        self.RoomSpeak("That goes back towards the cave exit.")
      
      # Door2
      elif entity == "EntityValleyDoor2":
        self.RoomSpeak("I think I see a vehicle in the distance!  That could be my ticket outta here!")
      
      # Object1
      elif entity == "EntityValleyObject1":
        self.RoomSpeak("There's stone all around the base of the valley.  It looks like there's quite a lot of snow perched up above too...")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityValleyDoor1":
        app.ChangeState(RoomCaveExit.RoomCaveExit())
      
      # Door2
      elif entity == "EntityValleyDoor2":
        app.ChangeState(RoomAreaSnowplow.RoomAreaSnowplow())
      
      # Object1
      elif entity == "EntityValleyObject1":
        if Globals.Flags["USED_EXPLOSIVE"]:
          self.RoomSpeak("I already set the dynamite, I have to get going before it gets set off!")
        else:
          if Globals.Flags["HOLDING_ITEM"] and ((Globals.Flags["CURRENT_ITEM"] == "ObjectDynamite") or (Globals.Flags["CURRENT_ITEM"] == "ObjectMatches")):
            Globals.Flags["USED_EXPLOSIVE"] = True
            self.RoomSpeak("I stood the stick of dynamite up against the stone, and lit it with one of the matches in the book.  It immediately started sparkling, looks like it worked!")
          else:
            self.RoomSpeak("Maybe if I could cause an avalanche somehow I could at least slow this guy down, I hope.  There's gotta be something I can use around here somewhere...")
      
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
    Room.Room.initialize(self, RoomValley(), "RoomValley", "Storm")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityValleyDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityValleyDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityValleyObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityValleyObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityValleyHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityValleyHidingSpot2"), self.EventHandler])
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
