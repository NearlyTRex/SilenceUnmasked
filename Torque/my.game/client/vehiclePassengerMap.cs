// vehiclePassengerMap.cs

if ( isObject( vehiclePassengerMap ) )
   vehiclePassengerMap.delete();
new ActionMap(vehiclePassengerMap);

//------------------------------------------------------------------------------
// Non-remapable binds
//------------------------------------------------------------------------------
function escapeFromGame()
{
   echo("vehiclePassengerMap");

   if ( $Server::ServerType $= "SinglePlayer" )
      MessageBoxYesNo( "Quit Mission", "Exit from this Mission?", "disconnect();", "");
   else
      MessageBoxYesNo( "Disconnect", "Disconnect from the server?", "disconnect();", "");
}

vehiclePassengerMap.bindCmd(keyboard, "escape", "", "escapeFromGame();");
vehiclePassengerMap.bindcmd(keyboard, "F2", "", "PlayerListGui.toggle();");

//------------------------------------------------------------------------------
// Message HUD functions
//------------------------------------------------------------------------------
vehiclePassengerMap.bind(keyboard, c, toggleMessageHud );
vehiclePassengerMap.bind(keyboard, "pageUp", pageMessageHudUp );
vehiclePassengerMap.bind(keyboard, "pageDown", pageMessageHudDown );
vehiclePassengerMap.bind(keyboard, "p", resizeMessageHud );

//------------------------------------------------------------------------------
// Demo recording functions
//------------------------------------------------------------------------------
vehiclePassengerMap.bind( keyboard, F3, startRecordingDemo );
vehiclePassengerMap.bind( keyboard, F4, stopRecordingDemo );

//------------------------------------------------------------------------------
// Helper Functions
//------------------------------------------------------------------------------
//vehiclePassengerMap.bind(keyboard, "F8", dropCameraAtPlayer);
//vehiclePassengerMap.bind(keyboard, "F7", dropPlayerAtCamera);

//------------------------------------------------------------------------------
// Misc.
//------------------------------------------------------------------------------

vehiclePassengerMap.bind(keyboard, tab, toggleFirstPerson );
vehiclePassengerMap.bindCmd(keyboard, "q", "commandToServer(\'FindNextFreeSeat\');", "");
vehiclePassengerMap.bindCmd(keyboard, "e", "commandToServer(\'DismountVehicle\');", "");
vehiclePassengerMap.bind(keyboard, "alt c", toggleCamera);
vehiclePassengerMap.bindCmd(keyboard, "ctrl k", "commandToServer('suicide');", "");

