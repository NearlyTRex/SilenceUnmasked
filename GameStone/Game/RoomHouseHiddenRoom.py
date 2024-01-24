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
import CutsceneBunny
import CutsceneScrapbook

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class RoomHouseHiddenRoom(Room.Room):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Button A
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A:
      
      # Door
      if entity == "EntityHouseHiddenRoomDoor":
        self.RoomSpeak("There's an opening leading back to the living room fireplace.")
      
      # Object1
      if entity == "EntityHouseHiddenRoomObject1":
        self.RoomSpeak("Sitting on a shelf is an old dirty stuffed bunny.  I guess at one point this must have been very important to someone... now it's just an old pile of dirty cotton.")
    
      # Object2
      if entity == "EntityHouseHiddenRoomObject2":
        self.RoomSpeak("There's a large scrapbook open on the desk.")
      
      # Object3
      if entity == "EntityHouseHiddenRoomObject3":
        self.RoomSpeak("Oh wow, there's a large and bloody axe laying on the floor... My god, it looks like it has fresh blood on it!")
      
      # Object4
      if entity == "EntityHouseHiddenRoomObject4":
        self.RoomSpeak("There's an evil looking painting on the wall... Odd... it looks like the eyes are following me as I move...")
      
      # Object5
      if entity == "EntityHouseHiddenRoomObject5":
        self.RoomSpeak("What a disgusting looking mattress... I sure hope no one had to sleep on this!")
      
      # Object6
      if entity == "EntityHouseHiddenRoomObject6":
        self.RoomSpeak("Someone has drawn figures all around the wall... people getting killed and other random disturbing scribbles...")
      
    # Button B
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Door
      if entity == "EntityHouseHiddenRoomDoor":
        app.ChangeState(RoomHouseLivingRoom.RoomHouseLivingRoom())
      
      # Object1
      if entity == "EntityHouseHiddenRoomObject1":
        if Globals.Flags["SEEN_BUNNY"]:
          self.RoomSpeak("I don't think I'm ever going to get that image out of my mind.... who would put an animal there?!")
        else:
          if Globals.Flags["HOLDING_ITEM"] and Globals.Flags["CURRENT_ITEM"] == "ObjectOpener":
            app.ChangeState(CutsceneBunny.CutsceneBunny())
          else:
            self.RoomSpeak("It feels like there might be something inside the stuffed bunny, maybe I should get something to open it?")
    
      # Object2
      if entity == "EntityHouseHiddenRoomObject2":
        if Globals.Flags["SEEN_SCRAPBOOK"]:
          self.RoomSpeak("I don't need to look at that disturbing stuff again, thank you very much...")
        else:
          app.ChangeState(CutsceneScrapbook.CutsceneScrapbook())
      
      # Object3
      if entity == "EntityHouseHiddenRoomObject3":
        if not Globals.Flags["PICKED_UP_AXE"]:
          if Globals.Flags["AXE_WARNING1"] and Globals.Flags["AXE_WARNING2"]:
            Globals.Flags["PICKED_UP_AXE"] = True
            Globals.Flags["HAVE_AXE"] = True
            self.RoomSpeak("Carefully, I picked up the heavy axe, trying not to get any of the blood on my hands... now what?")
          else:
            if not Globals.Flags["AXE_WARNING1"]:
              Globals.Flags["AXE_WARNING1"] = True
              self.RoomSpeak("I don't really think I should pick that up... it looks like it weighs a ton, I doubt it could be of much use...")
            elif not Globals.Flags["AXE_WARNING2"]:
              Globals.Flags["AXE_WARNING2"] = True
              self.RoomSpeak("I have a bad feeling about picking that up... I mean, for crying out loud, it's got something's... or someone's... blood on it!")
        else:
          self.RoomSpeak("There's a bloodstain on the floor where the axe was laying...")
        
      # Object4
      if entity == "EntityHouseHiddenRoomObject4":
        self.RoomSpeak("I think I'll stay far away from that painting, it's giving me the heeby jeebies.")
      
      # Object5
      if entity == "EntityHouseHiddenRoomObject5":
        self.RoomSpeak("No way I am getting anywhere near that!")
      
      # Object6
      if entity == "EntityHouseHiddenRoomObject6":
        self.RoomSpeak("Looks like most of these scribbles have been here for quite some time, though some look new...")
      
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
    if Globals.Flags["PICKED_UP_AXE"]:
      Room.Room.initialize(self, RoomHouseHiddenRoom(), "RoomHouseHiddenRoom", "Mansion")
    else:
      Room.Room.initialize(self, RoomHouseHiddenRoom(), "RoomHouseHiddenRoomAxe", "Mansion")
  
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomDoor"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomObject1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomObject2"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomObject3"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomObject4"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomObject5"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomObject6"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomHidingSpot1"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("EntityHouseHiddenRoomHidingSpot2"), self.EventHandler])
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
