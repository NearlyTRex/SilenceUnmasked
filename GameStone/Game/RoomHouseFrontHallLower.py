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
import RoomHouseFront
import RoomHouseLivingRoom
import RoomHouseFrontHallUpper
import RoomHouseDen
import CutsceneShadowManIntro

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseFrontHallLower(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseFrontHallLowerDoor1":
        self.RoomSpeak("Behind me is the door going outside.")
      
      # Door2
      elif entity == "EntityHouseFrontHallLowerDoor2":
        self.RoomSpeak("It probably leads to the living room.")
      
      # Door3
      elif entity == "EntityHouseFrontHallLowerDoor3":
        self.RoomSpeak("Stairs leading up to second floor.")
      
      # Door4
      elif entity == "EntityHouseFrontHallLowerDoor4":
        self.RoomSpeak("A door leading to the den.")
      
      # Object1
      elif entity == "EntityHouseFrontHallLowerObject1":
        if not Globals.Flags["SEEN_SHADOWMAN_INTRO"]:
          self.RoomSpeak("It's a painting of a woman... I should take a closer look.")
        else:
          self.RoomSpeak("It's a painting of a woman...")
      
      # Object2
      elif entity == "EntityHouseFrontHallLowerObject2":
        self.RoomSpeak("I can see a door up the upstairs landing.")
      
      # HidingSpot1
      elif entity == "EntityHouseFrontHallLowerHidingSpot1":
        self.RoomSpeak("It's a coat closet.  Seems to have a bunch of really old raincoats and sportcoats.")
      
      # HidingSpot2
      elif entity == "EntityHouseFrontHallLowerHidingSpot2":
        self.RoomSpeak("Another closet.  This one seems to be filled with shoes and umbrellas...")
      
      # HidingSpot3
      elif entity == "EntityHouseFrontHallLowerHidingSpot3":
        self.RoomSpeak("There's a crawlspace beneath the stairs.  The dust looks like it's been here for quite some time...")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseFrontHallLowerDoor1":
        if not Globals.Flags["SEEN_SHADOWMAN_INTRO"]:
          self.RoomSpeak("I should take a look at that painting first...")
        else:
          app.ChangeState(RoomHouseFront.RoomHouseFront())
      
      # Door2
      elif entity == "EntityHouseFrontHallLowerDoor2":
        if not Globals.Flags["SEEN_SHADOWMAN_INTRO"]:
          self.RoomSpeak("I should take a look at that painting first...")
        else:
          if Globals.Flags["UNLOCKED_LIVINGROOM"]:
            app.ChangeState(RoomHouseLivingRoom.RoomHouseLivingRoom())
          else:
            self.RoomSpeak("The door is locked.")
      
      # Door3
      elif entity == "EntityHouseFrontHallLowerDoor3":
        if not Globals.Flags["SEEN_SHADOWMAN_INTRO"]:
          self.RoomSpeak("I should take a look at that painting first...")
        else:
          app.ChangeState(RoomHouseFrontHallUpper.RoomHouseFrontHallUpper())
      
      # Door4
      elif entity == "EntityHouseFrontHallLowerDoor4":
        if not Globals.Flags["SEEN_SHADOWMAN_INTRO"]:
          self.RoomSpeak("I should take a look at that painting first...")
        else:
          app.ChangeState(RoomHouseDen.RoomHouseDen())
      
      # Object1
      elif entity == "EntityHouseFrontHallLowerObject1":
        if not Globals.Flags["SEEN_SHADOWMAN_INTRO"]:
          app.ChangeState(CutsceneShadowManIntro.CutsceneShadowManIntro())
        else:
          self.RoomSpeak("Looking at the painting again, I notice that there's a strange bump on it... how odd.")
      
      # Object2
      elif entity == "EntityHouseFrontHallLowerObject2":
        self.RoomSpeak("It probably leads to the bedrooms upstairs, I'll have to climb the stairs first.")
      
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
    Room.Room.initialize(self, RoomHouseFrontHallLower(), "RoomHouseFrontHallLower", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerDoor3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerDoor4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerHidingSpot2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseFrontHallLowerHidingSpot3"), self.EventHandler])
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
