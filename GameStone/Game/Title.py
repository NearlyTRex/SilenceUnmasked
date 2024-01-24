## Silence Unmasked
## Waterstone Productions

# System imports
import Application
import Objects

# Local imports
import Constants

# State imports
import State
import MainMenu

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class Title(State.State):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
    
    # Call parent
    State.State.initialize(self)
    
    # Wait counter
    self.counter = 0
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName("Title")
    self.screenref.SetVisible(True)
    
    # Load music
    self.musicref = radmanager.RetrieveByName("Music")
    self.musicref.Play("Title")
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    State.State.finalize(self)
    
    # Unload screen
    self.screenref.SetVisible(False)
  
  ######################################################################################
  # Update
  ######################################################################################
  def update(self):
    
    # Call parent
    State.State.update(self)
    
    # Increment counter
    self.counter += 1
    
    # Ready to transfer?
    if self.counter > Constants.SCREEN_MAXTIME:
      
      # Switch state
      app.ChangeState(MainMenu.MainMenu())
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):
    
    # Call parent
    State.State.input(self)
########################################################################################
