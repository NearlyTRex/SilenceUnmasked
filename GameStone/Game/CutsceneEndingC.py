## Silence Unmasked
## Waterstone Productions

# Local imports
import Constants
import Globals
import Scenes

# State imports
import Cutscene
import CutsceneCredits

########################################################################################
class CutsceneEndingC(Cutscene.Cutscene):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    Cutscene.Cutscene.initialize(self, Scenes.Scene_EndingC, CutsceneCredits.CutsceneCredits())
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    Cutscene.Cutscene.finalize(self)
  
  ######################################################################################
  # Update
  ######################################################################################
  def update(self):
    
    # Call parent
    Cutscene.Cutscene.update(self)
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):
    
    # Call parent
    Cutscene.Cutscene.input(self)
########################################################################################
