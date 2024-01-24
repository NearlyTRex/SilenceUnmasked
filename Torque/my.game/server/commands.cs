//-----------------------------------------------------------------------------
// Torque Game Engine 
// Copyright (C) GarageGames.com, Inc.
//-----------------------------------------------------------------------------

function serverCmdMountVehicle(%client)
{
   //Determine how far should the picking ray extend into the world?
   %selectRange = 3;

   // Only search for vehicles
   %searchMasks = $TypeMasks::vehicleObjectType;

   %pos = %client.player.getEyePoint();

   // Start with the shape's eye vector...
   %eye = %client.player.getEyeVector();
   %eye = vectorNormalize(%eye);
   %vec = vectorScale(%eye, %selectRange);

   %end = vectorAdd(%vec, %pos);

   %scanTarg = ContainerRayCast (%pos, %end, %searchMasks);

   // a target in range was found so select it
   if (%scanTarg)
   {
      %targetObject = firstWord(%scanTarg);
      echo("Found a vehicle: " @ %targetObject);
      onMountVehicle(%targetObject.getDataBlock(),
                     %client.player,
                     %targetObject);
   }
   else
   {
      echo("No object found");
   }
}

function serverCmdDismountVehicle(%client)
{
   doPlayerDismount(%client, %client.player, %true);
}


function serverCmdFindNextFreeSeat(%client)
{
   echo("serverCmdFindNextFreeSeat " @ %client.nameBase);

   // Is the vehicle moving? If so, prevent the player from switching seats
   if (isVehicleMoving(%client.player.mvehicle) == true)
      return;

   %newSeat = findNextFreeSeat(%client,
                               %client.player.mvehicle,
                               %client.player.mvehicle.getDataBlock());

   if (%newSeat != -1)
   {
      echo("Found new seat " @ %newSeat);

      setActiveSeat(%client.player,
                    %client.player.mvehicle,
                    %client.player.mvehicle.getDataBlock(),
                    %newSeat);
   }
   else
   {
      echo("No next free seat");
   }
}

//-----------------------------------------------------------------------------
// Misc. server commands avialable to clients
//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

function serverCmdToggleCamera(%client)
{
   %control = %client.getControlObject();
   if (%control == %client.player)
   {
      %control = %client.camera;
      %control.mode = toggleCameraFly;
   }
   else
   {
      %control = %client.player;
      %control.mode = observerFly;
   }
   %client.setControlObject(%control);
}

function serverCmdDropPlayerAtCamera(%client)
{
   if ($Server::TestCheats || isObject(EditorGui))
   {
      %client.player.setTransform(%client.camera.getTransform());
      %client.player.setVelocity("0 0 0");
      %client.setControlObject(%client.player);
   }
}

function serverCmdDropCameraAtPlayer(%client)
{
   %client.camera.setTransform(%client.player.getEyeTransform());
   %client.camera.setVelocity("0 0 0");
   %client.setControlObject(%client.camera);
}


//-----------------------------------------------------------------------------

function serverCmdSuicide(%client)
{
   if (isObject(%client.player))
      %client.player.kill("Suicide");
}   

function serverCmdPlayCel(%client,%anim)
{
   if (isObject(%client.player))
      %client.player.playCelAnimation(%anim);
}

function serverCmdPlayDeath(%client)
{
   if (isObject(%client.player))
      %client.player.playDeathAnimation();
}



