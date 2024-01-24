## Silence Unmasked
## Waterstone Productions

# Local imports
import Constants
import Globals
import Scenes

# State imports
import Cutscene
import RoomHouseFrontHallLower

########################################################################################
class CutsceneShadowManIntro(Cutscene.Cutscene):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    Cutscene.Cutscene.initialize(self, Scenes.Scene_ShadowManIntro, RoomHouseFrontHallLower.RoomHouseFrontHallLower())
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    Cutscene.Cutscene.finalize(self)
    
    # Set flags
    Globals.Flags["BEING_CHASED"] = True
    Globals.Flags["BEING_CHASED_INSTANTLY"] = True
    Globals.Flags["SEEN_SHADOWMAN_INTRO"] = True
    
    # Set counters
    Globals.Counters["CHASE_COUNTER"] = Constants.CHASE_TIME_CLOAK
  
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
