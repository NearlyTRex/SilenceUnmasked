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
import RoomHouseFrontHallUpper
import RoomHouseGuestroom
import RoomHouseLinen
import RoomHouseBathroom
import RoomHouseMusicRoom
import RoomHouseBedroom
import CutsceneFall

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseBedHall(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseBedHallDoor1":
        self.RoomSpeak("Behind me is the upper level of the front hall.")
      
      # Door2
      elif entity == "EntityHouseBedHallDoor2":
        self.RoomSpeak("It looks like a guest bedroom.")
      
      # Door3
      elif entity == "EntityHouseBedHallDoor3":
        self.RoomSpeak("It's a linen room, but it's broken and I can't enter.")
      
      # Door4
      elif entity == "EntityHouseBedHallDoor4":
        self.RoomSpeak("It looks to be another bathroom...")
      
      # Door5
      elif entity == "EntityHouseBedHallDoor5":
        self.RoomSpeak("I can hear music playing faintly on the other side, perhaps it's a music room?")
      
      # Door6
      elif entity == "EntityHouseBedHallDoor6":
        self.RoomSpeak("A bedroom door")
      
      # Door7
      elif entity == "EntityHouseBedHallDoor7":
        self.RoomSpeak("Another bedroom it would appear... though it's boarded shut.  Why are all these doors boarded up, what happened here?")
      
      # Object1
      elif entity == "EntityHouseBedHallObject1":
        self.RoomSpeak("There's a note on the floor over there... looks like it might be important, but I'm a bit weary of the wood over there... it looks weakened...")
      
      # HidingSpot1
      elif entity == "EntityHouseBedHallHidingSpot1":
        self.RoomSpeak("There's a window mostly covered by some ratty looking curtains.")
      
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseBedHallDoor1":
        app.ChangeState(RoomHouseFrontHallUpper.RoomHouseFrontHallUpper())
      
      # Door2
      elif entity == "EntityHouseBedHallDoor2":
        app.ChangeState(RoomHouseGuestroom.RoomHouseGuestroom())
      
      # Door3
      elif entity == "EntityHouseBedHallDoor3":
        self.RoomSpeak("I can't go through the door, it's broken and completely nailed shut.")
      
      # Door4
      elif entity == "EntityHouseBedHallDoor4":
        if Globals.Flags["UNLOCKED_BATHROOM"]:
          app.ChangeState(RoomHouseBathroom.RoomHouseBathroom())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectBathroomKey":
            Globals.Flags["UNLOCKED_BATHROOM"] = True
            self.RoomSpeak("It's unlocked now.")
          else:
            self.RoomSpeak("It's locked, I can't open it.")
      
      # Door5
      elif entity == "EntityHouseBedHallDoor5":
        if Globals.Flags["UNLOCKED_MUSICROOM"]:
          app.ChangeState(RoomHouseMusicRoom.RoomHouseMusicRoom())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectCrowbar":
            Globals.Flags["UNLOCKED_MUSICROOM"] = True
            self.RoomSpeak("Bracing myself, I managed to dig the crowbar behind the nailed boards and pull as hard as I could.  After a few tugs, the nails on the board over the door came loose!")
          else:
            self.RoomSpeak("The door handle seems to be nailed closed... why the heck would someone do that?")
      
      # Door6
      elif entity == "EntityHouseBedHallDoor6":
        app.ChangeState(RoomHouseBedroom.RoomHouseBedroom())
      
      # Door7
      elif entity == "EntityHouseBedHallDoor7":
        self.RoomSpeak("As much as I'd like to, I can't walk through wood and nails.  It's a no go this way.")
      
      # Object1
      elif entity == "EntityHouseBedHallObject1":
        if Globals.Flags["FALL_WARNING1"] and Globals.Flags["FALL_WARNING2"]:
          app.ChangeState(CutsceneFall.CutsceneFall())
        else:
          if not Globals.Flags["FALL_WARNING1"]:
            Globals.Flags["FALL_WARNING1"] = True
            self.RoomSpeak("I don't know... it looks very weak over there....")
          elif not Globals.Flags["FALL_WARNING2"]:
            Globals.Flags["FALL_WARNING2"] = True
            self.RoomSpeak("As much as I'd like to get the note, I don't think it's safe....")
      
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
    Room.Room.initialize(self, RoomHouseBedHall(), "RoomHouseBedHall", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallDoor3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallDoor4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallDoor5"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallDoor6"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallDoor7"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBedHallHidingSpot2"), self.EventHandler])
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
