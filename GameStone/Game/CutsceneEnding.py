## Silence Unmasked
## Waterstone Productions

# System imports
import Application

# Local imports
import Constants
import Globals

# State imports
import State
import CutsceneEndingA
import CutsceneEndingB
import CutsceneEndingC
import CutsceneEndingD

########################################################################################
app = Application.Application.GetInstance()
########################################################################################
class CutsceneEnding(State.State):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    State.State.initialize(self)
    
    # Transfer to ending
    if Globals.Flags["USED_EXPLOSIVE"]:
      if Globals.Flags["HAVE_AXE"]:
        app.ChangeState(CutsceneEndingC.CutsceneEndingC())
      else:
        if Globals.Flags["PICKED_UP_BIBLE"]:
          app.ChangeState(CutsceneEndingA.CutsceneEndingA())
        else:
          app.ChangeState(CutsceneEndingB.CutsceneEndingB())
    else:
      app.ChangeState(CutsceneEndingD.CutsceneEndingD())
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    State.State.finalize(self)
  
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
