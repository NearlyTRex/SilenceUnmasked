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
import RoomHouseSideHall1
import CutsceneDiary

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseStudy(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseStudyDoor1":
        self.RoomSpeak("That door would open to the patio, except it's been permanently closed.")
      
      # Door2
      elif entity == "EntityHouseStudyDoor2":
        self.RoomSpeak("I can get back to the side hall from there.")
      
      # Object1
      elif entity == "EntityHouseStudyObject1":
        self.RoomSpeak("Among all the other books on the shelf, there's a diary that I can see sticking out.  It's half burned and missing lots of pages...")
      
      # Object2
      elif entity == "EntityHouseStudyObject2":
        if not Globals.Flags["PICKED_UP_BIBLE"]:
          self.RoomSpeak("An extremely old looking bible is laying on the desk.  It's very tattered and the cover looks spotty.")
        else:
          self.RoomSpeak("Not much else on the desk that is of any real use it would seem...")
      
      # HidingSpot1
      elif entity == "EntityHouseStudyHidingSpot1":
        self.RoomSpeak("It's an old mahogany desk, very much an antique by now.")
      
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseStudyDoor1":
        self.RoomSpeak("It would take way too much time to take all the boards down to get through here.  I have better things to do with my time, like getting the heck outta here!")
      
      # Door2
      elif entity == "EntityHouseStudyDoor2":
        app.ChangeState(RoomHouseSideHall1.RoomHouseSideHall1())
      
      # Object1
      elif entity == "EntityHouseStudyObject1":
        if Globals.Flags["SEEN_DIARY"]:
          self.RoomSpeak("I've already seen the diary, I have no desire to read that thing again....")
        else:
          app.ChangeState(CutsceneDiary.CutsceneDiary())
      
      # Object2
      elif entity == "EntityHouseStudyObject2":
        if not Globals.Flags["PICKED_UP_BIBLE"]:
          Globals.Flags["HAVE_BIBLE"] = True
          Globals.Flags["PICKED_UP_BIBLE"] = True
          self.RoomSpeak("I picked up the bible, I guess Stevens is looking for it, I should bring it to him.  Maybe then he'll tell me what the heck is going on!")
        else:
          self.RoomSpeak("Nothing else really of value on the desk.")
      
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
    Room.Room.initialize(self, RoomHouseStudy(), "RoomHouseStudy", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseStudyDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseStudyDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseStudyObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseStudyObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseStudyHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseStudyHidingSpot2"), self.EventHandler])
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
