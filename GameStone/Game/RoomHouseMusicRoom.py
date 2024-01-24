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
class RoomHouseMusicRoom(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseMusicRoomDoor1":
        self.RoomSpeak("This leads back to the bedroom hall.")
      
      # Door2
      elif entity == "EntityHouseMusicRoomDoor2":
        self.RoomSpeak("It looks like another small room... but someone thought it would be a great idea to nail a bunch of two by fours across the door.")
      
      # Object1
      elif entity == "EntityHouseMusicRoomObject1":
        self.RoomSpeak("It's an old fashioned record player...")
      
      # Object2
      elif entity == "EntityHouseMusicRoomObject2":
        self.RoomSpeak("It's a music box.  It seems to have a ballerina on top that moves when played.")
      
      # Object3
      elif entity == "EntityHouseMusicRoomObject3":
        self.RoomSpeak("A guitar.  Looks like it's in decent condition, I wonder how well it plays?")
      
      # HidingSpot1
      elif entity == "EntityHouseMusicRoomHidingSpot1":
        self.RoomSpeak("It's an old fashioned piano, looks like it's out of tune though.")
      
      # HidingSpot2
      elif entity == "EntityHouseMusicRoomHidingSpot2":
        self.RoomSpeak("Between the piano and the table I see that some music notes fell through.")
      
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseMusicRoomDoor1":
        app.ChangeState(RoomHouseBedHall.RoomHouseBedHall())
      
      # Door2
      elif entity == "EntityHouseMusicRoomDoor2":
        self.RoomSpeak("I can't get in there, it's completely boarded up.  You know, with wood, nails, that kind of thing.")
      
      # Object1
      elif entity == "EntityHouseMusicRoomObject1":
        self.RoomSpeak("I can't open it to change the record being played... it seems like it's locked shut.")
      
      # Object2
      elif entity == "EntityHouseMusicRoomObject2":
        if Globals.Flags["PICKED_UP_STUDY_KEY"]:
          self.RoomSpeak("I already opened the music box.  There's not much else to do here except wind it up and play the music.")
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectMusicBoxKeys":
            Globals.Flags["PICKED_UP_STUDY_KEY"] = True
            Globals.Flags["HAVE_STUDY_KEY"] = True
            self.RoomSpeak("I put both small keys into the locks of the music box and turned.  Something on the bottom clicked, and I opened the base and saw that there was something inside.  Another key!  This one looks pretty important to have been kept so hidden away...")
          else:
            self.RoomSpeak("There's a couple of keyholes at the base of the box.  I wonder what could be inside this?")
      
      # Object3
      elif entity == "EntityHouseMusicRoomObject3":
        self.RoomSpeak("I'm not very good at playing, but I am a huge fan of listening to guitar music.")
      
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
    Room.Room.initialize(self, RoomHouseMusicRoom(), "RoomHouseMusicRoom", "Dancing")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseMusicRoomDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseMusicRoomDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseMusicRoomObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseMusicRoomObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseMusicRoomObject3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseMusicRoomHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseMusicRoomHidingSpot2"), self.EventHandler])
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
