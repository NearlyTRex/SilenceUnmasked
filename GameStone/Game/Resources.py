## Silence Unmasked
## Waterstone Productions

# Local imports
from Constants import *

########################################################################################
def Convert(x, y, z):
  
  # Convert standard screen coordinate system to OpenGL
  newx = x - (SCREEN_WIDTH / 2)
  newy = -(y - (SCREEN_HEIGHT / 2))
  newz = z
  
  # Return new coordinates
  return (newx, newy, newz)
########################################################################################

########################################################################################
Sprites = []
########################################################################################
Sprites.append(["Loader", "Loader.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["Title", "Title.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["Inventory", "Inventory.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["MainMenu", "MainMenu.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["MainMenuDifficulty", "MainMenuDifficulty.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["Instructions1", "Instructions1.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["Instructions2", "Instructions2.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
########################################################################################
Sprites.append(["RoomAreaCar", "RoomAreaCar.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomAreaSnowplow", "RoomAreaSnowplow.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomCabin", "RoomCabin.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomCabinFront", "RoomCabinFront.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomCaveEntrance", "RoomCaveEntrance.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomCaveExit", "RoomCaveExit.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomDriveway1", "RoomDriveway1.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomDriveway2", "RoomDriveway2.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseBack", "RoomHouseBack.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseBathroom", "RoomHouseBathroom.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseBedHall", "RoomHouseBedHall.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseBedroom", "RoomHouseBedroom.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseCourtyard", "RoomHouseCourtyard.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseDen", "RoomHouseDen.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseFront", "RoomHouseFront.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseFrontHallLower", "RoomHouseFrontHallLower.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseFrontHallUpper", "RoomHouseFrontHallUpper.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseGarage", "RoomHouseGarage.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseGuestroom", "RoomHouseGuestroom.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseHiddenRoom", "RoomHouseHiddenRoom.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseHiddenRoomAxe", "RoomHouseHiddenRoomAxe.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseKitchen", "RoomHouseKitchen.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseLaundry", "RoomHouseLaundry.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseLinen", "RoomHouseLinen.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseLivingRoom", "RoomHouseLivingRoom.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseMusicRoom", "RoomHouseMusicRoom.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHousePaintingHall", "RoomHousePaintingHall.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHousePantry", "RoomHousePantry.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHousePatio", "RoomHousePatio.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseSideHall1", "RoomHouseSideHall1.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseSideHall2", "RoomHouseSideHall2.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomHouseStudy", "RoomHouseStudy.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["RoomValley", "RoomValley.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
########################################################################################
Sprites.append(["CutsceneAccident", "CutsceneAccident.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneBunny", "CutsceneBunny.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneCave1", "CutsceneCave1.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneCave2", "CutsceneCave2.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneCredits1", "CutsceneCredits1.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneCredits2", "CutsceneCredits2.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneCredits3", "CutsceneCredits3.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneCredits4", "CutsceneCredits4.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneDark", "CutsceneDark.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneDiary", "CutsceneDiary.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneDriving", "CutsceneDriving.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneEvil", "CutsceneEvil.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneExplosion", "CutsceneExplosion.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneFall", "CutsceneFall.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneFathersGrave", "CutsceneFathersGrave.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneGameOver", "CutsceneGameOver.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneHallucination", "CutsceneHallucination.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneHouseFront", "CutsceneHouseFront.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneHouseHall", "CutsceneHouseHall.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneKnives", "CutsceneKnives.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneLocket1", "CutsceneLocket1.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneLocket2", "CutsceneLocket2.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneMentalHospital", "CutsceneMentalHospital.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutscenePainting", "CutscenePainting.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneScrapbook", "CutsceneScrapbook.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneShadowMan", "CutsceneShadowMan.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneSnowplow", "CutsceneSnowplow.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
Sprites.append(["CutsceneStevens", "CutsceneStevens.sx", (SCREEN_X, SCREEN_Y, SCREEN_Z)])
########################################################################################
Sprites.append(["ButtonGameInventory", "ButtonGameInventory.sx", Convert(90, 454, EVENT_DEPTH)])
Sprites.append(["ButtonGameSave", "ButtonGameSave.sx", Convert(564, 434, EVENT_DEPTH)])
Sprites.append(["ButtonGameQuit", "ButtonGameQuit.sx", Convert(564, 464, EVENT_DEPTH)])
Sprites.append(["ButtonMainMenuNewGame", "ButtonMainMenuNewGame.sx", Convert(20, 248, EVENT_DEPTH)])
Sprites.append(["ButtonMainMenuContinue", "ButtonMainMenuContinue.sx", Convert(20, 356, EVENT_DEPTH)])
Sprites.append(["ButtonMainMenuQuit", "ButtonMainMenuQuit.sx", Convert(20, 462, EVENT_DEPTH)])
Sprites.append(["ButtonMainMenuEasy", "ButtonMainMenuEasy.sx", Convert(24, 310, EVENT_DEPTH)])
Sprites.append(["ButtonMainMenuHard", "ButtonMainMenuHard.sx", Convert(151, 313, EVENT_DEPTH)])
########################################################################################
Sprites.append(["Cloak", "Cloak.sx", Convert(235, 282, EVENT_DEPTH)])
Sprites.append(["Cursor", "CursorNew.sx", Convert(0, 0, EVENT_DEPTH)])
########################################################################################
Sprites.append(["ObjectBucket", "Objects.sx", Convert(OBJECT_X1, OBJECT_Y1, OBJECT_Z)])
Sprites.append(["ObjectCrowbar", "Objects.sx", Convert(OBJECT_X2, OBJECT_Y1, OBJECT_Z)])
Sprites.append(["ObjectHanger", "Objects.sx", Convert(OBJECT_X3, OBJECT_Y1, OBJECT_Z)])
Sprites.append(["ObjectThinner", "Objects.sx", Convert(OBJECT_X4, OBJECT_Y1, OBJECT_Z)])
Sprites.append(["ObjectOpener", "Objects.sx", Convert(OBJECT_X5, OBJECT_Y1, OBJECT_Z)])
Sprites.append(["ObjectKnob", "Objects.sx", Convert(OBJECT_X1, OBJECT_Y2, OBJECT_Z)])
Sprites.append(["ObjectGas", "Objects.sx", Convert(OBJECT_X2, OBJECT_Y2, OBJECT_Z)])
Sprites.append(["ObjectPins", "Objects.sx", Convert(OBJECT_X3, OBJECT_Y2, OBJECT_Z)])
Sprites.append(["ObjectLocket1", "Objects.sx", Convert(OBJECT_X4, OBJECT_Y2, OBJECT_Z)])
Sprites.append(["ObjectLocket2", "Objects.sx", Convert(OBJECT_X5, OBJECT_Y2, OBJECT_Z)])
Sprites.append(["ObjectDynamite", "Objects.sx", Convert(OBJECT_X1, OBJECT_Y3, OBJECT_Z)])
Sprites.append(["ObjectMatches", "Objects.sx", Convert(OBJECT_X2, OBJECT_Y3, OBJECT_Z)])
Sprites.append(["ObjectBible", "Objects.sx", Convert(OBJECT_X3, OBJECT_Y3, OBJECT_Z)])
Sprites.append(["ObjectAxe", "Objects.sx", Convert(OBJECT_X4, OBJECT_Y3, OBJECT_Z)])
Sprites.append(["ObjectMusicBoxKeys", "Objects.sx", Convert(OBJECT_X5, OBJECT_Y3, OBJECT_Z)])
Sprites.append(["ObjectCourtyardKey", "Objects.sx", Convert(OBJECT_X1, OBJECT_Y4, OBJECT_Z)])
Sprites.append(["ObjectBedroomHallKey", "Objects.sx", Convert(OBJECT_X2, OBJECT_Y4, OBJECT_Z)])
Sprites.append(["ObjectBathroomKey", "Objects.sx", Convert(OBJECT_X3, OBJECT_Y4, OBJECT_Z)])
Sprites.append(["ObjectGarageKey", "Objects.sx", Convert(OBJECT_X4, OBJECT_Y4, OBJECT_Z)])
Sprites.append(["ObjectStudyKey", "Objects.sx", Convert(OBJECT_X5, OBJECT_Y4, OBJECT_Z)])
########################################################################################
Sprites.append(["EntityAreaCarDoor", "EntityAreaCarDoor.sx", Convert(339, 215, EVENT_DEPTH)])
Sprites.append(["EntityAreaSnowplowDoor1", "EntityAreaSnowplowDoor1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityAreaSnowplowDoor2", "EntityAreaSnowplowDoor2.sx", Convert(145, 281, EVENT_DEPTH)])
Sprites.append(["EntityCabinDoor1", "EntityCabinDoor1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityCabinDoor2", "EntityCabinDoor2.sx", Convert(44, 259, EVENT_DEPTH)])
Sprites.append(["EntityCabinDoor3", "EntityCabinDoor3.sx", Convert(506, 126, EVENT_DEPTH)])
Sprites.append(["EntityCabinFrontDoor1", "EntityCabinFrontDoor1.sx", Convert(4, 311, EVENT_DEPTH)])
Sprites.append(["EntityCabinFrontDoor2", "EntityCabinFrontDoor2.sx", Convert(375, 202, EVENT_DEPTH)])
Sprites.append(["EntityCaveEntranceDoor1", "EntityCaveEntranceDoor1.sx", Convert(70, 351, EVENT_DEPTH)])
Sprites.append(["EntityCaveEntranceDoor2", "EntityCaveEntranceDoor2.sx", Convert(568, 384, EVENT_DEPTH)])
Sprites.append(["EntityCaveExitDoor1", "EntityCaveExitDoor1.sx", Convert(44, 332, EVENT_DEPTH)])
Sprites.append(["EntityCaveExitDoor2", "EntityCaveExitDoor2.sx", Convert(572, 351, EVENT_DEPTH)])
Sprites.append(["EntityDriveway1Door1", "EntityDriveway1Door1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityDriveway1Door2", "EntityDriveway1Door2.sx", Convert(592, 367, EVENT_DEPTH)])
Sprites.append(["EntityDriveway2Door1", "EntityDriveway2Door1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityDriveway2Door2", "EntityDriveway2Door2.sx", Convert(12, 383, EVENT_DEPTH)])
Sprites.append(["EntityDriveway2Door3", "EntityDriveway2Door3.sx", Convert(304, 314, EVENT_DEPTH)])
Sprites.append(["EntityHouseBackDoor1", "EntityHouseBackDoor1.sx", Convert(121, 248, EVENT_DEPTH)])
Sprites.append(["EntityHouseBackDoor2", "EntityHouseBackDoor2.sx", Convert(584, 321, EVENT_DEPTH)])
Sprites.append(["EntityHouseBathroomDoor", "EntityHouseBathroomDoor.sx", Convert(567, 236, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallDoor1", "EntityHouseBedHallDoor1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallDoor2", "EntityHouseBedHallDoor2.sx", Convert(35, 230, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallDoor3", "EntityHouseBedHallDoor3.sx", Convert(142, 136, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallDoor4", "EntityHouseBedHallDoor4.sx", Convert(195, 145, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallDoor5", "EntityHouseBedHallDoor5.sx", Convert(365, 164, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallDoor6", "EntityHouseBedHallDoor6.sx", Convert(432, 230, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallDoor7", "EntityHouseBedHallDoor7.sx", Convert(564, 271, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedroomDoor", "EntityHouseBedroomDoor.sx", Convert(32, 270, EVENT_DEPTH)])
Sprites.append(["EntityHouseCourtyardDoor1", "EntityHouseCourtyardDoor1.sx", Convert(436, 206, EVENT_DEPTH)])
Sprites.append(["EntityHouseCourtyardDoor2", "EntityHouseCourtyardDoor2.sx", Convert(570, 191, EVENT_DEPTH)])
Sprites.append(["EntityHouseDenDoor1", "EntityHouseDenDoor1.sx", Convert(23, 270, EVENT_DEPTH)])
Sprites.append(["EntityHouseDenDoor2", "EntityHouseDenDoor2.sx", Convert(85, 219, EVENT_DEPTH)])
Sprites.append(["EntityHouseDenDoor3", "EntityHouseDenDoor3.sx", Convert(503, 219, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontDoor1", "EntityHouseFrontDoor1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontDoor2", "EntityHouseFrontDoor2.sx", Convert(18, 214, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontDoor3", "EntityHouseFrontDoor3.sx", Convert(258, 125, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallLowerDoor1", "EntityHouseFrontHallLowerDoor1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallLowerDoor2", "EntityHouseFrontHallLowerDoor2.sx", Convert(17, 276, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallLowerDoor3", "EntityHouseFrontHallLowerDoor3.sx", Convert(234, 255, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallLowerDoor4", "EntityHouseFrontHallLowerDoor4.sx", Convert(563, 286, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallUpperDoor1", "EntityHouseFrontHallUpperDoor1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallUpperDoor2", "EntityHouseFrontHallUpperDoor2.sx", Convert(161, 278, EVENT_DEPTH)])
Sprites.append(["EntityHouseGarageDoor1", "EntityHouseGarageDoor1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHouseGarageDoor2", "EntityHouseGarageDoor2.sx", Convert(19, 221, EVENT_DEPTH)])
Sprites.append(["EntityHouseGuestroomDoor1", "EntityHouseGuestroomDoor1.sx", Convert(88, 254, EVENT_DEPTH)])
Sprites.append(["EntityHouseGuestroomDoor2", "EntityHouseGuestroomDoor2.sx", Convert(540, 305, EVENT_DEPTH)])
Sprites.append(["EntityHouseHiddenRoomDoor", "EntityHouseHiddenRoomDoor.sx", Convert(250, 192, EVENT_DEPTH)])
Sprites.append(["EntityHouseKitchenDoor1", "EntityHouseKitchenDoor1.sx", Convert(384, 172, EVENT_DEPTH)])
Sprites.append(["EntityHouseKitchenDoor2", "EntityHouseKitchenDoor2.sx", Convert(476, 188, EVENT_DEPTH)])
Sprites.append(["EntityHouseKitchenDoor3", "EntityHouseKitchenDoor3.sx", Convert(527, 245, EVENT_DEPTH)])
Sprites.append(["EntityHouseKitchenDoor4", "EntityHouseKitchenDoor4.sx", Convert(589, 229, EVENT_DEPTH)])
Sprites.append(["EntityHouseLaundryDoor", "EntityHouseLaundryDoor.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHouseLinenDoor1", "EntityHouseLinenDoor1.sx", Convert(74, 220, EVENT_DEPTH)])
Sprites.append(["EntityHouseLinenDoor2", "EntityHouseLinenDoor2.sx", Convert(413, 238, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomDoor1", "EntityHouseLivingRoomDoor1.sx", Convert(23, 184, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomDoor2", "EntityHouseLivingRoomDoor2.sx", Convert(126, 158, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomDoor3", "EntityHouseLivingRoomDoor3.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomDoor4", "EntityHouseLivingRoomDoor4.sx", Convert(318, 160, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomDoor5", "EntityHouseLivingRoomDoor5.sx", Convert(542, 276, EVENT_DEPTH)])
Sprites.append(["EntityHouseMusicRoomDoor1", "EntityHouseMusicRoomDoor1.sx", Convert(45, 242, EVENT_DEPTH)])
Sprites.append(["EntityHouseMusicRoomDoor2", "EntityHouseMusicRoomDoor2.sx", Convert(528, 217, EVENT_DEPTH)])
Sprites.append(["EntityHousePaintingHallDoor1", "EntityHousePaintingHallDoor1.sx", Convert(11, 208, EVENT_DEPTH)])
Sprites.append(["EntityHousePaintingHallDoor2", "EntityHousePaintingHallDoor2.sx", Convert(576, 271, EVENT_DEPTH)])
Sprites.append(["EntityHousePantryDoor", "EntityHousePantryDoor.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHousePatioDoor1", "EntityHousePatioDoor1.sx", Convert(43, 208, EVENT_DEPTH)])
Sprites.append(["EntityHousePatioDoor2", "EntityHousePatioDoor2.sx", Convert(240, 133, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall1Door1", "EntityHouseSideHall1Door1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall1Door2", "EntityHouseSideHall1Door2.sx", Convert(180, 204, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall1Door3", "EntityHouseSideHall1Door3.sx", Convert(295, 133, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall1Door4", "EntityHouseSideHall1Door4.sx", Convert(438, 207, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall2Door1", "EntityHouseSideHall2Door1.sx", Convert(BUTTON_ARROW_SX, BUTTON_ARROW_SY, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall2Door2", "EntityHouseSideHall2Door2.sx", Convert(21, 270, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall2Door3", "EntityHouseSideHall2Door3.sx", Convert(151, 215, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall2Door4", "EntityHouseSideHall2Door4.sx", Convert(334, 201, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall2Door5", "EntityHouseSideHall2Door5.sx", Convert(507, 166, EVENT_DEPTH)])
Sprites.append(["EntityHouseStudyDoor1", "EntityHouseStudyDoor1.sx", Convert(81, 243, EVENT_DEPTH)])
Sprites.append(["EntityHouseStudyDoor2", "EntityHouseStudyDoor2.sx", Convert(460, 240, EVENT_DEPTH)])
Sprites.append(["EntityValleyDoor1", "EntityValleyDoor1.sx", Convert(12, 384, EVENT_DEPTH)])
Sprites.append(["EntityValleyDoor2", "EntityValleyDoor2.sx", Convert(505, 221, EVENT_DEPTH)])
########################################################################################
Sprites.append(["EntityAreaCarObject1", "EntityObject.sx", Convert(113, 128, EVENT_DEPTH)])
Sprites.append(["EntityAreaCarObject2", "EntityObject.sx", Convert(312, 321, EVENT_DEPTH)])
Sprites.append(["EntityAreaSnowplowObject1", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityAreaSnowplowObject2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCabinObject1", "EntityObject.sx", Convert(434, 225, EVENT_DEPTH)]) # Dynamite
Sprites.append(["EntityCabinObject2", "EntityObject.sx", Convert(239, 176, EVENT_DEPTH)]) # Matches
Sprites.append(["EntityCabinFrontObject1", "EntityObject.sx", Convert(133, 49, EVENT_DEPTH)])
Sprites.append(["EntityCabinFrontObject2", "EntityObject.sx", Convert(463, 109, EVENT_DEPTH)])
Sprites.append(["EntityCabinFrontObject3", "EntityObject.sx", Convert(509, 187, EVENT_DEPTH)])
Sprites.append(["EntityCaveEntranceObject1", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCaveEntranceObject2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCaveExitObject1", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCaveExitObject2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityDriveway1Object1", "EntityObject.sx", Convert(48, 131, EVENT_DEPTH)])
Sprites.append(["EntityDriveway1Object2", "EntityObject.sx", Convert(481, 93, EVENT_DEPTH)])
Sprites.append(["EntityDriveway2Object1", "EntityObject.sx", Convert(228, 254, EVENT_DEPTH)])
Sprites.append(["EntityDriveway2Object2", "EntityObject.sx", Convert(451, 231, EVENT_DEPTH)])
Sprites.append(["EntityHouseBackObject1", "EntityObject.sx", Convert(309, 106, EVENT_DEPTH)])
Sprites.append(["EntityHouseBackObject2", "EntityObject.sx", Convert(409, 163, EVENT_DEPTH)])
Sprites.append(["EntityHouseBathroomObject1", "EntityObject.sx", Convert(399, 204, EVENT_DEPTH)]) # Bucket
Sprites.append(["EntityHouseBathroomObject2", "EntityObject.sx", Convert(35, 211, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallObject1", "EntityObject.sx", Convert(275, 151, EVENT_DEPTH)]) # Note
Sprites.append(["EntityHouseBedHallObject2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedroomObject1", "EntityObject.sx", Convert(546, 266, EVENT_DEPTH)]) # Crowbar
Sprites.append(["EntityHouseBedroomObject2", "EntityObject.sx", Convert(226, 190, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedroomObject3", "EntityObject.sx", Convert(371, 201, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedroomObject4", "EntityObject.sx", Convert(595, 180, EVENT_DEPTH)])
Sprites.append(["EntityHouseCourtyardObject1", "EntityObject.sx", Convert(215, 107, EVENT_DEPTH)])
Sprites.append(["EntityHouseCourtyardObject2", "EntityObject.sx", Convert(352, 133, EVENT_DEPTH)])
Sprites.append(["EntityHouseDenObject1", "EntityObject.sx", Convert(253, 170, EVENT_DEPTH)]) # Courtyard key
Sprites.append(["EntityHouseDenObject2", "EntityObject.sx", Convert(269, 119, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontObject1", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontObject2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallLowerObject1", "EntityObject.sx", Convert(280, 143, EVENT_DEPTH)]) # Painting
Sprites.append(["EntityHouseFrontHallLowerObject2", "EntityObject.sx", Convert(293, 62, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallUpperObject1", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallUpperObject2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseGarageObject1", "EntityObject.sx", Convert(190, 127, EVENT_DEPTH)]) # Hammer
Sprites.append(["EntityHouseGarageObject2", "EntityObject.sx", Convert(256, 125, EVENT_DEPTH)]) # Knob
Sprites.append(["EntityHouseGarageObject3", "EntityObject.sx", Convert(319, 127, EVENT_DEPTH)]) # Bulb
Sprites.append(["EntityHouseGarageObject4", "EntityObject.sx", Convert(462, 327, EVENT_DEPTH)]) # Gas opening
Sprites.append(["EntityHouseGarageObject5", "EntityObject.sx", Convert(255, 312, EVENT_DEPTH)]) # Car
Sprites.append(["EntityHouseGarageObject6", "EntityObject.sx", Convert(409, 159, EVENT_DEPTH)]) # Thinner
Sprites.append(["EntityHouseGuestroomObject1", "EntityObject.sx", Convert(478, 238, EVENT_DEPTH)]) # Bathroom key
Sprites.append(["EntityHouseGuestroomObject2", "EntityObject.sx", Convert(391, 103, EVENT_DEPTH)])
Sprites.append(["EntityHouseHiddenRoomObject1", "EntityObject.sx", Convert(470, 137, EVENT_DEPTH)]) # Bunny
Sprites.append(["EntityHouseHiddenRoomObject2", "EntityObject.sx", Convert(84, 213, EVENT_DEPTH)]) # Scrapbook
Sprites.append(["EntityHouseHiddenRoomObject3", "EntityObject.sx", Convert(324, 305, EVENT_DEPTH)]) # Axe
Sprites.append(["EntityHouseHiddenRoomObject4", "EntityObject.sx", Convert(74, 87, EVENT_DEPTH)]) # Evil Painting
Sprites.append(["EntityHouseHiddenRoomObject5", "EntityObject.sx", Convert(422, 258, EVENT_DEPTH)]) # Cot
Sprites.append(["EntityHouseHiddenRoomObject6", "EntityObject.sx", Convert(523, 56, EVENT_DEPTH)]) # Drawings
Sprites.append(["EntityHouseKitchenObject1", "EntityObject.sx", Convert(37, 263, EVENT_DEPTH)]) # Kitchen sink
Sprites.append(["EntityHouseKitchenObject2", "EntityObject.sx", Convert(258, 180, EVENT_DEPTH)]) # Red herring
Sprites.append(["EntityHouseLaundryObject1", "EntityObject.sx", Convert(293, 188, EVENT_DEPTH)]) # Garage key
Sprites.append(["EntityHouseLaundryObject2", "EntityObject.sx", Convert(141, 306, EVENT_DEPTH)])
Sprites.append(["EntityHouseLinenObject1", "EntityObject.sx", Convert(301, 163, EVENT_DEPTH)]) # Coat Hanger
Sprites.append(["EntityHouseLinenObject2", "EntityObject.sx", Convert(291, 234, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomObject1", "EntityObject.sx", Convert(449, 255, EVENT_DEPTH)]) # Bedroom hall key
Sprites.append(["EntityHouseLivingRoomObject2", "EntityObject.sx", Convert(340, 41, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomObject3", "EntityObject.sx", Convert(559, 94, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomObject4", "EntityObject.sx", Convert(232, 130, EVENT_DEPTH)])
Sprites.append(["EntityHouseMusicRoomObject1", "EntityObject.sx", Convert(171, 170, EVENT_DEPTH)]) # Record player
Sprites.append(["EntityHouseMusicRoomObject2", "EntityObject.sx", Convert(270, 170, EVENT_DEPTH)]) # Music box
Sprites.append(["EntityHouseMusicRoomObject3", "EntityObject.sx", Convert(387, 141, EVENT_DEPTH)]) # Guitar
Sprites.append(["EntityHousePaintingHallObject1", "EntityObject.sx", Convert(371, 132, EVENT_DEPTH)]) # Painting/locket2
Sprites.append(["EntityHousePaintingHallObject2", "EntityObject.sx", Convert(192, 85, EVENT_DEPTH)]) # Other painting
Sprites.append(["EntityHousePantryObject1", "EntityObject.sx", Convert(226, 152, EVENT_DEPTH)]) # Pins
Sprites.append(["EntityHousePantryObject2", "EntityObject.sx", Convert(112, 226, EVENT_DEPTH)])
Sprites.append(["EntityHousePantryObject3", "EntityObject.sx", Convert(260, 97, EVENT_DEPTH)])
Sprites.append(["EntityHousePantryObject4", "EntityObject.sx", Convert(497, 156, EVENT_DEPTH)])
Sprites.append(["EntityHousePatioObject1", "EntityObject.sx", Convert(346, 196, EVENT_DEPTH)]) # Gas can
Sprites.append(["EntityHousePatioObject2", "EntityObject.sx", Convert(45, 302, EVENT_DEPTH)])
Sprites.append(["EntityHousePatioObject3", "EntityObject.sx", Convert(484, 166, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall1Object1", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall1Object2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall2Object1", "EntityObject.sx", Convert(262, 209, EVENT_DEPTH)]) # Opener
Sprites.append(["EntityHouseSideHall2Object2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseStudyObject1", "EntityObject.sx", Convert(359, 137, EVENT_DEPTH)]) # Diary
Sprites.append(["EntityHouseStudyObject2", "EntityObject.sx", Convert(232, 202, EVENT_DEPTH)]) # Bible
Sprites.append(["EntityValleyObject1", "EntityObject.sx", Convert(255, 277, EVENT_DEPTH)]) # Explosive point
Sprites.append(["EntityValleyObject2", "EntityObject.sx", Convert(0, 0, EVENT_DEPTH)])
########################################################################################
Sprites.append(["EntityAreaCarHidingSpot1", "EntityHiding.sx", Convert(491, 305, EVENT_DEPTH)])
Sprites.append(["EntityAreaCarHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityAreaSnowplowHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityAreaSnowplowHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCabinHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCabinHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCabinFrontHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCabinFrontHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCaveEntranceHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCaveEntranceHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCaveExitHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityCaveExitHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityDriveway1HidingSpot1", "EntityHiding.sx", Convert(63, 264, EVENT_DEPTH)])
Sprites.append(["EntityDriveway1HidingSpot2", "EntityHiding.sx", Convert(452, 192, EVENT_DEPTH)])
Sprites.append(["EntityDriveway2HidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityDriveway2HidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseBackHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseBackHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseBathroomHidingSpot1", "EntityHiding.sx", Convert(345, 181, EVENT_DEPTH)])
Sprites.append(["EntityHouseBathroomHidingSpot2", "EntityHiding.sx", Convert(161, 177, EVENT_DEPTH)])
Sprites.append(["EntityHouseBathroomHidingSpot3", "EntityHiding.sx", Convert(495, 197, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallHidingSpot1", "EntityHiding.sx", Convert(275, 76, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedHallHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedroomHidingSpot1", "EntityHiding.sx", Convert(413, 309, EVENT_DEPTH)])
Sprites.append(["EntityHouseBedroomHidingSpot2", "EntityHiding.sx", Convert(141, 231, EVENT_DEPTH)])
Sprites.append(["EntityHouseCourtyardHidingSpot1", "EntityHiding.sx", Convert(68, 174, EVENT_DEPTH)])
Sprites.append(["EntityHouseCourtyardHidingSpot2", "EntityHiding.sx", Convert(63, 301, EVENT_DEPTH)])
Sprites.append(["EntityHouseDenHidingSpot1", "EntityHiding.sx", Convert(266, 297, EVENT_DEPTH)])
Sprites.append(["EntityHouseDenHidingSpot2", "EntityHiding.sx", Convert(384, 139, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHidingSpot1", "EntityHiding.sx", Convert(157, 108, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHidingSpot2", "EntityHiding.sx", Convert(389, 193, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallLowerHidingSpot1", "EntityHiding.sx", Convert(122, 235, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallLowerHidingSpot2", "EntityHiding.sx", Convert(486, 235, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallLowerHidingSpot3", "EntityHiding.sx", Convert(415, 302, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallUpperHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseFrontHallUpperHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseGarageHidingSpot1", "EntityHiding.sx", Convert(367, 293, EVENT_DEPTH)])
Sprites.append(["EntityHouseGarageHidingSpot2", "EntityHiding.sx", Convert(248, 188, EVENT_DEPTH)])
Sprites.append(["EntityHouseGuestroomHidingSpot1", "EntityHiding.sx", Convert(277, 307, EVENT_DEPTH)])
Sprites.append(["EntityHouseGuestroomHidingSpot2", "EntityHiding.sx", Convert(28, 209, EVENT_DEPTH)])
Sprites.append(["EntityHouseHiddenRoomHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseHiddenRoomHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseKitchenHidingSpot1", "EntityHiding.sx", Convert(163, 223, EVENT_DEPTH)])
Sprites.append(["EntityHouseKitchenHidingSpot2", "EntityHiding.sx", Convert(356, 287, EVENT_DEPTH)])
Sprites.append(["EntityHouseLaundryHidingSpot1", "EntityHiding.sx", Convert(399, 237, EVENT_DEPTH)])
Sprites.append(["EntityHouseLaundryHidingSpot2", "EntityHiding.sx", Convert(198, 229, EVENT_DEPTH)])
Sprites.append(["EntityHouseLinenHidingSpot1", "EntityHiding.sx", Convert(192, 231, EVENT_DEPTH)])
Sprites.append(["EntityHouseLinenHidingSpot2", "EntityHiding.sx", Convert(80, 285, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomHidingSpot1", "EntityHiding.sx", Convert(205, 259, EVENT_DEPTH)])
Sprites.append(["EntityHouseLivingRoomHidingSpot2", "EntityHiding.sx", Convert(454, 134, EVENT_DEPTH)])
Sprites.append(["EntityHouseMusicRoomHidingSpot1", "EntityHiding.sx", Convert(392, 275, EVENT_DEPTH)])
Sprites.append(["EntityHouseMusicRoomHidingSpot2", "EntityHiding.sx", Convert(391, 207, EVENT_DEPTH)])
Sprites.append(["EntityHousePaintingHallHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHousePaintingHallHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHousePantryHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHousePantryHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHousePatioHidingSpot1", "EntityHiding.sx", Convert(278, 262, EVENT_DEPTH)])
Sprites.append(["EntityHousePatioHidingSpot2", "EntityHiding.sx", Convert(167, 113, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall1HidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall1HidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall2HidingSpot1", "EntityHiding.sx", Convert(329, 282, EVENT_DEPTH)])
Sprites.append(["EntityHouseSideHall2HidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityHouseStudyHidingSpot1", "EntityHiding.sx", Convert(211, 263, EVENT_DEPTH)])
Sprites.append(["EntityHouseStudyHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityValleyHidingSpot1", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
Sprites.append(["EntityValleyHidingSpot2", "EntityHiding.sx", Convert(0, 0, EVENT_DEPTH)])
########################################################################################

########################################################################################

########################################################################################
Fonts = []
Fonts.append(["Font", "Tuffy.fx", (FONT_X, FONT_Y, FONT_Z)])
########################################################################################

########################################################################################
Radios = []
Radios.append(["Music", "Music.rx", (RADIO_X, RADIO_Y, RADIO_Z)])
Radios.append(["Sounds", "Sounds.rx", (RADIO_X, RADIO_Y, RADIO_Z)])
########################################################################################
