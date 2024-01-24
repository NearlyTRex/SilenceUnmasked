//===========================================================================

datablock TriggerData( PuzzleArea )
{
	tickPeriodMS = 100;
};

function PuzzleArea::onEnterTrigger( %this, %trigger, %obj )
{
	$clockStrikeHandle = alxPlay(ClockStrikeStart);
	if ($PaintingPuzzle.getTransform() $= "240.892 310.402 136.336 0 0 1 2.31911")
	{
		$PaintingPuzzle.setTransform("244.892 310.402 136.336 0 0 1 134.266");
	}
	else
	{
		$PaintingPuzzle.setTransform("240.892 310.402 136.336 0 0 1 134.266");
	}
	Parent::onEnterTrigger( %this, %trigger, %obj );
}

function PuzzleArea::onLeaveTrigger( %this, %trigger, %obj )
{
	alxStop($clockStrikeHandle);
	Parent::onLeaveTrigger( %this, %trigger, %obj );
}

function PuzzleArea::onTickTrigger( %this, %trigger )
{
	
	Parent::onTickTrigger( %this, %trigger );
}

//===========================================================================

