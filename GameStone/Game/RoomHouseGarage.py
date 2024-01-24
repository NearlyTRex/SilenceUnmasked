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
import RoomDriveway2
import RoomHouseSideHall2
import CutsceneDark

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseGarage(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseGarageDoor1":
        self.RoomSpeak("Behind me is the door going outside to the driveway.")
      
      # Door2
      elif entity == "EntityHouseGarageDoor2":
        self.RoomSpeak("It goes into the house apparently.")
      
      # Object1
      elif entity == "EntityHouseGarageObject1":
        self.RoomSpeak("It's a pretty hefty hammer.  Could be used for a lot of things I guess.")
      
      # Object2
      elif entity == "EntityHouseGarageObject2":
        if not Globals.Flags["PICKED_UP_DOORKNOB"]:
          self.RoomSpeak("It's a doorknob with a weird face on it.  Looks like it's been recently repaired.")
        else:
          self.RoomSpeak("There's a few other miscellaneous things... a screwdriver, some nails.  Not a lot really useful at this time...")
      
      # Object3
      elif entity == "EntityHouseGarageObject3":
        self.RoomSpeak("A solitary light bulb that is lighting up the garage.  It looks like it's getting power temporarily from the motor it's attached to...")
      
      # Object4
      elif entity == "EntityHouseGarageObject4":
        self.RoomSpeak("The nozzle for the car's gas tank.  It's missing the cap.")
      
      # Object5
      elif entity == "EntityHouseGarageObject5":
        if not Globals.Flags["USED_GASCAN"]:
          self.RoomSpeak("An old broken down car sits in the garage.  It seems like most of the important parts are missing, though there's still a motor in there.  The car is currently rumbling and sputtering away, and it sounds like it's about to run out of gas sometime soon...")
        else:
          self.RoomSpeak("The tank of the car is full now, it should have no problems for the next few hours...")
      
      # Object6
      elif entity == "EntityHouseGarageObject6":
        self.RoomSpeak("An old canister of paint thinner.")
      
      # HidingSpot1
      elif entity == "EntityHouseGarageHidingSpot1":
        self.RoomSpeak("The back door to the car, seems to be unlocked.")
      
      # HidingSpot2
      elif entity == "EntityHouseGarageHidingSpot2":
        self.RoomSpeak("There's a cabinet under the workbench.  Not much inside except some bottles of oil.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseGarageDoor1":
        if Globals.Flags["USED_GASCAN"]:
          app.ChangeState(RoomDriveway2.RoomDriveway2())
        else:
          app.ChangeState(CutsceneDark.CutsceneDark())
      
      # Door2
      elif entity == "EntityHouseGarageDoor2":
        if Globals.Flags["USED_GASCAN"]:
          app.ChangeState(RoomHouseSideHall2.RoomHouseSideHall2())
        else:
          app.ChangeState(CutsceneDark.CutsceneDark())
      
      # Object1
      elif entity == "EntityHouseGarageObject1":
        if Globals.Flags["SMASHED_LOCKETS"]:
          self.RoomSpeak("It's a pretty hefty hammer.  Could be used for a lot of things I guess.")
        else:
          if Globals.Flags["HOLDING_ITEM"] and ((Globals.Flags["CURRENT_ITEM"] == "ObjectLocket1") or (Globals.Flags["CURRENT_ITEM"] == "ObjectLocket2")) and (Globals.Flags["HAVE_LOCKET1"] and Globals.Flags["HAVE_LOCKET2"]):
            Globals.Flags["SMASHED_LOCKETS"] = True
            Globals.Flags["HAVE_LOCKET1"] = False
            Globals.Flags["HAVE_LOCKET2"] = False
            Globals.Flags["HAVE_MUSICBOX_KEYS"] = True
            self.RoomSpeak("After smashing both lockets to bits, I saw to my surprise that there were tiny keys inside each!")
          else:
            self.RoomSpeak("It's a pretty hefty hammer.  Could be used for a lot of things I guess.")
      
      # Object2
      elif entity == "EntityHouseGarageObject2":
        if not Globals.Flags["PICKED_UP_DOORKNOB"]:
          Globals.Flags["HAVE_DOORKNOB"] = True
          Globals.Flags["PICKED_UP_DOORKNOB"] = True
          self.RoomSpeak("I picked up the doorknob.")
        else:
          self.RoomSpeak("Nothing else of interest remains here.")
      
      # Object3
      elif entity == "EntityHouseGarageObject3":
        self.RoomSpeak("Not much I can really do with it, nor would be a good idea to take it, it's supplying light to the garage.")
      
      # Object4
      elif entity == "EntityHouseGarageObject4":
        if Globals.Flags["USED_GASCAN"]:
          self.RoomSpeak("The gas tank is full now, I don't need to add any more.")
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectGas":
            Globals.Flags["USED_GASCAN"] = True
            self.RoomSpeak("I emptied the gas can into the tank of the car, it should be full now.")
          else:
            self.RoomSpeak("If I had some gasonline, I could probably fill the tank up.")
      
      # Object5
      elif entity == "EntityHouseGarageObject5":
        if Globals.Flags["BEING_CHASED"]:
          self.RoomHide()
        else:
          self.RoomSpeak("I can't use the car, it's broken.")
      
      # Object6
      elif entity == "EntityHouseGarageObject6":
        if not Globals.Flags["PICKED_UP_THINNER"]:
          Globals.Flags["HAVE_THINNER"] = True
          Globals.Flags["PICKED_UP_THINNER"] = True
          self.RoomSpeak("The container is a bit sticky and smells funny, but I got the paint thinner.")
        else:
          self.RoomSpeak("I only need one of these, yuck it smells!")
      
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
    Room.Room.initialize(self, RoomHouseGarage(), "RoomHouseGarage", "Sputter")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageObject3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageObject4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageObject5"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageObject6"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseGarageHidingSpot2"), self.EventHandler])
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
