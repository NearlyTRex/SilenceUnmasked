## Silence Unmasked
## Waterstone Productions

# System imports
import Application
import Objects
import Math

# Local imports
import Constants
import Resources

# State imports
import State
import Title

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
fntmanager = Objects.FontManager.GetInstance()
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class Loader(State.State):
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
    
    # Call parent
    State.State.initialize(self)
    
    # Counters
    self.spritecounter = 0
    self.fontcounter = 0
    self.radiocounter = 0
    
    # Flags
    self.spritefinished = False
    self.fontfinished = False
    self.radiofinished = False
    
    # Type
    self.type = Constants.LOADER_TYPE_SPRITES
    
    # Get screen data
    name = Resources.Sprites[self.spritecounter][0]
    file = Resources.Sprites[self.spritecounter][1]
    x = Resources.Sprites[self.spritecounter][2][0]
    y = Resources.Sprites[self.spritecounter][2][1]
    z = Resources.Sprites[self.spritecounter][2][2]
    
    # Load screen
    self.screenid = sptmanager.Load(name, file)
    self.screenref = sptmanager.Retrieve(self.screenid)
    self.screenref.SetVisible(True)
    self.screenref.Move(x, y, z)
    self.spritecounter += 1
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    
    # Call parent
    State.State.finalize(self)
    
    # Unload screen
    self.screenref.SetVisible(False)
    
    # Set objects
    sptmanager.RetrieveByName("ObjectBucket").ChangeAnimation("Bucket")
    sptmanager.RetrieveByName("ObjectCrowbar").ChangeAnimation("Crowbar")
    sptmanager.RetrieveByName("ObjectHanger").ChangeAnimation("Hanger")
    sptmanager.RetrieveByName("ObjectThinner").ChangeAnimation("Thinner")
    sptmanager.RetrieveByName("ObjectOpener").ChangeAnimation("Opener")
    sptmanager.RetrieveByName("ObjectKnob").ChangeAnimation("Knob")
    sptmanager.RetrieveByName("ObjectGas").ChangeAnimation("Gas")
    sptmanager.RetrieveByName("ObjectPins").ChangeAnimation("Pins")
    sptmanager.RetrieveByName("ObjectLocket1").ChangeAnimation("Locket1")
    sptmanager.RetrieveByName("ObjectLocket2").ChangeAnimation("Locket2")
    sptmanager.RetrieveByName("ObjectDynamite").ChangeAnimation("Dynamite")
    sptmanager.RetrieveByName("ObjectMatches").ChangeAnimation("Matches")
    sptmanager.RetrieveByName("ObjectBible").ChangeAnimation("Bible")
    sptmanager.RetrieveByName("ObjectAxe").ChangeAnimation("Axe")
    sptmanager.RetrieveByName("ObjectMusicBoxKeys").ChangeAnimation("MusicBoxKeys")
    sptmanager.RetrieveByName("ObjectCourtyardKey").ChangeAnimation("CourtyardKey")
    sptmanager.RetrieveByName("ObjectBedroomHallKey").ChangeAnimation("BedroomHallKey")
    sptmanager.RetrieveByName("ObjectBathroomKey").ChangeAnimation("BathroomKey")
    sptmanager.RetrieveByName("ObjectGarageKey").ChangeAnimation("GarageKey")
    sptmanager.RetrieveByName("ObjectStudyKey").ChangeAnimation("StudyKey")
  ######################################################################################
  # Update
  ######################################################################################
  def update(self):
    
    # Call parent
    State.State.update(self)
    
    # Sprite type
    if self.type == Constants.LOADER_TYPE_SPRITES:
      
      # Do we still have sprites to load?
      if self.spritecounter < len(Resources.Sprites):
        
        # Get sprite data
        name = Resources.Sprites[self.spritecounter][0]
        file = Resources.Sprites[self.spritecounter][1]
        x = Resources.Sprites[self.spritecounter][2][0]
        y = Resources.Sprites[self.spritecounter][2][1]
        z = Resources.Sprites[self.spritecounter][2][2]
        
        # Load sprite
        print("Loading...", name)
        id = sptmanager.Load(name, file)
        ref = sptmanager.Retrieve(id)
        ref.Move(x, y, z)
        self.spritecounter += 1
      
      # Done with sprites
      else:
        
        # Sprites are finished
        print("Finished loading sprites")
        self.spritefinished = True
        self.type = Constants.LOADER_TYPE_FONTS
    
    # Font type
    elif self.type == Constants.LOADER_TYPE_FONTS:
      
      # Do we still have fonts to load?
      if self.fontcounter < len(Resources.Fonts):
        
        # Get font data
        name = Resources.Fonts[self.fontcounter][0]
        file = Resources.Fonts[self.fontcounter][1]
        x = Resources.Fonts[self.fontcounter][2][0]
        y = Resources.Fonts[self.fontcounter][2][1]
        z = Resources.Fonts[self.fontcounter][2][2]
        
        # Load font
        print("Loading...", name)
        id = fntmanager.Load(name, file)
        ref = fntmanager.Retrieve(id)
        ref.Move(x, y, z)
        self.fontcounter += 1
      
      # Done with fonts
      else:
        
        # Fonts are finished
        print("Finished loading fonts")
        self.fontfinished = True
        self.type = Constants.LOADER_TYPE_RADIOS
    
    # Radio type
    elif self.type == Constants.LOADER_TYPE_RADIOS:
      
      # Do we still have radios to load?
      if self.radiocounter < len(Resources.Radios):
        
        # Get radio data
        name = Resources.Radios[self.radiocounter][0]
        file = Resources.Radios[self.radiocounter][1]
        x = Resources.Radios[self.radiocounter][2][0]
        y = Resources.Radios[self.radiocounter][2][1]
        z = Resources.Radios[self.radiocounter][2][2]
        
        # Load font
        print("Loading...", name)
        id = radmanager.Load(name, file)
        ref = radmanager.Retrieve(id)
        ref.Move(x, y, z)
        self.radiocounter += 1
      
      # Done with radios
      else:
        
        # Radios are finished
        print("Finished loading radios")
        self.radiofinished = True
        self.type = Constants.LOADER_TYPE_NONE
    
    # All finished?
    if (self.spritefinished and self.fontfinished and self.radiofinished):
      
      # Move on
      app.ChangeState(Title.Title())
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):
    
    # Call parent
    State.State.input(self)
########################################################################################
