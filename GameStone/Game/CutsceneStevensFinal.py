## Silence Unmasked
## Waterstone Productions

# Local imports
import Constants
import Globals
import Scenes

# State imports
import Cutscene
import RoomCaveEntrance

########################################################################################
class CutsceneStevensFinal(Cutscene.Cutscene):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    if Globals.Flags["HAVE_BIBLE"]:
      Globals.Flags["HAVE_BIBLE"] = False
      Cutscene.Cutscene.initialize(self, Scenes.Scene_StevensFinal1, RoomCaveEntrance.RoomCaveEntrance()) 
    else:
      Cutscene.Cutscene.initialize(self, Scenes.Scene_StevensFinal2, RoomCaveEntrance.RoomCaveEntrance())
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    Cutscene.Cutscene.finalize(self)
    
    # Set flags
    Globals.Flags["BEING_CHASED"] = True
    Globals.Flags["SEEN_STEVENS_FINAL"] = True
  
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
