//===========================================================================

datablock TriggerData( FrontDoorArea )
{
	tickPeriodMS = 100;
};

function FrontDoorArea::onEnterTrigger( %this, %trigger, %obj )
{
	Parent::onEnterTrigger( %this, %trigger, %obj );
}

function FrontDoorArea::onLeaveTrigger( %this, %trigger, %obj )
{
	if (!alxIsPlaying($womanSobHandle))
	{
		$womanSobHandle = alxPlay(WomanSobStart);
	}
	stopSnowStorm();
	$DoorBarrierPainting.setTransform("242.689 300.044 129.216 0 0 1 223.701");
	Parent::onLeaveTrigger( %this, %trigger, %obj );
}

function FrontDoorArea::onTickTrigger( %this, %trigger )
{
	Parent::onTickTrigger( %this, %trigger );
}

//===========================================================================


