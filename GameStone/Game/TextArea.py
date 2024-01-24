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

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
########################################################################################
class TextArea(State.State):
  
  ######################################################################################
  # Constructor
  ######################################################################################
  def __init__(self, state, screen, text):
  
    # Initialize
    self.returnstate = state
    self.roomscreen = screen
    self.textdata = text
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    State.State.initialize(self)
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName(self.roomscreen)
    self.screenref.SetVisible(True)
    self.screenref.SetColor(Application.Color(1, 1, 1, Constants.SCREEN_DIM))
    
    # Load text
    self.textref = fntmanager.RetrieveByName("Font")
    self.textref.SetVisible(True)
    self.textref.SetText(self.textdata)
    
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
    self.screenref.SetColor(Application.Color(1, 1, 1, Constants.SCREEN_NORMAL))
    
    # Unload text
    self.textref.SetVisible(False)
    
    # Hide cursor
    self.HideCursor()
    
    # Set flags
    Globals.Flags["DISPLAYED_SUBSCREEN"] = True
  
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
    
    # No object was clicked on    
    if (Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A) or (Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B):
      
      # Transfer back
      app.ChangeState(self.returnstate)
########################################################################################
