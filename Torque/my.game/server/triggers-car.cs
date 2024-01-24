//===========================================================================

datablock TriggerData( CarMountArea )
{
	tickPeriodMS = 100;
};

function CarMountArea::onEnterTrigger( %this, %trigger, %obj )
{
	commandToServer('MountVehicle');
	Parent::onEnterTrigger( %this, %trigger, %obj );
}

function CarMountArea::onLeaveTrigger( %this, %trigger, %obj )
{
	Parent::onLeaveTrigger( %this, %trigger, %obj );
}

function CarMountArea::onTickTrigger( %this, %trigger )
{
	commandToServer('MountVehicle');
	Parent::onTickTrigger( %this, %trigger );
}

//===========================================================================

datablock TriggerData( CarDismountArea )
{
	tickPeriodMS = 100;
};

function CarDismountArea::onEnterTrigger( %this, %trigger, %obj )
{
	commandToServer('DisMountVehicle');
	Parent::onEnterTrigger( %this, %trigger, %obj );
}

function CarDismountArea::onLeaveTrigger( %this, %trigger, %obj )
{
	Parent::onLeaveTrigger( %this, %trigger, %obj );
}

function CarDismountArea::onTickTrigger( %this, %trigger )
{
	commandToServer('DisMountVehicle');
	Parent::onTickTrigger( %this, %trigger );
}

//===========================================================================

