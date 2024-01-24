//-----------------------------------------------------------------------------
// The first thing will do is to setup a particle system for our camp fire.
// The fire particle system below consists of three scripted parts.
// 
// FireParticle            - Defines how individual particles behave.
// FireParticleEmitter     - Defines how the particles enter the world.
// FireParticleEmitterNode - The particle system's node for world placement.
//-----------------------------------------------------------------------------
datablock ParticleData( FireParticle )
{
	textureName        = "~/data/shapes/campfire_particles/fire";
	dragCoefficient    = 0.0;
	gravityCoefficient = -0.3; // Gravity pulls down, but a negative value makes the particles rise instead of sink
	inheritedVelFactor = 0.00;
	useInvAlpha        = false;
	spinRandomMin      = -30.0;
	spinRandomMax      = 30.0;

	lifetimeMS         = 500;
	lifetimeVarianceMS = 250;

	times[0] = 0.0;
	times[1] = 0.5;
	times[2] = 1.0;

	colors[0] = "0.8 0.6 0.0 0.1";
	colors[1] = "0.8 0.6 0.0 0.1";
	colors[2] = "0.0 0.0 0.0 0.0";

	sizes[0] = 1.0;
	sizes[1] = 1.0;
	sizes[2] = 5.0;
};

datablock ParticleEmitterData( FireParticleEmitter )
{
	particles = "FireParticle";

	ejectionPeriodMS = 15;
	periodVarianceMS = 5;

	ejectionVelocity = 0.25;
	velocityVariance = 0.10;

	thetaMin = 0.0;
	thetaMax = 90.0;
};

datablock ParticleEmitterNodeData( FireParticleEmitterNode )
{
	timeMultiple = 1;
};

//-----------------------------------------------------------------------------
// Where there's fire... there's smoke, so the second thing we need to do is 
// create a second particle system to represent the smoke.
// 
// SmokeParticle            - Defines how individual particles behave.
// SmokeParticleEmitter     - Defines how the particles enter the world.
// SmokeParticleEmitterNode - The particle system's node for world placement.
//-----------------------------------------------------------------------------
datablock ParticleData( SmokeParticle )
{
	textureName        = "~/data/shapes/campfire_particles/smoke";
	dragCoefficient    = 0.0;
	gravityCoefficient = -0.2; // Gravity pulls down, but a negative value makes the particles rise instead of sink
	inheritedVelFactor = 0.00;
	useInvAlpha        = false;
	spinRandomMin      = -30.0;
	spinRandomMax      = 30.0;

	lifetimeMS         = 3000;
	lifetimeVarianceMS = 250;

	times[0] = 0.0;
	times[1] = 0.5;
	times[2] = 1.0;

	colors[0] = "0.6 0.6 0.6 0.1";
	colors[1] = "0.6 0.6 0.6 0.1";
	colors[2] = "0.6 0.6 0.6 0.0";

	sizes[0] = 0.5;
	sizes[1] = 0.75;
	sizes[2] = 1.5;
};

datablock ParticleEmitterData( SmokeParticleEmitter )
{
	particles = SmokeParticle;

	ejectionPeriodMS = 20;
	periodVarianceMS = 5;

	ejectionVelocity = 0.25;
	velocityVariance = 0.10;

	thetaMin = 0.0;
	thetaMax = 90.0;
};

datablock ParticleEmitterNodeData( SmokeParticleEmitterNode )
{
	timeMultiple = 1;
};
