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
import RoomHouseKitchen
import RoomHouseLaundry
import RoomHouseGarage
import CutsceneStevensBible

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseSideHall2(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseSideHall2Door1":
        self.RoomSpeak("Behind me is the other part of the side hall.")
      
      # Door2
      elif entity == "EntityHouseSideHall2Door2":
        if not Globals.Flags["UNLOCKED_KITCHEN"]:
          self.RoomSpeak("The door to the kichen.  It's missing a handle though.")
        else:
          self.RoomSpeak("The door to the kitchen, sporting a spiffy new handle.")
      
      # Door3
      elif entity == "EntityHouseSideHall2Door3":
        self.RoomSpeak("It appears to be the laundry room.")
      
      # Door4
      elif entity == "EntityHouseSideHall2Door4":
        self.RoomSpeak("This is the garage door.  I can hear a motor running on the other side...")
      
      # Door5
      elif entity == "EntityHouseSideHall2Door5":
        self.RoomSpeak("It probably used to be a bathroom door at one time, but now it's completely boarded up.")
      
      # Object1
      elif entity == "EntityHouseSideHall2Object1":
        self.RoomSpeak("It looks like a tiny mouse hole...")
      
      # HidingSpot1
      elif entity == "EntityHouseSideHall2HidingSpot1":
        self.RoomSpeak("It's a table, covered with some books, papers, and magazines.  Doesn't look like there's anything here dated beyond 1980...")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseSideHall2Door1":
        app.ChangeState(RoomHouseSideHall1.RoomHouseSideHall1())
      
      # Door2
      elif entity == "EntityHouseSideHall2Door2":
        if Globals.Flags["UNLOCKED_KITCHEN"]:
          if not Globals.Flags["SEEN_STEVENS_BIBLE"]:
            app.ChangeState(CutsceneStevensBible.CutsceneStevensBible())
          else:
            app.ChangeState(RoomHouseKitchen.RoomHouseKitchen())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectKnob":
            Globals.Flags["UNLOCKED_KITCHEN"] = True
            Globals.Flags["HAVE_DOORKNOB"] = False
            self.RoomSpeak("The handle fit into the door snugly, I can open it now.")
          else:
            self.RoomSpeak("There's a handle missing from the door, I won't be able to open it yet.")
      
      # Door3
      elif entity == "EntityHouseSideHall2Door3":
        app.ChangeState(RoomHouseLaundry.RoomHouseLaundry())
      
      # Door4
      elif entity == "EntityHouseSideHall2Door4":
        if Globals.Flags["UNLOCKED_GARAGE"]:
          app.ChangeState(RoomHouseGarage.RoomHouseGarage())
        else:
          self.RoomSpeak("I can't open it, it's locked.")
      
      # Door5
      elif entity == "EntityHouseSideHall2Door5":
        self.RoomSpeak("I can't get into that room, it's been nailed over with plywood.")
      
      # Object1
      elif entity == "EntityHouseSideHall2Object1":
        if not Globals.Flags["PICKED_UP_OPENER"]:
          Globals.Flags["HAVE_OPENER"] = True
          Globals.Flags["PICKED_UP_OPENER"] = True
          self.RoomSpeak("I reached my hand inside the hole and tried to see if there was anything inside it.  Among all the dirt and other unmentionable things I felt, there was a strange metal object inside.  Pulling out, I found a letter opener.  How the heck did that get there?")
        else:
          self.RoomSpeak("Nothing else in there except... well you know.")
      
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
    Room.Room.initialize(self, RoomHouseSideHall2(), "RoomHouseSideHall2", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2Door1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2Door2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2Door3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2Door4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2Door5"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2Object1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2Object2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2HidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseSideHall2HidingSpot2"), self.EventHandler])
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
