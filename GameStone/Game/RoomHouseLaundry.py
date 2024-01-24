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
import RoomHouseSideHall2

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseLaundry(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door
      if entity == "EntityHouseLaundryDoor":
        self.RoomSpeak("Behind me is the door towards the side hall.")
      
      # Object1
      elif entity == "EntityHouseLaundryObject1":
        self.RoomSpeak("There's a washer here, with.... some moldy clothes inside.  Ewww...")
      
      # Object2
      elif entity == "EntityHouseLaundryObject2":
        self.RoomSpeak("A large basket filled with soiled clothing.  Yuck, I think some of this stuff has mold on it!")
      
      # HidingSpot1
      elif entity == "EntityHouseLaundryHidingSpot1":
        self.RoomSpeak("There are some dryers against the wall.  They seem to be empty.")
      
      # HidingSpot2
      elif entity == "EntityHouseLaundryHidingSpot2":
        self.RoomSpeak("There's a cabinet here, with some dirty towels laying on top.  Inside there's just some bottles of detergent.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door
      if entity == "EntityHouseLaundryDoor":
        app.ChangeState(RoomHouseSideHall2.RoomHouseSideHall2())
      
      # Object1
      elif entity == "EntityHouseLaundryObject1":
        if not Globals.Flags["PICKED_UP_GARAGE_KEY"]:
          Globals.Flags["HAVE_GARAGE_KEY"] = True
          Globals.Flags["PICKED_UP_GARAGE_KEY"] = True
          self.RoomSpeak("Pinching my nose, I reached into the washing machine and felt around in some of the clothing.  I found something, a hard metal object.  It was a key!")
        else:
          self.RoomSpeak("No way I'm going near those clothes again, I feel like I'm going to be sick just standing in this room!")
      
      # Object2
      elif entity == "EntityHouseLaundryObject2":
        self.RoomSpeak("There might be something of use in there, but I'm not going to touch any of that stuff as is and risk getting sick...")
      
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
    Room.Room.initialize(self, RoomHouseLaundry(), "RoomHouseLaundry", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLaundryDoor"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLaundryObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLaundryObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLaundryHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLaundryHidingSpot2"), self.EventHandler])
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
