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
import RoomHouseBedHall

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseBathroom(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door
      if entity == "EntityHouseBathroomDoor":
        self.RoomSpeak("It leads back out to the bedroom hallway.")
      
      # Object1
      elif entity == "EntityHouseBathroomObject1":
        if not Globals.Flags["PICKED_UP_BUCKET"]:
          self.RoomSpeak("Opening the cabinet, I see that it's bare except for an old rusty bucket, I wonder what it was used for?")
        else:
          self.RoomSpeak("There's nothing else here of any importance.")
      
      # Object2
      elif entity == "EntityHouseBathroomObject2":
        self.RoomSpeak("The bathroom sink.  I can smell something foul from inside the drain, and the mirror is pretty disgusting looking...")
      
      # HidingSpot1
      elif entity == "EntityHouseBathroomHidingSpot1":
        self.RoomSpeak("It's a small closet for storing towels and such.")
      
      # HidingSpot2
      elif entity == "EntityHouseBathroomHidingSpot2":
        self.RoomSpeak("An old fashioned bathtub.  It looks like it might have been cleaned for quite some time....")
      
      # HidingSpot3
      elif entity == "EntityHouseBathroomHidingSpot3":
        self.RoomSpeak("It's a hamper used, used for storing dirty linen and clothes.  Something tells me it hasn't been emptied in quite some time...")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door
      if entity == "EntityHouseBathroomDoor":
        app.ChangeState(RoomHouseBedHall.RoomHouseBedHall())
      
      # Object1
      elif entity == "EntityHouseBathroomObject1":
        if not Globals.Flags["PICKED_UP_BUCKET"]:
          Globals.Flags["HAVE_BUCKET_NONFILLED"] = True
          Globals.Flags["PICKED_UP_BUCKET"] = True
          self.RoomSpeak("I picked up a bucket.")
        else:
          self.RoomSpeak("There's nothing left inside this cabinet.")
      
      # Object2
      elif entity == "EntityHouseBathroomObject2":
        self.RoomSpeak("I don't think it would be a good idea to turn the faucet on...")
      
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
    Room.Room.initialize(self, RoomHouseBathroom(), "RoomHouseBathroom", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBathroomDoor"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBathroomObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBathroomObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBathroomHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBathroomHidingSpot2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseBathroomHidingSpot3"), self.EventHandler])
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
