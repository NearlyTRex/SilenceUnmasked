## Silence Unmasked
## Waterstone Productions

# Standard imports
import pickle, random

# System imports
import Application
import Objects

# Local imports
import Constants
import Globals

# State imports
import State
import Inventory
import TextArea
import HidingSpot
import MainMenu
import CutsceneShadowManDeath

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class Room(State.State):
  
  ######################################################################################
  # RoomSave
  ######################################################################################
  def RoomSave(self):
    
    # Being chased?
    if not Globals.Flags["BEING_CHASED"]:
      
      # Open save file
      savefile = open(Constants.SAVE_FILENAME, "wb")
      
      # Write save data
      pickle.dump(self.currentroom, savefile)
      pickle.dump(Globals.Flags, savefile)
      pickle.dump(Globals.Counters, savefile)
      
      # Close save file
      savefile.close()
      
      # Notify player
      self.RoomSpeak("Game saved!")
    
    # Chase mode
    else:
      
      # Notify player
      self.RoomSpeak("** Can't save now! **")
  
  ######################################################################################
  # RoomSpeak
  ######################################################################################
  def RoomSpeak(self, text):
    
    # Speak aloud to the room
    app.ChangeState(TextArea.TextArea(self.currentroom, self.currentscreen, text))
  
  ######################################################################################
  # RoomHide
  ######################################################################################
  def RoomHide(self):
    
    # Attempt to hide
    if Globals.Flags["BEING_CHASED"]:
      app.ChangeState(HidingSpot.HidingSpot(self.currentroom, self.currentscreen))
    else:
      self.RoomSpeak(random.choice(Constants.HIDING_SPOT_REMINDERS))
  
  ######################################################################################
  # RoomEventHandler
  ######################################################################################
  def RoomEventHandler(self, entity):
    
    # Either button
    if Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A or Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B:
      
      # Inventory
      if entity == "ButtonGameInventory":
        app.ChangeState(Inventory.Inventory(self.currentroom))
      
      # Save game
      elif entity == "ButtonGameSave":
        self.RoomSave()
      
      # Quit game
      elif entity == "ButtonGameQuit":
        self.musicref.StopAll()
        self.soundsref.StopAll()
        app.ChangeState(MainMenu.MainMenu())
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self, room, screen, music):
    
    # Call parent
    State.State.initialize(self)
    
    # Hard difficulty?
    if Globals.Flags["HARD_DIFFICULTY"]:
      
      # Determine chase
      if not Globals.Flags["BEING_CHASED"] and not Globals.Flags["DISPLAYED_SUBSCREEN"] and Globals.Flags["SEEN_SHADOWMAN_INTRO"]:
        random.seed(None)
        chance = random.randint(Constants.CHASE_CHANCE_RANGE_START, Constants.CHASE_CHANCE_RANGE_END)
        if chance < Constants.CHASE_CHANCE_RANGE_DIVIDER:
          Globals.Flags["BEING_CHASED"] = True
    
    # Initialize
    self.currentroom = room
    self.currentscreen = screen
    if Globals.Flags["BEING_CHASED"]:
      if music == "Storm":
        self.currentmusic = "Chase2"
      else:
        self.currentmusic = "Chase1"
    else:
      self.currentmusic = music
    
    # Load chase
    if not Globals.Flags["DISPLAYED_SUBSCREEN"]:
      if not Globals.Flags["BEING_CHASED_INSTANTLY"]:
        Globals.Counters["CHASE_COUNTER"] = Constants.CHASE_TIME_START
    Globals.Flags["DISPLAYED_SUBSCREEN"] = False
    Globals.Flags["BEING_CHASED_INSTANTLY"] = False
    
    # Load cloak
    self.cloakref = sptmanager.RetrieveByName("Cloak")
    if Globals.Flags["BEING_CHASED"]:
      if Globals.Counters["CHASE_COUNTER"] <= Constants.CHASE_TIME_CLOAK:
        self.cloakref.SetVisible(True)
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName(self.currentscreen)
    self.screenref.SetVisible(True)
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("ButtonGameInventory"), self.RoomEventHandler])
    self.objects.append([sptmanager.RetrieveByName("ButtonGameSave"), self.RoomEventHandler])
    self.objects.append([sptmanager.RetrieveByName("ButtonGameQuit"), self.RoomEventHandler])
    
    # Load music
    self.musicref = radmanager.RetrieveByName("Music")
    if not self.musicref.IsPlaying(self.currentmusic):
      self.musicref.StopAll()
      self.musicref.Play(self.currentmusic)
    
    # Load sounds
    self.soundsref = radmanager.RetrieveByName("Sounds")
    if not Globals.Flags["BEING_CHASED"]:
      self.soundsref.Stop("Knives")
    else:
      if not self.soundsref.IsPlaying("Knives"):
        self.soundsref.StopAll()
        self.soundsref.Play("Knives")
    
    # Show cursor
    self.ShowCursor()
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    State.State.finalize(self)
    
    # Unload cloak
    self.cloakref.SetVisible(False)
    
    # Unload screen
    self.screenref.SetVisible(False)
    
    # Hide cursor
    self.HideCursor()
  
  ######################################################################################
  # Update
  ######################################################################################
  def update(self):
    
    # Call parent
    State.State.update(self)
    
    # No objects selectable
    self.objectselectable = False
    
    # Object name
    self.objectname = ""
    
    # Loop through objects
    for object in self.objects:
      
      # Selectable?
      if object[0].IsMouseSelectable():
        
        # Selectable object
        self.objectselectable = True
        
        # Get name
        self.objectname = object[0].GetName()
        
        # If you find one, don't need to look for another
        break
    
    # Cursor string
    self.cursorstring = ""
    
    # Selectable object?
    if self.objectselectable:
      
      # Holding something
      if Globals.Flags["HOLDING_ITEM"]:
        
        # Determine cursor (held)
        if self.objectname.count("Object") > 0:
          self.cursorstring = "InspectableHeld"
        elif self.objectname.count("Door") > 0:
          self.cursorstring = "WalkableHeld"
        elif self.objectname.count("HidingSpot") > 0:
          self.cursorstring = "HideableHeld"
      
      # Not holding anything
      else:
        
        # Determine cursor (non-held)
        if self.objectname.count("Object") > 0:
          self.cursorstring = "Inspectable"
        elif self.objectname.count("Door") > 0:
          self.cursorstring = "Walkable"
        elif self.objectname.count("HidingSpot") > 0:
          self.cursorstring = "Hideable"
    
    # Not selectable for anything
    else:
      
      # Holding something
      if Globals.Flags["HOLDING_ITEM"]:
        
        # Determine cursor (held)
        self.cursorstring = "NormalHeld"
      
      # Not holding anything
      else:
        
        # Determine cursor (non-held)
        self.cursorstring = "Normal"
    
    # Update cursor
    self.cursorref.ChangeAnimation(self.cursorstring)
    
    # Being chased?
    if Globals.Flags["BEING_CHASED"]:
      
      # Decrement counter
      Globals.Counters["CHASE_COUNTER"] -= 1
      
      # Time for the cloak to appear?
      if Globals.Counters["CHASE_COUNTER"] <= Constants.CHASE_TIME_CLOAK:
        self.cloakref.SetVisible(True)
      
      # Time to die?
      if Globals.Counters["CHASE_COUNTER"] < Constants.CHASE_TIME_DIE:
        app.ChangeState(CutsceneShadowManDeath.CutsceneShadowManDeath())
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):
    
    # Call parent
    State.State.input(self)
########################################################################################
