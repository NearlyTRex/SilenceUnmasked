//-------------- Sound for Rain -------------------------------------
//datablock AudioProfile(Universal_Rain_Light_1)
//{
//   filename    = "~/data/sound/fx/environment/rain_light_1.wav";
//   description = AudioLooping2d;
//};
//the description is already defined in ~/fps/server/scripts/audioprofiles.cs
//
//-------------------- RAIN -----------------------------------------
datablock PrecipitationData(Rain) 
{ 
   type = 1; 
   materialList = "~/data/fx/precipitation/rainstorm.dml"; 
   //soundProfile = "Universal_Rain_Light_1";
   sizeX = 0.10; 
   sizeY = 0.10; 

   movingBoxPer = 0.35; 
   divHeightVal = 1.5; 
   sizeBigBox = 1; 
   topBoxSpeed = 20; 
   frontBoxSpeed = 30; 
   topBoxDrawPer = 0.5; 
   bottomDrawHeight = 40; 
   skipIfPer = -0.3; 
   bottomSpeedPer = 1.0; 
   frontSpeedPer = 1.5; 
   frontRadiusPer = 0.5; 
};
//-------------------- SNOW -----------------------------------------------------
datablock PrecipitationData(Snow) 
{ 
   type = 1; 
   materialList = "~/data/environment/snowstorm.dml";
   sizeX = 0.10; 
   sizeY = 0.10;  

   movingBoxPer = 0.35; 
   divHeightVal = 1.5; 
   sizeBigBox = 1; 
   topBoxSpeed = 20; 
   frontBoxSpeed = 30; 
   topBoxDrawPer = 0.5; 
   bottomDrawHeight = 40; 
   skipIfPer = -0.3; 
   bottomSpeedPer = 1.0; 
   frontSpeedPer = 1.5; 
   frontRadiusPer = 0.5; 
}; 

