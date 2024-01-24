## Silence Unmasked
## Waterstone Productions

# Standard imports
import os, sys, pickle

# System imports
import Application
import Objects

# Local imports
import Constants
import Globals

# State imports
import State
import MainMenuDifficulty

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
def ClearFlags():
  
  # Clear events
  Globals.Events["INPUT"] = Constants.EVENT_NOTHING
  Globals.Events["OBJECT"] = False
  
  # Loop through counters
  for key in Globals.Counters.keys():
    
    # Clear counter
    Globals.Counters[key] = 0
  
  # Loop through flags
  for key in Globals.Flags.keys():
    
    # Clear flag
    Globals.Flags[key] = False
########################################################################################
class MainMenu(State.State):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Play click
    self.soundsref.Stop("Click")
    self.soundsref.Play("Click")
    
    # New game
    if entity == "ButtonMainMenuNewGame":
      
      # Start new game
      app.ChangeState(MainMenuDifficulty.MainMenuDifficulty())
    
    # Continue game
    elif entity == "ButtonMainMenuContinue":
      
      # Save game exists?
      if os.path.exists(os.path.join(os.getcwd(), Constants.SAVE_FILENAME)):
        
        # Open save file
        savefile = open(Constants.SAVE_FILENAME, "rb")
        
        # Read save data
        room = pickle.load(savefile)
        flags = pickle.load(savefile)
        counters = pickle.load(savefile)
        
        # Close save file
        savefile.close()
        
        # Assign save data
        Globals.Flags = flags
        Globals.Counters = counters
        
        # Transfer to room
        app.ChangeState(room)
    
    # Quit
    elif entity == "ButtonMainMenuQuit":
      
      # Quit game
      app.EndGame()
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
    
    # Call parent
    State.State.initialize(self)
    
    # Clear flags
    ClearFlags()
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName("MainMenu")
    self.screenref.SetVisible(True)
    
    # Load music
    self.musicref = radmanager.RetrieveByName("Music")
    if not self.musicref.IsPlaying("Title"):
      self.musicref.Play("Title")
    
    # Load sounds
    self.soundsref = radmanager.RetrieveByName("Sounds")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("ButtonMainMenuNewGame"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("ButtonMainMenuContinue"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("ButtonMainMenuQuit"), self.EventHandler])
    self.ShowObjects()
    
    # Show cursor
    self.ShowCursor()
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    State.State.finalize(self)
    
    # Unload screen
    self.screenref.SetVisible(False)
    
    # Unload objects
    self.HideObjects()
    
    # Hide cursor
    self.HideCursor()
  
  ######################################################################################
  # Update
  ######################################################################################
  def update(self):
    
    # Call parent
    State.State.update(self)
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):
    
    # Call parent
    State.State.input(self)
########################################################################################
