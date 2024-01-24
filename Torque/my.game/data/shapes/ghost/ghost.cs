//-----------------------------------------------------------------------------
// Torque Game Engine 
// Copyright (C) GarageGames.com, Inc.
//-----------------------------------------------------------------------------

datablock StaticShapeData(ghost)
{
   // The category variable determins where the item
   // shows up in the mission editor's creator tree.
   // Path is relative to where the script is executed from.
   category = "hauntedhouse";
   shapeFile = "~/data/shapes/ghost/ghost.dts";
   isPlaying = 1;
  
   
   preload = true;


};

function ghost::onAdd(%this, %obj)
{
   %obj.playThread(0, "ambient");
}