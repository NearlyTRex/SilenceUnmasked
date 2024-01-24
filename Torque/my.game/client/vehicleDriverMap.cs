// vehicleDriverMap.cs

if ( isObject( vehicleDriverMap ) )
   vehicleDriverMap.delete();
new ActionMap(vehicleDriverMap);

//------------------------------------------------------------------------------
// Non-remapable binds
//------------------------------------------------------------------------------
function escapeFromGame()
{
   echo("vehicleDriverMap");

   if ( $Server::ServerType $= "SinglePlayer" )
      MessageBoxYesNo( "Quit Mission", "Exit from this Mission?", "disconnect();", "");
   else
      MessageBoxYesNo( "Disconnect", "Disconnect from the server?", "disconnect();", "");
}

vehicleDriverMap.bindCmd(keyboard, "escape", "", "escapeFromGame();");
vehicleDriverMap.bindcmd(keyboard, "F2", "", "PlayerListGui.toggle();");

//------------------------------------------------------------------------------
// Movement Keys
//------------------------------------------------------------------------------

function turnLeft(%val)
{
   $mvLeftAction = %val;
}

function turnRight(%val)
{
   $mvRightAction = %val;
}


vehicleDriverMap.bind( keyboard, a, turnLeft );
vehicleDriverMap.bind( keyboard, d, turnRight );
vehicleDriverMap.bind( keyboard, w, moveforward );
vehicleDriverMap.bind( keyboard, s, movebackward );
vehicleDriverMap.bind( mouse, xaxis, yaw );
vehicleDriverMap.bind( mouse, yaxis, pitch );


//------------------------------------------------------------------------------
// Message HUD functions
//------------------------------------------------------------------------------
vehicleDriverMap.bind(keyboard, c, toggleMessageHud );
vehicleDriverMap.bind(keyboard, "pageUp", pageMessageHudUp );
vehicleDriverMap.bind(keyboard, "pageDown", pageMessageHudDown );
vehicleDriverMap.bind(keyboard, "p", resizeMessageHud );

//------------------------------------------------------------------------------
// Demo recording functions
//------------------------------------------------------------------------------
vehicleDriverMap.bind( keyboard, F3, startRecordingDemo );
vehicleDriverMap.bind( keyboard, F4, stopRecordingDemo );

//------------------------------------------------------------------------------
// Helper Functions
//------------------------------------------------------------------------------
vehicleDriverMap.bind(keyboard, "F8", dropCameraAtPlayer);
vehicleDriverMap.bind(keyboard, "F7", dropPlayerAtCamera);

//------------------------------------------------------------------------------
// Misc.
//------------------------------------------------------------------------------

vehicleDriverMap.bind(keyboard, tab, toggleFirstPerson );
vehicleDriverMap.bindCmd(keyboard, "q", "commandToServer(\'FindNextFreeSeat\');", "");
vehicleDriverMap.bindCmd(keyboard, "ctrl k", "commandToServer('suicide');", "");
vehicleDriverMap.bind(keyboard, "alt c", toggleCamera);
vehicleDriverMap.bindCmd(keyboard, "e", "commandToServer(\'DismountVehicle\');", "");

