//-----------------------------------------------------------------------------
// Torque Game Engine 
// Copyright (C) GarageGames.com, Inc.
//-----------------------------------------------------------------------------

// Game duration in secs, no limit if the duration is set to 0
$Game::Duration = 20 * 60;

// When a client score reaches this value, the game is ended.
$Game::EndGameScore = 30;

// Pause while looking over the end game screen (in secs)
$Game::EndGamePause = 10;


//-----------------------------------------------------------------------------
//  Functions that implement game-play
//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

function onServerCreated()
{
   // Server::GameType is sent to the master server.
   // This variable should uniquely identify your game and/or mod.
   $Server::GameType = "FPS Starter Kit";

   // Server::MissionType sent to the master server.  Clients can
   // filter servers based on mission type.
   $Server::MissionType = "Deathmatch";

   // GameStartTime is the sim time the game started. Used to calculated
   // game elapsed time.
   $Game::StartTime = 0;

   // Load up all datablocks, objects etc.  This function is called when
   // a server is constructed.
   exec("common/server/lightingSystem.cs");
   exec("./audioProfiles.cs");
   exec("./envAudioProfiles.cs");
   exec("./camera.cs");
   exec("./markers.cs"); 
   exec("./triggers.cs"); 
   exec("./shapeBase.cs");
   exec("./item.cs");
   exec("./environment.cs");
   exec("./staticShape.cs");
   exec("./radiusDamage.cs");
   exec("./environment.cs");
   exec("./player.cs");
   exec("./chimneyfire.cs");
   exec("./aiPlayer.cs");
   exec("./sgExamples.cs");
   exec("./vehicle.cs");
   exec("./car.cs");
   exec("./triggers-car.cs");
   exec("./triggers-door.cs");
   exec("./triggers-puzzle.cs");

   // Keep track of when the game started
   $Game::StartTime = $Sim::Time;
}

function onServerDestroyed()
{
   // This function is called as part of a server shutdown.
}


//-----------------------------------------------------------------------------

function onMissionLoaded()
{
   // Called by loadMission() once the mission is finished loading.
   // Nothing special for now, just start up the game play.
   startGame();
}

function onMissionEnded()
{
   // Called by endMission(), right before the mission is destroyed

   // Normally the game should be ended first before the next
   // mission is loaded, this is here in case loadMission has been
   // called directly.  The mission will be ended if the server
   // is destroyed, so we only need to cleanup here.
   
   cancel($Game::Schedule);
   $Game::Running = false;
   $Game::Cycling = false;
}


//-----------------------------------------------------------------------------
function startBots()
{
   // Start the first Kitty
   new ScriptObject(KittyManager) {};
   MissionCleanup.add(KittyManager);
   KittyManager.think();
   
   // Start the second Kitty
   new ScriptObject(KittyManager2) {};
   MissionCleanup.add(KittyManager2);
   KittyManager2.think();
   
   // Start the Ghost
   new ScriptObject(ToyManager) {};
   MissionCleanup.add(ToyManager);
   ToyManager.think();
}

function stopBots()
{
   // Stop the managers
   KittyManager.delete();
   ToyManager.delete();
}

//-----------------------------------------------------------------------------

function placeBuggy()
{
 if (!isObject($NewBuggy))
 {
   $NewBuggy = new WheeledVehicle()
   {
      canSaveDynamicFields = "1";
      position = "162.728 265.52 126.212";
      rotation = "-0.0403224 0.0338483 0.998613 71.6565";
      scale = "1 1 1";
      dataBlock = "DefaultCar";
      disableMove = "0";
      onGroup = "Default Value";
      mountable = "1";
   };
   MissionCleanup.add($NewBuggy);
 }
}

//-----------------------------------------------------------------------------

function startSun()
{
  if (!isObject($SunObj))
  {
	$SunObj = new Sun(Sun)
	{
		canSaveDynamicFields = "1";
		azimuth = "0";
		elevation = "-90";
		color = "0.988 0.985 0.98 1";
		ambient = "0.5 0.5 0.5 1";
		CastsShadows = "1";
		direction = "1 0.57735 -0.57735";
		position = "1 1 1";
		locked = "true";
		rotation = "1 0 0 0";
		scale = "1 1 1";
	};
	MissionCleanup.add($SunObj);
  }
}

function stopSun()
{
   if (isObject($SunObj))
      $SunObj.delete();
   $SunObj = "";
}

//-----------------------------------------------------------------------------

function startSnowStorm()
{
   if (!isObject($SnowStorm))
   {
      $SnowStorm = new Precipitation(Snowstorm) {
         canSaveDynamicFields = "1";
         position = "-3.2741 -228.279 99.7809";
         rotation = "1 0 0 0";
         scale = "1 1 1";
         nameTag = "Snowstorm";
         dataBlock = "Snowstorm";
         minSpeed = "1";
         maxSpeed = "1";
         minMass = "0.5";
         maxMass = "1";
         maxTurbulence = "10";
         turbulenceSpeed = "0.1";
         rotateWithCamVel = "0";
         useTurbulence = "1";
         numDrops = "1700";
         boxWidth = "150";
         boxHeight = "100";
         doCollision = "0";
      };
      
      MissionCleanup.add($SnowStorm);
   }
   
   if (!isObject($SnowParticles))
   {
      $SnowParticles = new Precipitation(SnowParticle) {
         canSaveDynamicFields = "1";
         position = "25.7111 -201.737 100.477";
         rotation = "1 0 0 0";
         scale = "1 1 1";
         nameTag = "Snow";
         dataBlock = "HeavySnow";
         minSpeed = "0.1";
         maxSpeed = "0.7";
         minMass = "1";
         maxMass = "2";
         maxTurbulence = "10";
         turbulenceSpeed = "1";
         rotateWithCamVel = "0";
         useTurbulence = "1";
         numDrops = "2600";
         boxWidth = "200";
         boxHeight = "100";
         doCollision = "0";
      };
      
      MissionCleanup.add($SnowParticles);
   }
}

function stopSnowStorm()
{
   if (isObject($SnowStorm))
      $SnowStorm.delete();
   $SnowStorm = "";
   
   if (isObject($SnowParticles))
      $SnowParticles.delete();
   $SnowParticles = "";
}

//-----------------------------------------------------------------------------

function placeDoorBarrierPainting()
{
   $DoorBarrierPainting = new InteriorInstance() {
      canSaveDynamicFields = "1";
      position = "239.708 302.69 129.216";
      rotation = "0 0 1 224.571";
      scale = "1 1 1";
      interiorFile = "~/data/interiors/Paintings/painting011.dif";
      useGLLighting = "0";
      showTerrainInside = "0";
   };
   
   MissionCleanup.add($DoorBarrierPainting);
}

function placePaintingPuzzle()
{
   $PaintingPuzzle = new InteriorInstance() {
      canSaveDynamicFields = "1";
      position = "244.486 314.075 136.336";
      rotation = "0 0 -1 46.5921";
      scale = "0.5 0.5 0.5";
      interiorFile = "~/data/interiors/Paintings/painting128.dif";
      useGLLighting = "0";
      showTerrainInside = "0";
   };
}

//-----------------------------------------------------------------------------

function startGame()
{
   if ($Game::Running) {
      error("startGame: End the game first!");
      return;
   }

   // Inform the client we're starting up
   for( %clientIndex = 0; %clientIndex < ClientGroup.getCount(); %clientIndex++ ) {
      %cl = ClientGroup.getObject( %clientIndex );
      commandToClient(%cl, 'GameStart');

      // Other client specific setup..
      %cl.score = 0;
   }

   // Start the game timer
   if ($Game::Duration)
      $Game::Schedule = schedule($Game::Duration * 1000, 0, "onGameDurationEnd" );
   $Game::Running = true;
   
   // Start the bots
   startBots();
   
   // Start the sun
   startSun();
   
   // Start the snowstorm
   startSnowStorm();
   
   // Place door barrier painting
   placeDoorBarrierPainting();
   
   // Place puzzle painting
   placePaintingPuzzle();
}

function endGame()
{
   if (!$Game::Running)  {
      error("endGame: No game running!");
      return;
   }
   
   // Stop the bots
   stopBots();
   
   // Stop the sun
   stopSun();
   
   // Stop the snowstorm
   stopSnowStorm();

   // Stop any game timers
   cancel($Game::Schedule);

   // Inform the client the game is over
   for( %clientIndex = 0; %clientIndex < ClientGroup.getCount(); %clientIndex++ ) {
      %cl = ClientGroup.getObject( %clientIndex );
      commandToClient(%cl, 'GameEnd');
   }

   // Delete all the temporary mission objects
   resetMission();
   $Game::Running = false;
}

function onGameDurationEnd()
{
   // This "redirect" is here so that we can abort the game cycle if
   // the $Game::Duration variable has been cleared, without having
   // to have a function to cancel the schedule.
   if ($Game::Duration && !isObject(EditorGui))
      cycleGame();
}


//-----------------------------------------------------------------------------

function cycleGame()
{
   // This is setup as a schedule so that this function can be called
   // directly from object callbacks.  Object callbacks have to be
   // carefull about invoking server functions that could cause
   // their object to be deleted.
   if (!$Game::Cycling) {
      $Game::Cycling = true;
      $Game::Schedule = schedule(0, 0, "onCycleExec");
   }
}

function onCycleExec()
{
   // End the current game and start another one, we'll pause for a little
   // so the end game victory screen can be examined by the clients.
   endGame();
   $Game::Schedule = schedule($Game::EndGamePause * 1000, 0, "onCyclePauseEnd");
}

function onCyclePauseEnd()
{
   $Game::Cycling = false;

   // Just cycle through the missions for now.
   %search = $Server::MissionFileSpec;
   for (%file = findFirstFile(%search); %file !$= ""; %file = findNextFile(%search)) {
      if (%file $= $Server::MissionFile) {
         // Get the next one, back to the first if there
         // is no next.
         %file = findNextFile(%search);
         if (%file $= "")
           %file = findFirstFile(%search);
         break;
      }
   }
   loadMission(%file);
}


//-----------------------------------------------------------------------------
// GameConnection Methods
// These methods are extensions to the GameConnection class. Extending
// GameConnection make is easier to deal with some of this functionality,
// but these could also be implemented as stand-alone functions.
//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

function GameConnection::onClientEnterGame(%this)
{
   commandToClient(%this, 'SyncClock', $Sim::Time - $Game::StartTime);

   // Create a new camera object.
   %this.camera = new Camera() {
      dataBlock = Observer;
   };
   MissionCleanup.add( %this.camera );
   %this.camera.scopeToClient(%this);

   // Setup game parameters, the onConnect method currently starts
   // everyone with a 0 score.
   %this.score = 0;

   // Create a player object.
   %this.spawnPlayer();
}

function GameConnection::onClientLeaveGame(%this)
{
   if (isObject(%this.camera))
      %this.camera.delete();
   if (isObject(%this.player))
      %this.player.delete();
}


//-----------------------------------------------------------------------------

function GameConnection::onLeaveMissionArea(%this)
{
   // The control objects invoked this method when they
   // move out of the mission area.
}

function GameConnection::onEnterMissionArea(%this)
{
   // The control objects invoked this method when they
   // move back into the mission area.
}


//-----------------------------------------------------------------------------

function GameConnection::onDeath(%this, %sourceObject, %sourceClient, %damageType, %damLoc)
{
   // Clear out the name on the corpse
   %this.player.setShapeName("");

   // Switch the client over to the death cam and unhook the player object.
   if (isObject(%this.camera) && isObject(%this.player)) {
      %this.camera.setMode("Corpse",%this.player);
      %this.setControlObject(%this.camera);
   }
   %this.player = 0;

   // Doll out points and display an appropriate message
   if (%damageType $= "Suicide" || %sourceClient == %this) {
      %this.incScore(-1);
      messageAll('MsgClientKilled','%1 takes his own life!',%this.name);
   }
   else {
      %sourceClient.incScore(1);
      messageAll('MsgClientKilled','%1 gets nailed by %2!',%this.name,%sourceClient.name);
      if (%sourceClient.score >= $Game::EndGameScore)
         cycleGame();
   }
}


//-----------------------------------------------------------------------------

function GameConnection::spawnPlayer(%this)
{
   // Combination create player and drop him somewhere
   %spawnPoint = pickSpawnPoint();
   %this.createPlayer(%spawnPoint);
}   


//-----------------------------------------------------------------------------

function GameConnection::createPlayer(%this, %spawnPoint)
{
   if (%this.player > 0)  {
      // The client should not have a player currently
      // assigned.  Assigning a new one could result in 
      // a player ghost.
      error( "Attempting to create an angus ghost!" );
   }

   // Create the player object
   %player = new Player() {
      dataBlock = PlayerBody;
      client = %this;
   };
   MissionCleanup.add(%player);

   // Player setup...
   %player.setTransform(%spawnPoint);
   %player.setShapeName(%this.name);
   
   // Starting equipment
   //%player.setInventory(Crossbow,1);
   //%player.setInventory(CrossbowAmmo,10);
   //%player.mountImage(CrossbowImage,0);

   // Update the camera to start with the player
   %this.camera.setTransform(%player.getEyeTransform());

   // Give the client control of the player
   %this.player = %player;
   %this.setControlObject(%player);
}


//-----------------------------------------------------------------------------
// Support functions
//-----------------------------------------------------------------------------

function pickSpawnPoint() 
{
   %groupName = "MissionGroup/PlayerDropPoints";
   %group = nameToID(%groupName);

   if (%group != -1) {
      %count = %group.getCount();
      if (%count != 0) {
         %index = getRandom(%count-1);
         %spawn = %group.getObject(%index);
         return %spawn.getTransform();
      }
      else
         error("No spawn points found in " @ %groupName);
   }
   else
      error("Missing spawn points group " @ %groupName);

   // Could be no spawn points, in which case we'll stick the
   // player at the center of the world.
   return "0 0 300 1 0 0 0";
}
