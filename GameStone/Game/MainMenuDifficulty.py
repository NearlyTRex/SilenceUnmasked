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
import Instructions1

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class MainMenuDifficulty(State.State):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Play click
    self.soundsref.Stop("Click")
    self.soundsref.Play("Click")
    
    # Easy game
    if entity == "ButtonMainMenuEasy":
      
      # Set difficulty
      Globals.Flags["HARD_DIFFICULTY"] = False
      
      # Start new game
      app.ChangeState(Instructions1.Instructions1())
    
    # Hard game
    elif entity == "ButtonMainMenuHard":
      
      # Set difficulty
      Globals.Flags["HARD_DIFFICULTY"] = True
      
      # Start new game
      app.ChangeState(Instructions1.Instructions1())
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
    
    # Call parent
    State.State.initialize(self)
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName("MainMenuDifficulty")
    self.screenref.SetVisible(True)
    
    # Load music
    self.musicref = radmanager.RetrieveByName("Music")
    if not self.musicref.IsPlaying("Title"):
      self.musicref.Play("Title")
    
    # Load sounds
    self.soundsref = radmanager.RetrieveByName("Sounds")
    
    # Load objects
    self.objects.append([sptmanager.RetrieveByName("ButtonMainMenuEasy"), self.EventHandler])
    self.objects.append([sptmanager.RetrieveByName("ButtonMainMenuHard"), self.EventHandler])
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
