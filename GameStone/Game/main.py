## Silence Unmasked
## Waterstone Productions

# Standard imports
import os, sys

# System imports
import Application

# Local imports
import Constants
import Loader

########################################################################################
app = Application.Application.GetInstance()
########################################################################################
def main():
  
  # Set paths
  app.SetManagerPath(os.path.join(os.getcwd(), "../Manager/"))
  app.SetMetaPath(os.path.join(os.getcwd(), "../Meta/"))
  app.SetMediaPath(os.path.join(os.getcwd(), "../Media/"))
  
  # Set start
  app.StartGame(Loader.Loader())
  
  # Start game
  app.MainLoop("Silence Unmasked", False, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, 60, 32, 24, 8, 0)
########################################################################################
main()
