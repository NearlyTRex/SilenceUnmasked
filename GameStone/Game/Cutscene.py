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
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class Cutscene(State.State):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self, scene, state):
  
    # Call parent
    State.State.initialize(self)
    
    # Initialize
    self.pages = scene
    self.pagecounter = 0
    self.newstate = state
    self.counter = 0
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName(self.pages[self.pagecounter][0])
    self.screenref.SetVisible(True)
    
    # Load text
    self.textref = fntmanager.RetrieveByName(self.pages[self.pagecounter][1])
    self.textref.SetVisible(True)
    self.textref.SetText(self.pages[self.pagecounter][4])
    
    # Load music
    self.musicref = radmanager.RetrieveByName(self.pages[self.pagecounter][2])
    if not self.musicref.IsPlaying(self.pages[self.pagecounter][3]):
      self.musicref.StopAll()
      self.musicref.Play(self.pages[self.pagecounter][3])
    
    # Load sounds
    self.soundsref = radmanager.RetrieveByName("Sounds")
    self.soundsref.StopAll()
    
    # Show cursor
    self.ShowCursor()
    self.HideCursor()
    
    # Reset cursor
    self.cursorref.ChangeAnimation("Normal")
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    State.State.finalize(self)
    
    # Unload screen
    self.screenref.SetVisible(False)
    
    # Unload text
    self.textref.SetVisible(False)
    
    # Unload music
    self.musicref.StopAll()
    
    # Unload sounds
    self.soundsref.StopAll()
    
    # Hide cursor
    self.HideCursor()
  
  ######################################################################################
  # Update
  ######################################################################################
  def update(self):
    
    # Call parent
    State.State.update(self)
    
    # Increment counter
    self.counter += 1
    
    # Ready to transfer?
    if self.counter > Constants.SCREEN_MAXTIME_CUTSCENE:
      
      # Reset counter
      self.counter = 0
      
      # Unload screen
      self.screenref.SetVisible(False)
      
      # Advance page
      self.pagecounter += 1
    
      # Did the page counter go beyond the bounds?
      if self.pagecounter >= len(self.pages):
        
        # Reset counter
        self.pagecounter = 0
        
        # Transfer state
        app.ChangeState(self.newstate)
      
      # Still fine
      else:
        
        # Load screen
        self.screenref = sptmanager.RetrieveByName(self.pages[self.pagecounter][0])
        self.screenref.SetVisible(True)
        
        # Load text
        self.textref = fntmanager.RetrieveByName(self.pages[self.pagecounter][1])
        self.textref.SetVisible(True)
        self.textref.SetText(self.pages[self.pagecounter][4])
        
        # Load music
        self.musicref = radmanager.RetrieveByName(self.pages[self.pagecounter][2])
        if not self.musicref.IsPlaying(self.pages[self.pagecounter][3]):
          self.musicref.StopAll()
          self.musicref.Play(self.pages[self.pagecounter][3])
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):
    
    # Call parent
    State.State.input(self)
    
    # Some event came in
    #if Globals.Events["INPUT"] != Constants.EVENT_NOTHING:
    #  
    #  # Skip cutscene
    #  app.ChangeState(self.newstate)
########################################################################################
