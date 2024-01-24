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
import RoomHouseKitchen

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHousePantry(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door
      if entity == "EntityHousePantryDoor":
        self.RoomSpeak("The door back to the kitchen.")
      
      # Object1
      elif entity == "EntityHousePantryObject1":
        self.RoomSpeak("There's a cup here full of hairpins... strange to find in a pantry, but then everything in this house is strange....")
      
      # Object2
      elif entity == "EntityHousePantryObject2":
        self.RoomSpeak("There are some pots and pans on the shelf.")
      
      # Object3
      elif entity == "EntityHousePantryObject3":
        self.RoomSpeak("Looks like some bread, though I don't think normal bread is brown and green...")
      
      # Object4
      elif entity == "EntityHousePantryObject4":
        self.RoomSpeak("Ugh... someone left a bunch of steaks to thaw and apparently forgot them....")
      
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door
      if entity == "EntityHousePantryDoor":
        app.ChangeState(RoomHouseKitchen.RoomHouseKitchen())
      
      # Object1
      elif entity == "EntityHousePantryObject1":
        if not Globals.Flags["PICKED_UP_PINS"]:
          Globals.Flags["HAVE_PINS"] = True
          Globals.Flags["PICKED_UP_PINS"] = True
          self.RoomSpeak("I reached into the cup and grabbed a couple pins.")
        else:
          self.RoomSpeak("I don't think I'll be needing any more of them.")
      
      # Object2
      elif entity == "EntityHousePantryObject2":
        self.RoomSpeak("I probably don't need a pan at the moment.")
      
      # Object3
      elif entity == "EntityHousePantryObject3":
        self.RoomSpeak("You couldn't pay me to eat something like that.")
      
      # Object4
      elif entity == "EntityHousePantryObject4":
        self.RoomSpeak("Good thing I'm a vegetarian....")
      
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
    Room.Room.initialize(self, RoomHousePantry(), "RoomHousePantry", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHousePantryDoor"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePantryObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePantryObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePantryObject3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePantryObject4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePantryHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHousePantryHidingSpot2"), self.EventHandler])
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
