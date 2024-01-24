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
import RoomHousePaintingHall
import RoomHouseHiddenRoom
import RoomHouseFrontHallLower
import RoomHouseCourtyard

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseLivingRoom(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door1
      if entity == "EntityHouseLivingRoomDoor1":
        self.RoomSpeak("This is the door to the kitchen, though it's boarded up and inaccessible this way.")
      
      # Door2
      elif entity == "EntityHouseLivingRoomDoor2":
        self.RoomSpeak("This leads back to the painting hall.")
      
      # Door4
      elif entity == "EntityHouseLivingRoomDoor4":
        self.RoomSpeak("The front hall is on the other side of this door.")
      
      # Door5
      elif entity == "EntityHouseLivingRoomDoor5":
        self.RoomSpeak("This door opens up into the courtyard.")
      
      # Object1
      elif entity == "EntityHouseLivingRoomObject1":
        if not Globals.Flags["PICKED_UP_BEDROOMHALL_KEY"]:
          self.RoomSpeak("There's some random stuff on the table here...")
        else:
          self.RoomSpeak("Not much is left, just some old books.  Nothing else useful.")
      
      # Object2
      elif entity == "EntityHouseLivingRoomObject2":
        self.RoomSpeak("There's a stuffed moose head set against the wall.  Probably a hunting trophy.")
      
      # Object3
      elif entity == "EntityHouseLivingRoomObject3":
        self.RoomSpeak("A hunting rifle is set against the wall.")
      
      # Object4
      elif entity == "EntityHouseLivingRoomObject4":
        if not Globals.Flags["UNLOCKED_HIDDENROOM"]:
          self.RoomSpeak("It's a warm fireplace, which feels particularly good considering the weather...")
        else:
          self.RoomSpeak("Now that the fire is gone, everything feels a lot colder...")
      
      # HidingSpot1
      elif entity == "EntityHouseLivingRoomHidingSpot1":
        self.RoomSpeak("It's a ratty looking couch.  Still could be comfortable to sit on though.")
        
      # HidingSpot2
      elif entity == "EntityHouseLivingRoomHidingSpot2":
        self.RoomSpeak("Some old curtains cover a window.")
    
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door1
      if entity == "EntityHouseLivingRoomDoor1":
        self.RoomSpeak("The kitchen is blocked off it would seem, I need to find another way to get into there.")
      
      # Door2
      elif entity == "EntityHouseLivingRoomDoor2":
        app.ChangeState(RoomHousePaintingHall.RoomHousePaintingHall())
      
      # Door4
      elif entity == "EntityHouseLivingRoomDoor4":
        app.ChangeState(RoomHouseFrontHallLower.RoomHouseFrontHallLower())
      
      # Door5
      elif entity == "EntityHouseLivingRoomDoor5":
        app.ChangeState(RoomHouseCourtyard.RoomHouseCourtyard())
      
      # Object1
      elif entity == "EntityHouseLivingRoomObject1":
        if not Globals.Flags["PICKED_UP_BEDROOMHALL_KEY"]:
          Globals.Flags["HAVE_BEDROOMHALL_KEY"] = True
          Globals.Flags["PICKED_UP_BEDROOMHALL_KEY"] = True
          self.RoomSpeak("Picked up the bedroom hall key.")
        else:
          self.RoomSpeak("I see there's some magazines left on the table, but from looking at the dates, I don't think the mailman has come here in quite some time...")
      
      # Object2
      elif entity == "EntityHouseLivingRoomObject2":
        self.RoomSpeak("I don't really need to be carrying a moose's head.")
      
      # Object3
      elif entity == "EntityHouseLivingRoomObject3":
        self.RoomSpeak("It's too high to reach.  Not that I think it would be loaded anyway.")
      
      # Object4
      elif entity == "EntityHouseLivingRoomObject4":
        if Globals.Flags["UNLOCKED_HIDDENROOM"]:
          app.ChangeState(RoomHouseHiddenRoom.RoomHouseHiddenRoom())
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectBucket" and Globals.Flags["HAVE_BUCKET_FILLED"]:
            Globals.Flags["UNLOCKED_HIDDENROOM"] = True
            self.RoomSpeak("I threw the yucky water on the fire and it sizzled and died.... Hey! There was a hidden passage behind the fire!")
          else:
            self.RoomSpeak("As much as I enjoy being near a fire on a day like this, it's still burning hot so I'd better not touch it directly.")
      
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
    if not Globals.Flags["UNLOCKED_HIDDENROOM"]:
      Room.Room.initialize(self, RoomHouseLivingRoom(), "RoomHouseLivingRoom", "Fireplace")
    else:
      Room.Room.initialize(self, RoomHouseLivingRoom(), "RoomHouseLivingRoom", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomDoor1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomDoor2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomDoor3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomDoor4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomDoor5"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomObject3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomObject4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseLivingRoomHidingSpot2"), self.EventHandler])
    self.ShowObjects()
    
    # If we've entered here, it's now unlocked everywhere else
    Globals.Flags["UNLOCKED_LIVINGROOM"] = True
  
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
