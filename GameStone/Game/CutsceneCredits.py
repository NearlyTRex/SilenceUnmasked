## Silence Unmasked
## Waterstone Productions

# Local imports
import Constants
import Globals
import Scenes

# State imports
import Cutscene
import MainMenu

########################################################################################
class CutsceneCredits(Cutscene.Cutscene):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    Cutscene.Cutscene.initialize(self, Scenes.Scene_Credits, MainMenu.MainMenu())
  
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
    
    # Last page?
    if (self.pagecounter == len(self.pages) - 1):
      
      # Show ranking
      if Globals.Flags["USED_EXPLOSIVE"]:
        if Globals.Flags["HAVE_AXE"]:
          self.textref.SetText("You got a ranking of C\nTry to find the other endings!")
        else:
          if Globals.Flags["PICKED_UP_BIBLE"]:
            self.textref.SetText("You got a ranking of A\nTry to find the other endings!")
          else:
            self.textref.SetText("You got a ranking of B\nTry to find the other endings!")
      else:
        self.textref.SetText("You got a ranking of D\nTry to find the other endings!")
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):
    
    # Call parent
    Cutscene.Cutscene.input(self)
########################################################################################
