## Silence Unmasked
## Waterstone Productions

# Local imports
import Constants
import Globals
import Scenes

# State imports
import Cutscene
import RoomHouseHiddenRoom

########################################################################################
class CutsceneScrapbook(Cutscene.Cutscene):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    Cutscene.Cutscene.initialize(self, Scenes.Scene_Scrapbook, RoomHouseHiddenRoom.RoomHouseHiddenRoom())
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    Cutscene.Cutscene.finalize(self)
    
    # Set flags
    Globals.Flags["SEEN_SCRAPBOOK"] = True
  
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
