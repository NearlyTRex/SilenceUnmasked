//-----------------------------------------------------------------------------

// Variables used by client scripts & code.  The ones marked with (c)
// are accessed from code.  Variables preceeded by Pref:: are client
// preferences and stored automatically in the ~/client/prefs.cs file
// in between sessions.
//
//    (c) Client::MissionFile             Mission file name
//    ( ) Client::Password                Password for server join

//    (?) Pref::Player::CurrentFOV
//    (?) Pref::Player::DefaultFov
//    ( ) Pref::Input::KeyboardTurnSpeed

//    (c) pref::Master[n]                 List of master servers
//    (c) pref::Net::RegionMask     
//    (c) pref::Client::ServerFavoriteCount
//    (c) pref::Client::ServerFavorite[FavoriteCount]
//    .. Many more prefs... need to finish this off

// Moves, not finished with this either...
//    (c) firstPerson
//    $mv*Action...

//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

function initClient()
{
   echo("\n--------- Initializing MOD: FPS Starter Kit: Client ---------");

   // Make sure this variable reflects the correct state.
   $Server::Dedicated = false;

   // Game information used to query the master server
   $Client::GameTypeQuery = "FPS Starter Kit";
   $Client::MissionTypeQuery = "Any";

   //
   exec("./customProfiles.cs"); // override the base profiles if necessary

   // The common module provides basic client functionality
   initBaseClient();

   // InitCanvas starts up the graphics system.
   // The canvas needs to be constructed before the gui scripts are
   // run because many of the controls assume the canvas exists at
   // load time.
   initCanvas("Torque Game Engine", true);
   if (!isObject(Canvas))
      // failed, don't make it worse by crashing...
      return;

   /// Load client-side Audio Profiles/Descriptions
   exec("./audioProfiles.cs");

   // Load up the Game GUIs
   exec("./defaultGameProfiles.cs");
   exec("./PlayGui.gui");
   //exec("./ChatHud.gui");
   //exec("./playerList.gui");

   // Load up the shell GUIs
   exec("./mainMenuGui.gui");
   exec("./aboutDlg.gui");
   exec("./startMissionGui.gui");
   exec("./joinServerGui.gui");
   exec("./loadingGui.gui");
   exec("./endGameGui.gui");
   exec("./optionsDlg.gui");
   exec("./remapDlg.gui");
   exec("./StartupGui.gui");

   // Client scripts
   exec("./client.cs");
   exec("./game.cs");
   exec("./missionDownload.cs");
   exec("./serverConnection.cs");
   exec("./playerList.cs");
   exec("./loadingGui.cs");
   exec("./optionsDlg.cs");
   exec("./chatHud.cs");
   exec("./messageHud.cs");
   exec("./playGui.cs");
   exec("./centerPrint.cs");
   exec("./vehiclePassengerMap.cs");
   exec("./vehicleDriverMap.cs");

   // Default player key bindings
   exec("./default.bind.cs");
   exec("./config.cs");

   // Really shouldn't be starting the networking unless we are
   // going to connect to a remote server, or host a multi-player
   // game.
   setNetPort(0);

   // Copy saved script prefs into C++ code.
   setShadowDetailLevel( $pref::shadows );
   setDefaultFov( $pref::Player::defaultFov );
   setZoomSpeed( $pref::Player::zoomSpeed );

   // Start up the main menu... this is separated out into a 
   // method for easier mod override.

   if ($JoinGameAddress !$= "") {
      // If we are instantly connecting to an address, load the
      // main menu then attempt the connect.
      loadMainMenu();
      connect($JoinGameAddress, "", $Pref::Player::Name);
   }
   else {
      // Otherwise go to the splash screen.
      Canvas.setCursor("DefaultCursor");
      loadStartup();
   }
}


//-----------------------------------------------------------------------------


function loadMainMenu()
{
   // Startup the client with the Main menu...
   Canvas.setContent( MainMenuGui );


   // Make sure the audio initialized.
   if($Audio::initFailed) {
      MessageBoxOK("Audio Initialization Failed", 
         "The OpenAL audio system failed to initialize.  " @
         "You can get the most recent OpenAL drivers <a:www.garagegames.com/docs/torque/gstarted/openal.html>here</a>.");
   }

   Canvas.setCursor("DefaultCursor");
}


