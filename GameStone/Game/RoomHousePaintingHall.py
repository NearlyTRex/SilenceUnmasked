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
import RoomHouseLivingRoom
import RoomHouseDen

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHousePaintingHall(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHousePaintingHallDoor1":
        self.RoomSpeak("A door leading to the living room.")
      
      # Door2
      elif entity == "EntityHousePaintingHallDoor2":
        self.RoomSpeak("This leads back to the den.")
      
      # Object1
      elif entity == "EntityHousePaintingHallObject1":
        self.RoomSpeak("It's another painting of the same woman that was in the front hall.  She looks very sad.")
      
      # Object2
      elif entity == "EntityHousePaintingHallObject2":
        self.RoomSpeak("A painting of a man, probably the owner of the house.  It looks like his name is Robert Meadows.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHousePaintingHallDoor1":
        if Globals.Flags["UNLOCKED_LIVINGROOM"]:
          app.ChangeState(RoomHouseLivingRoom.RoomHouseLivingRoom())
        else:
          self.RoomSpeak("The door is locked tight.")
      
      # Door2
      elif entity == "EntityHousePaintingHallDoor2":
        app.ChangeState(RoomHouseDen.RoomHouseDen())
      
      # Object1
      elif entity == "EntityHousePaintingHallObject1":
        if Globals.Flags["PICKED_UP_LOCKET2"]:
          self.RoomSpeak("There's not much left but a distorted painting.")
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectThinner":
            Globals.Flags["PICKED_UP_LOCKET2"] = True
            Globals.Flags["HAVE_LOCKET2"] = True
            self.RoomSpeak("I poured a bit of the thinner onto the painting.  After a few seconds, I noticed that there was a locket embedded in the frame, which was painted over!  I took the locket with me.")
          else:
            self.RoomSpeak("Odd, there's another one of those strange bumps again in the painting, this one being bigger than the other one in the main hallway...")
      
      # Object2
      elif entity == "EntityHousePaintingHallObject2":
        self.RoomSpeak("It's firmly nailed to the wall, I can't take it.")
      
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
    Room.Room.initialize(self, RoomHousePaintingHall(), "RoomHousePaintingHall", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHousePaintingHallDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePaintingHallDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePaintingHallObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePaintingHallObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePaintingHallHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePaintingHallHidingSpot2"), self.EventHandler])
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
