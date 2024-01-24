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
import State
import CutsceneShadowManDeath

########################################################################################
HideSuccess = [
"Whew.... It looks like he didn't see me hide here...",
"It looks like he's moving away in the other direction... thank god he didn't find me!",
"Looks like the coast is clear..."
]
HideFailure = [
"Oh god, he saw me hide!  He's coming right for me!",
"Oh no, I think he's coming this way!  He must have saw me hide here!",
".....He's looking straight at me!  He must see me hiding here!"
]
########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
########################################################################################
class HidingSpot(State.State):
  
  ######################################################################################
  # Constructor
  ######################################################################################
  def __init__(self, state, screen):
  
    # Initialize
    self.returnstate = state
    self.roomscreen = screen
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    State.State.initialize(self)
    
    # Check success of hiding
    if Globals.Counters["CHASE_COUNTER"] <= Constants.CHASE_TIME_CLOAK:
      self.hidesuccessful = False
    else:
      self.hidesuccessful = True
    
    # Assign text
    if self.hidesuccessful:
      self.hidetext = random.choice(HideSuccess)
    else:
      self.hidetext = random.choice(HideFailure)
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName(self.roomscreen)
    self.screenref.SetVisible(True)
    self.screenref.SetColor(Application.Color(1, 1, 1, Constants.SCREEN_DIM))
    
    # Load text
    self.textref = fntmanager.RetrieveByName("Font")
    self.textref.SetVisible(True)
    self.textref.SetText(self.hidetext)
    
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
    Globals.Flags["BEING_CHASED"] = False
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
      if self.hidesuccessful:
        app.ChangeState(self.returnstate)
      else:
        app.ChangeState(CutsceneShadowManDeath.CutsceneShadowManDeath())
########################################################################################
