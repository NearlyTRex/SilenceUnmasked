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
radmanager = Objects.RadioManager.GetInstance()
########################################################################################
class Inventory(State.State):
  
  ######################################################################################
  # EventHandler
  ######################################################################################
  def EventHandler(self, entity):
    
    # Set current item
    Globals.Flags["CURRENT_ITEM"] = entity
    
    # Now holding an item
    Globals.Flags["HOLDING_ITEM"] = True
    
    # Transfer back
    app.ChangeState(self.returnstate)
  
  ######################################################################################
  # Constructor
  ######################################################################################
  def __init__(self, state):
  
    # Initialize
    self.returnstate = state
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
  
    # Call parent
    State.State.initialize(self)
    
    # Load screen
    self.screenref = sptmanager.RetrieveByName("Inventory")
    self.screenref.SetVisible(True)
    
    # Load objects
    if Globals.Flags["HAVE_BUCKET_NONFILLED"] or Globals.Flags["HAVE_BUCKET_FILLED"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectBucket"), self.EventHandler])
    if Globals.Flags["HAVE_CROWBAR"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectCrowbar"), self.EventHandler])
    if Globals.Flags["HAVE_HANGER"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectHanger"), self.EventHandler])
    if Globals.Flags["HAVE_THINNER"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectThinner"), self.EventHandler])
    if Globals.Flags["HAVE_OPENER"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectOpener"), self.EventHandler])
    if Globals.Flags["HAVE_DOORKNOB"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectKnob"), self.EventHandler])
    if Globals.Flags["HAVE_GASCAN"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectGas"), self.EventHandler])
    if Globals.Flags["HAVE_PINS"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectPins"), self.EventHandler])
    if Globals.Flags["HAVE_LOCKET1"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectLocket1"), self.EventHandler])
    if Globals.Flags["HAVE_LOCKET2"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectLocket2"), self.EventHandler])
    if Globals.Flags["HAVE_DYNAMITE"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectDynamite"), self.EventHandler])
    if Globals.Flags["HAVE_MATCHES"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectMatches"), self.EventHandler])
    if Globals.Flags["HAVE_BIBLE"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectBible"), self.EventHandler])
    if Globals.Flags["HAVE_AXE"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectAxe"), self.EventHandler])
    if Globals.Flags["HAVE_MUSICBOX_KEYS"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectMusicBoxKeys"), self.EventHandler])
    if Globals.Flags["HAVE_COURTYARD_KEY"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectCourtyardKey"), self.EventHandler])
    if Globals.Flags["HAVE_BEDROOMHALL_KEY"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectBedroomHallKey"), self.EventHandler])
    if Globals.Flags["HAVE_BATHROOM_KEY"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectBathroomKey"), self.EventHandler])
    if Globals.Flags["HAVE_GARAGE_KEY"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectGarageKey"), self.EventHandler])
    if Globals.Flags["HAVE_STUDY_KEY"]:
      self.objects.append([sptmanager.RetrieveByName("ObjectStudyKey"), self.EventHandler])
    self.ShowObjects()
    
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
    
    # Unload objects
    self.HideObjects()
    
    # Hide cursor
    self.HideCursor()
    
    # Set flags
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
    if (not Globals.Events["OBJECT"]) and ((Globals.Events["INPUT"] == Constants.EVENT_BUTTON_A) or (Globals.Events["INPUT"] == Constants.EVENT_BUTTON_B)):
      
      # Transfer back
      app.ChangeState(self.returnstate)
########################################################################################
