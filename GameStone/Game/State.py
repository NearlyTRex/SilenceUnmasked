## Silence Unmasked
## Waterstone Productions

# System imports
import Application
import Objects
import Math

# Local imports
import Constants
import Globals

########################################################################################
app = Application.Application.GetInstance()
sptmanager = Objects.SpriteManager.GetInstance()
########################################################################################
class State(object):
  
  ######################################################################################
  # ShowObjects
  ######################################################################################
  def ShowObjects(self):
    
    # Loop through objects
    for object in self.objects:
      
      # Show
      object[0].SetVisible(True)
  
  ######################################################################################
  # HideObjects
  ######################################################################################
  def HideObjects(self):
    
    # Loop through objects
    for object in self.objects:
      
      # Show
      object[0].SetVisible(False)
  
  ######################################################################################
  # ShowCursor
  ######################################################################################
  def ShowCursor(self):
    
    # Show cursor
    self.cursorref = sptmanager.RetrieveByName("Cursor")
    self.cursorref.SetVisible(True)
    self.cursorshown = True
  
  ######################################################################################
  # HideCursor
  ######################################################################################
  def HideCursor(self):
    
    # Hide cursor
    self.cursorref.SetVisible(False)
    self.cursorshown = False
  
  ######################################################################################
  # Initialize
  ######################################################################################
  def initialize(self):
      
    # Setup colors
    app.GetColor(Application.SLOT_COLOR_AMBIENT).SetAll(1, 1, 1, 1)
    app.GetColor(Application.SLOT_COLOR_CLEAR).SetAll(0, 0, 0, 0)
    
    # Setup camera
    self.camera = app.GetCamera(Application.SLOT_CAMERA_OBJECT)
    self.camera.SetViewport(0, 0, app.GetWindowWidth(), app.GetWindowHeight())
    self.camera.SetOrtho(-10, 1000)
    self.camera.SetPosition(Math.Vector(0, 0, -400))
    
    # Setup controller
    self.controllera = app.GetController(Application.SLOT_CONTROLLER_A)
    self.controllerb = app.GetController(Application.SLOT_CONTROLLER_B)
    self.controller = self.controllera
    self.controller.RegisterPress(Application.CONTROLLER_BUTTON_A, Application.CONTROLLER_TYPE_MOUSE, Application.CODE_MOUSE_LEFT)
    self.controller.RegisterPress(Application.CONTROLLER_BUTTON_B, Application.CONTROLLER_TYPE_MOUSE, Application.CODE_MOUSE_RIGHT)
    self.controller.RegisterPress(Application.CONTROLLER_BUTTON_C, Application.CONTROLLER_TYPE_MOUSE, Application.CODE_MOUSE_MIDDLE)
    
    # Setup objects
    self.objects = []
    self.objectselectable = False
    
    # Setup cursor
    self.cursorshown = False
  
  ######################################################################################
  # Finalize
  ######################################################################################
  def finalize(self):
    pass
  
  ######################################################################################
  # Update
  ######################################################################################
  def update(self):
    
    # Visible cursor
    if self.cursorshown:
      
      # Set position
      self.cursorref.SetPosition(self.controller.GetWorldMousePosition() - Math.Vector(10, 30, 0))
  
  ######################################################################################
  # Input
  ######################################################################################
  def input(self):

    # Reset flags
    Globals.Events["INPUT"] = Constants.EVENT_NOTHING
    Globals.Events["OBJECT"] = False
    
    # Button A pressed?
    if self.controller.IsButtonAPressed():
      
      # Set flag
      Globals.Events["INPUT"] = Constants.EVENT_BUTTON_A
      self.controller.Clear()
      
    # Button B pressed?
    elif self.controller.IsButtonBPressed():
      
      # Set flag
      Globals.Events["INPUT"] = Constants.EVENT_BUTTON_B
      self.controller.Clear()
    
    # Flagged event
    if Globals.Events["INPUT"] != Constants.EVENT_NOTHING:
      
      # Loop through objects
      for object in self.objects:
        
        # Selectable?
        if object[0].IsMouseSelectable():
          
          # Hit an object
          Globals.Events["OBJECT"] = True
          
          # Run event handler
          object[1](object[0].GetName())
          return
    
    # Clear all system input
    self.controller.Clear()
########################################################################################
