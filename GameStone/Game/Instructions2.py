## Silence Unmasked
## Waterstone Productions

# System imports
import Application
import Objects

# Local imports
import Constants
import Globals

# State imports
import State
import CutsceneIntro

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class Instructions2(State.State):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
    
    # Call parent
    State.State.initialize(self)
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName("Instructions2")
    self.screenref.SetVisible(True)
    
    # Load music
    self.musicref = radmanager.RetrieveByName("Music")
    if not self.musicref.IsPlaying("Title"):
      self.musicref.Play("Title")
    
    # Load sounds
    self.soundsref = radmanager.RetrieveByName("Sounds")
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    State.State.finalize(self)
    
    # Unload screen
    self.screenref.SetVisible(False)
    
    # Unload music
    self.musicref.StopAll()
  
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
    
    # Any button
    if Globals.Events["INPUT"] != Constants.EVENT_NOTHING:
      
      # Play click
      self.soundsref.Stop("Click")
      self.soundsref.Play("Click")
      
      # Advance
      app.ChangeState(CutsceneIntro.CutsceneIntro())
########################################################################################
