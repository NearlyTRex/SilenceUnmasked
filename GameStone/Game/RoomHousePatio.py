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

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHousePatio(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHousePatioDoor1":
        self.RoomSpeak("I can get to the side hall from here.")
      
      # Door2
      elif entity == "EntityHousePatioDoor2":
        self.RoomSpeak("Another boarded up door... ")
      
      # Object1
      elif entity == "EntityHousePatioObject1":
        self.RoomSpeak("A couple of cans of gasoline are sitting on the floor...")
      
      # Object2
      elif entity == "EntityHousePatioObject2":
        self.RoomSpeak("Some dead plants are here, looks like no one bothered to water them.")
      
      # Object3
      elif entity == "EntityHousePatioObject3":
        self.RoomSpeak("A boarded up window is all that is left of what might have been a nice patio.")
      
      # HidingSpot1
      elif entity == "EntityHousePatioHidingSpot1":
        self.RoomSpeak("A nice looking wooden table sits here, with some cups and other assortments on top.  It's a pity that it's surrounded by such disgusting surroundings.")
      
      # HidingSpot2
      elif entity == "EntityHousePatioHidingSpot2":
        self.RoomSpeak("A large birdcage sits on top of a table.  Looks like no birds have been in there for a while.")
      
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHousePatioDoor1":
        app.ChangeState(RoomHouseSideHall1.RoomHouseSideHall1())
      
      # Door2
      elif entity == "EntityHousePatioDoor2":
        self.RoomSpeak("Last time I checked, I couldn't open doors that were nailed shut.")
      
      # Object1
      elif entity == "EntityHousePatioObject1":
        if not Globals.Flags["PICKED_UP_GASCAN"]:
          Globals.Flags["HAVE_GASCAN"] = True
          Globals.Flags["PICKED_UP_GASCAN"] = True
          self.RoomSpeak("I picked up one of the containers.")
        else:
          self.RoomSpeak("I don't think I'm going to need more than one of these.")
      
      # Object2
      elif entity == "EntityHousePatioObject2":
        self.RoomSpeak("I suppose given the state of disarray the rest of the house is in, healthy plants would have been more strange a sight.")
      
      # Object3
      elif entity == "EntityHousePatioObject3":
        self.RoomSpeak("No real way to see out from here, it's completely covered.")
      
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
    Room.Room.initialize(self, RoomHousePatio(), "RoomHousePatio", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHousePatioDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePatioDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePatioObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePatioObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePatioObject3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePatioHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePatioHidingSpot2"), self.EventHandler])
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
