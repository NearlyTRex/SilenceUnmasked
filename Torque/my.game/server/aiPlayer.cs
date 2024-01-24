//-----------------------------------------------------------------------------
// Torque Game Engine 
// Copyright (C) GarageGames.com, Inc.
//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------
// AIPlayer callbacks
// The AIPlayer class implements the following callbacks:
//
//    PlayerData::onStuck(%this,%obj)
//    PlayerData::onUnStuck(%this,%obj)
//    PlayerData::onStop(%this,%obj)
//    PlayerData::onMove(%this,%obj)
//    PlayerData::onReachDestination(%this,%obj)
//    PlayerData::onTargetEnterLOS(%this,%obj)
//    PlayerData::onTargetExitLOS(%this,%obj)
//    PlayerData::onAdd(%this,%obj)
//
// Since the AIPlayer doesn't implement it's own datablock, these callbacks
// all take place in the PlayerData namespace.
//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------
// Demo Pathed AIPlayer.
//-----------------------------------------------------------------------------

datablock PlayerData(KittyCat)
{
   shapeFile = "~/data/shapes/cat/Cat.dts";
};

datablock PlayerData(KittyCat2)
{
   shapeFile = "~/data/shapes/cat/Cat.dts";
};

datablock PlayerData(ToyCar)
{
   shapeFile = "~/data/shapes/ghost/ghost.dts";
};

//-----------------------------------------------------------------------------

function KittyCat::onReachDestination(%this,%obj)
{
   // Moves to the next node on the path.
   // Override for all player. Normally we'd override this for only
   // a specific player datablock or class of players.
   if (%obj.path !$= "") {
      if (%obj.currentNode == %obj.targetNode)
         %this.onEndOfPath(%obj,%obj.path);
      else
         %obj.moveToNextNode();
   }
}

function KittyCat::onEndOfPath(%this,%obj,%path)
{
   %obj.nextTask();
}

function KittyCat::onEndSequence(%this,%obj,%slot)
{
   echo("Sequence Done!");
   %obj.stopThread(%slot);
   %obj.nextTask();
}

//-----------------------------------------------------------------------------

function KittyCat2::onReachDestination(%this,%obj)
{
   // Moves to the next node on the path.
   // Override for all player. Normally we'd override this for only
   // a specific player datablock or class of players.
   if (%obj.path !$= "") {
      if (%obj.currentNode == %obj.targetNode)
         %this.onEndOfPath(%obj,%obj.path);
      else
         %obj.moveToNextNode();
   }
}

function KittyCat2::onEndOfPath(%this,%obj,%path)
{
   %obj.nextTask();
}

function KittyCat2::onEndSequence(%this,%obj,%slot)
{
   echo("Sequence Done!");
   %obj.stopThread(%slot);
   %obj.nextTask();
}

//-----------------------------------------------------------------------------

function ToyCar::onReachDestination(%this,%obj)
{
   // Moves to the next node on the path.
   // Override for all player. Normally we'd override this for only
   // a specific player datablock or class of players.
   if (%obj.path !$= "") {
      if (%obj.currentNode == %obj.targetNode)
         %this.onEndOfPath(%obj,%obj.path);
      else
         %obj.moveToNextNode();
   }
}

function ToyCar::onEndOfPath(%this,%obj,%path)
{
   %obj.nextTask();
}

function ToyCar::onEndSequence(%this,%obj,%slot)
{
   echo("Sequence Done!");
   %obj.stopThread(%slot);
   %obj.nextTask();
}


//-----------------------------------------------------------------------------
// AIPlayer static functions
//-----------------------------------------------------------------------------

function AIPlayer::spawnKitty(%name,%spawnPoint)
{
   // Create the demo player object
   %player = new AiPlayer() {
      dataBlock = KittyCat;
      path = "";
   };
   MissionCleanup.add(%player);
   %player.setShapeName(%name);
   %player.setTransform(%spawnPoint);
   return %player;
}

function AIPlayer::spawnKitty2(%name,%spawnPoint)
{
   // Create the demo player object
   %player = new AiPlayer() {
      dataBlock = KittyCat2;
      path = "";
   };
   MissionCleanup.add(%player);
   %player.setShapeName(%name);
   %player.setTransform(%spawnPoint);
   return %player;
}

function AIPlayer::spawnToy(%name,%spawnPoint)
{
   // Create the demo player object
   %player = new AiPlayer() {
      dataBlock = ToyCar;
      path = "";
   };
   MissionCleanup.add(%player);
   %player.setShapeName(%name);
   %player.setTransform(%spawnPoint);
   return %player;
}

function AIPlayer::spawnOnPathKitty(%name,%path)
{
   // Spawn a player and place him on the first node of the path
   if (!isObject(%path))
      return 0;
   %node = %path.getObject(0);
   %player = AIPlayer::spawnKitty(%name,%node.getTransform());
   return %player;
}

function AIPlayer::spawnOnPathKitty2(%name,%path)
{
   // Spawn a player and place him on the first node of the path
   if (!isObject(%path))
      return 0;
   %node = %path.getObject(0);
   %player = AIPlayer::spawnKitty2(%name,%node.getTransform());
   return %player;
}

function AIPlayer::spawnOnPathToy(%name,%path)
{
   // Spawn a player and place him on the first node of the path
   if (!isObject(%path))
      return 0;
   %node = %path.getObject(0);
   %player = AIPlayer::spawnToy(%name,%node.getTransform());
   return %player;
}


//-----------------------------------------------------------------------------
// AIPlayer methods 
//-----------------------------------------------------------------------------

function AIPlayer::followPath(%this,%path,%node)
{
   // Start the player following a path
   %this.stopThread(0);
   if (!isObject(%path)) {
      %this.path = "";
      return;
   }
   if (%node > %path.getCount() - 1)
      %this.targetNode = %path.getCount() - 1;
   else
      %this.targetNode = %node;
   if (%this.path $= %path)
      %this.moveToNode(%this.currentNode);
   else {
      %this.path = %path;
      %this.moveToNode(0);
   }
}

function AIPlayer::moveToNextNode(%this)
{
   if (%this.targetNode < 0 || %this.currentNode < %this.targetNode) {
      if (%this.currentNode < %this.path.getCount() - 1)
         %this.moveToNode(%this.currentNode + 1);
      else
         %this.moveToNode(0);
   }
   else
      if (%this.currentNode == 0)
         %this.moveToNode(%this.path.getCount() - 1);
      else
         %this.moveToNode(%this.currentNode - 1);
}

function AIPlayer::moveToNode(%this,%index)
{
   // Move to the given path node index
   %this.currentNode = %index;
   %node = %this.path.getObject(%index);
   %this.setMoveDestination(%node.getTransform(), %index == %this.targetNode);
}


//-----------------------------------------------------------------------------
//
//-----------------------------------------------------------------------------

function AIPlayer::pushTask(%this,%method)
{
   if (%this.taskIndex $= "") {
      %this.taskIndex = 0;
      %this.taskCurrent = -1;
   }
   %this.task[%this.taskIndex] = %method; 
   %this.taskIndex++;
   if (%this.taskCurrent == -1)
      %this.executeTask(%this.taskIndex - 1);
}

function AIPlayer::clearTasks(%this)
{
   %this.taskIndex = 0;
   %this.taskCurrent = -1;
}

function AIPlayer::nextTask(%this)
{
   if (%this.taskCurrent != -1)
      if (%this.taskCurrent < %this.taskIndex - 1)
         %this.executeTask(%this.taskCurrent++);
      else
         %this.taskCurrent = -1;
}

function AIPlayer::executeTask(%this,%index)
{
   %this.taskCurrent = %index;
   eval(%this.getId() @ "." @ %this.task[%index] @ ";");
}


//-----------------------------------------------------------------------------

function AIPlayer::singleShot(%this)
{
   // The shooting delay is used to pulse the trigger
   %this.setImageTrigger(0,true);
   %this.setImageTrigger(0,false);
   %this.trigger = %this.schedule(%this.shootingDelay,singleShot);
}


//-----------------------------------------------------------------------------

function AIPlayer::wait(%this,%time)
{
   %this.schedule(%time * 1000,"nextTask");
}

function AIPlayer::done(%this,%time)
{
   %this.schedule(0,"delete");
}

function AIPlayer::fire(%this,%bool)
{
   if (%bool) {
      cancel(%this.trigger);
      %this.singleShot();
   }
   else
      cancel(%this.trigger);
   %this.nextTask();
}

function AIPlayer::aimAt(%this,%object)
{
   echo("Aim: " @ %object);
   %this.setAimObject(%object);
   %this.nextTask();
}

function AIPlayer::animate(%this,%seq)
{
   //%this.stopThread(0);
   //%this.playThread(0,%seq);
   %this.setActionThread(%seq);
}


//-----------------------------------------------------------------------------

function KittyManager::think(%this)
{
   // Kitty Spawning
   if (!isObject(%this.player))
      %this.player = %this.spawn();
   %this.schedule(500,think);
}

function KittyManager::spawn(%this)
{
   %bot = AIPlayer::spawnOnPathKitty( "Kitty", "MissionGroup/Path1" );
   %bot.followPath( "MissionGroup/Path1", -1 );

   return %bot;
}

//-----------------------------------------------------------------------------

function KittyManager2::think(%this)
{
   // Kitty Spawning
   if (!isObject(%this.player))
      %this.player = %this.spawn();
   %this.schedule(500,think);
}

function KittyManager2::spawn(%this)
{
   %bot = AIPlayer::spawnOnPathKitty2( "Kitty2", "MissionGroup/Path1" );
   %bot.followPath( "MissionGroup/Path1", -1 );

   return %bot;
}

//-----------------------------------------------------------------------------

function ToyManager::think(%this)
{
   // Toy Spawning
   if (!isObject(%this.player))
      %this.player = %this.spawn();
   %this.schedule(500,think);
}

function ToyManager::spawn(%this)
{
   %bot = AIPlayer::spawnOnPathToy( "Toy", "MissionGroup/Path2" );
   %bot.followPath( "MissionGroup/Path2", -1 );

   return %bot;
}

//-----------------------------------------------------------------------------




