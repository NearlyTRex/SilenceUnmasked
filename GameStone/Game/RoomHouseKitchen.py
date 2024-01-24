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
import RoomHouseBack
import RoomHousePantry
import RoomHouseSideHall2

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseKitchen(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseKitchenDoor1":
        self.RoomSpeak("There's a door here leading back outside.")
      
      # Door2
      elif entity == "EntityHouseKitchenDoor2":
        self.RoomSpeak("It's a pantry.")
      
      # Door3
      elif entity == "EntityHouseKitchenDoor3":
        self.RoomSpeak("I can get back to the side hall via this door.")
      
      # Door4
      elif entity == "EntityHouseKitchenDoor4":
        self.RoomSpeak("That would be the living room door, I think.  Too bad I can't get through that way.")
      
      # Object1
      elif entity == "EntityHouseKitchenObject1":
        self.RoomSpeak("The kitchen sink.  It seems to work, though it just pours out a brownish looking water...  Yuck.")
      
      # Object2
      elif entity == "EntityHouseKitchenObject2":
        self.RoomSpeak("There's a barrel of some kind of fish... though they smell like they're rotting... The label says 'Herring'.  Hmm... seems to be of the red variety I think.")
      
      # HidingSpot1
      elif entity == "EntityHouseKitchenHidingSpot1":
        self.RoomSpeak("It's an antique fridge.  I half expected rotting meat to be there or something, but it's completely empty inside.")
      
      # HidingSpot2
      elif entity == "EntityHouseKitchenHidingSpot2":
        self.RoomSpeak("A dining table.  There are some placemats and dishes set out, though nothing is on the plates.  Plenty of space underneath.")
      
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseKitchenDoor1":
        if Globals.Flags["UNLOCKED_BACKAREA"]:
          app.ChangeState(RoomHouseBack.RoomHouseBack())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectPins":
            Globals.Flags["UNLOCKED_BACKAREA"] = True
            self.RoomSpeak("I used the pins to pick the lock.  Seemed easy enough, given that I'm a Master of Unlocking.")
          else:
            self.RoomSpeak("It's locked.  I'll need a key or some way to pick the lock...")
      
      # Door2
      elif entity == "EntityHouseKitchenDoor2":
        app.ChangeState(RoomHousePantry.RoomHousePantry())
      
      # Door3
      elif entity == "EntityHouseKitchenDoor3":
        app.ChangeState(RoomHouseSideHall2.RoomHouseSideHall2())
      
      # Door4
      elif entity == "EntityHouseKitchenDoor4":
        self.RoomSpeak("Can't go that way, it's all boarded up.")
      
      # Object1
      elif entity == "EntityHouseKitchenObject1":
        if not Globals.Flags["HAVE_BUCKET_FILLED"] and Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectBucket":
          Globals.Flags["HAVE_BUCKET_NONFILLED"] = False
          Globals.Flags["HAVE_BUCKET_FILLED"] = True
          self.RoomSpeak("Turning on the faucet, I filled the bucket with the murky looking water.  It's much heavier now.")
        else:
          self.RoomSpeak("What am I supposed to do?  Wash my hands?  This water is gross looking...")
      
      # Object2
      elif entity == "EntityHouseKitchenObject2":
        self.RoomSpeak("What should do I do with them?  They're all gross and rotting away, and I'm certainly not planning on eating them!")
      
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
    Room.Room.initialize(self, RoomHouseKitchen(), "RoomHouseKitchen", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseKitchenDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseKitchenDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseKitchenDoor3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseKitchenDoor4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseKitchenObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseKitchenObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseKitchenHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseKitchenHidingSpot2"), self.EventHandler])
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
