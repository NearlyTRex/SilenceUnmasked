//-----------------------------------------------------------------------------
// Torque Game Engine
// Copyright (C) GarageGames.com, Inc.
//-----------------------------------------------------------------------------

// Channel assignments (channel 0 is unused in-game).

$GuiAudioType     = 1;
$SimAudioType     = 2;
$MessageAudioType = 3;
$MusicAudioType   = 4;
$Music2AudioType  = 5;

//==========================================================================

new AudioDescription(AudioGui)
{
   volume   = 1.0;
   isLooping= false;
   is3D     = false;
   type     = $GuiAudioType;
};

new AudioDescription(AudioMessage)
{
   volume   = 1.0;
   isLooping= false;
   is3D     = false;
   type     = $MessageAudioType;
};

new AudioDescription(ClockStrike)
{
   volume   = 2.0;
   isLooping = true;
   is3D     = false;
   type     = $MusicAudioType;
};

new AudioDescription(WomanSob)
{
   volume   = 2.0;
   isLooping = true;
   is3D     = false;
   type     = $Music2AudioType;
};

//==========================================================================

new AudioProfile(AudioButtonOver)
{
   filename = "~/data/sound/buttonOver.wav";
   description = "AudioGui";
   preload = true;
};

new AudioProfile(ClockStrikeStart) 
{ 
   filename = "~/data/sound/ClockStrike.wav";
   description = "ClockStrike"; 
   preload = false; 
};

new AudioProfile(WomanSobStart) 
{ 
   filename = "~/data/sound/WomanSob.wav";
   description = "WomanSob"; 
   preload = false; 
};

//==========================================================================
