## Silence Unmasked
## Waterstone Productions

# Local imports
import Globals

########################################################################################
# Introduction
Lines_Intro1 = [
"I never much liked snow... A blinding torrent of it surrounded my car from all sides, seemingly isolating me from the rest of the world.",
"And yet there I was, trying to get to a place that I had apparently been to but never known...",
"Before my foster father died, he gave me the shock of my life by saying that I was adopted.  I couldn't believe it... that this family that had raised me was not my own!",
"I had another mother and father, somewhere out there...  I had to find out who these people were, where I came from.",
"I did a lot of digging and found this small town in the mountains.  It wasn't much to go on, but it was all I could find.",
"So, on the eve of my birthday, I set out to go find this place, and maybe, a bit of myself.",
"But I ended up getting trapped in the middle of a snowstorm!",
"I could barely see anything, and it was quite difficult to keep the car on the road..."
]
Lines_Intro2 = [
"Suddenly, I saw a figure on the road right in front of me!",
"I hit the brakes and swerved out of the way, but my car slid onto a patch of ice, and I almost completely lost control of it.",
"The car went into a spin, and I knew I was probably going to hit whoever was on this desolate road at night...",
"The last thing I remembered was my head hitting the steering wheel, and everything blacking out.",
]
Lines_Intro3 = [
"When I awoke, I realized I must have been passed out for hours.  It was now probably midday, though I couldn't be sure.",
"One thing I knew was that the snowstorm was still going strong, and I was lucky to be alive after that crash.",
"Immediately thinking of the figure on the road, I got out of my car and looked around...",
"But I didn't see anything, or anyone.",
"I wasn't even sure I was on the same road anymore.  Instead all I could see in the distance was a house with some lights on.",
"Knowing I couldn't go anywhere in my wrecked car, and getting colder by the minute, I knew I had no choice but to get moving...",
"Some birthday this was turning out to be...",
]
########################################################################################
Scene_Intro = []
for line in Lines_Intro1:
  Scene_Intro.append(["CutsceneDriving", "Font", "Music", "Introduction", line])
for line in Lines_Intro2:
  Scene_Intro.append(["CutsceneHallucination", "Font", "Music", "Introduction", line])
for line in Lines_Intro3:
  Scene_Intro.append(["CutsceneAccident", "Font", "Music", "Introduction", line])
########################################################################################

########################################################################################
# Stevens Introduction
Lines_StevensIntro1 = [
"Stepping up to the huge doors of the house, I knocked a few times to make sure that someone would hear it over the sound of the storm.",
"For a while, I thought no one was going to answer the door, when suddenly I heard the door unlock and open.",
]
Lines_StevensIntro2 = [
"A scraggly man with a beard poked his head out of the door and caught sight of me standing there."
"'What are you doing out there in this storm, come on in before you freeze!'",
"'Thanks!  I wasn't planning on being out in this, but my car got into an accident a little while away and I stumbled here to get out of the cold...'",
"I shook the snow off of my coat and asked him if there was a fire nearby so I could get warm.",
"With a sullen look on his face, he told me, 'You might have been better off out in the snow miss... something terrible is going on here...'",
"'The name is Stevens, I've been the caretaker here since the master passed away, but I'm afraid I can't offer much comfort...'",
"'There's a fire in the other room if you want, but I really think you need to get going soon for your own go-'",
"There was a loud crash coming from some other part of the house, startling us both.  Stevens eyes lit up with fear.",
"'You've got to leave here as soon as you can!  Do what you need to do and go!  And whatever you do, stay away from the shadows and... him!'",
"With that, he went off in the direction of where the sound came from, leaving me in this huge hallway by myself.",
]
Lines_StevensIntro3 = [
"Him?  Shadows?  What on earth did he mean by that?",
"After he left, I looked around the front hallway... it was quite an impressive looking mansion, though I could see it clearly was in a state of disarray.",
"I don't think the caretaker was really taking care of anything here.",
"I was about to try another room, when I noticed the painting in the center of the stairs... it looked very familiar, though I couldn't exactly place it... perhaps I should go take a closer look....",
]
########################################################################################
Scene_StevensIntro = []
for line in Lines_StevensIntro1:
  Scene_StevensIntro.append(["CutsceneHouseFront", "Font", "Music", "Stevens", line])
for line in Lines_StevensIntro2:
  Scene_StevensIntro.append(["CutsceneStevens", "Font", "Music", "Stevens", line])
for line in Lines_StevensIntro3:
  Scene_StevensIntro.append(["CutsceneHouseHall", "Font", "Music", "Stevens", line])
########################################################################################

########################################################################################
# Stevens Bible
Lines_StevensBible1 = [
"As I was walking into the kitchen, I bumped into Stevens again, nearly knocking us both over in the process.",
"'You're still here?!  I thought you would have gotten clear of this nightmare as soon as you could!'",
"'Well, I would, but I have no way to get out of here!  I told you my car is totalled!'",
"'Also, there's this creepy guy following me around with knives!  Do you know who he is?'",
"He acted as if he didn't even hear me... he must be in pretty bad shape himself...",
"'You shouldn't be here... none of us should...  Not with that demon spawn running around!  We have to get somewhere safe!'",
"'I told the master that we should have gotten rid of him a lot sooner... that boy is just plain evil I tell you.'",
"'What boy?' I asked, exasperated, 'What are you talking about?  You mean that psycho running around?'",
"Again, he just kept on rambling, almost oblivious to the fact that I was standing there.",
"'I have to find my bible!  It's the only protection I have left!  It has to be here somewhere... that will protect me from the devil himself.'",
"I felt like shaking him to get some straight answers!  'Listen, is there another vehicle around here that's working, maybe we can get out of here and call the police or something.'",
"'Ain't no stopping it, he's on to us now, he's going to follow us forever... My Bible!  I have to find it!  Save yourself however you can!'",
"'Wait!  Don't go again!' I yelled after him, but he was gone before I could stop him...",
"Once again, I found myself alone in this desolate place... and had a strange feeling that I was being watched..."
]
Lines_StevensBible2 = [
"!!"
]
########################################################################################
Scene_StevensBible = []
for line in Lines_StevensBible1:
  Scene_StevensBible.append(["CutsceneStevens", "Font", "Music", "Stevens", line])
for line in Lines_StevensBible2:
  Scene_StevensBible.append(["CutsceneShadowMan", "Font", "Music", "Surprise", line])
########################################################################################

########################################################################################
# Stevens Final
Lines_StevensFinal1_1 = [
"My Bible!  You found it!",
"'Miss!  Why are you still here?  Don't you know there's a madman on the loose?'",
"'I think I figured that one out already!  Who the heck is this guy that keeps trying to kill me?'",
"'I'm afraid it's all my fault miss... I was the one the master blamed when he originally got out... and killed dear lady Rose...'",
"'Huh?  Are you talking about the people who originally lived here?'",
"'Yes, they were the couple who lived here...  they were quite a happy family until the children came along'",
"'The children?' I asked.",
"'There were two children born of the master's wife... both were evil things... I could tell you see, I could tell before anyone else did, but they didn't listen to me... no they didn't'.",
"'I knew they were rotten... The master soon found out himself when he found all the chickens beheaded, the dogs gutted... those poor dogs...'",
"'Then, there was the lady's niece... oh god...'",
"'Yeah I read about that in a diary I found...' I said.  He again didn't seem to hear me.",
"'After that, the master locked the children away, where they wouldn't harm anyone.  The lady was very mournful and upset, she loved those two... then she went and let them out against his wishes...'",
"'And..... they killed her....'  He started sobbing.  'The master and I knew what we had to do... though we didn't want to do it.'",
"'We took them... and went out into the storm.  And left them there... to die... oh god it was horrible, but I knew it was for the best...'",
"'For the best!?!' I shouted, 'You tried to murder them!  Did murder at least one of them, and now the other is back for revenge!  I'm not even sure who the monster is here anymore!'",
"'Please...' he begged, 'I know my soul is damned as much as they were... but it was all I could do...'",
"'They were children, they didn't know any better!  Why didn't you even try to help them get better?'",
]
Lines_StevensFinal1_2 = [
"A loud crash interrupted us, and the door flung open.  Silhouetted against the doorway, I could see him.  The Shadow Man was back!",
"'Run!' Stevens cried to me, 'There's a snow plow a little ways away, you can use that to escape!'",
"Before I could say anything, he took the Bible that I had given him and flung it at the monster.  It screeched and fell backwards.",
"I didn't stay around for very long though.  I bolted through the other door of the cabin and back out into the snowstorm.",
"I wasn't sure about Stevens, but I was going to get out of here!"
]
Lines_StevensFinal2_1 = [
"'Miss!  What are you still doing here?  Don't you know you need to get out of here before he comes back?'"
]
Lines_StevensFinal2_2 = [
"He walked towards me, about to say something more, when suddenly, the door flew open and a figure leaped out from the shadows.  It was him!",
"The Shadow Man toppled over Stevens, bringing him to the ground quickly.  They fought for a few moments, Stevens trying to fend of the knives with his bare hands.",
"'Run!  Get out of here!  There's a snowplow behind the estate you can use to-'",
"All further words were cut off as the Shadow Man plunged the knives into Stevens body.  He gasped for breath, but soon died on the floor...",
"It all happened so fast, I hadn't even moved.  Now, the monster picked himself up off the floor, turned around, and set his eyes on me!  I couldn't really see much of a facial expression, but I knew somehow that he was smiling evily at me...",
"I bolted for the other cabin door, opening it as quickly as I could and rushing outside into the storm.",
"I heard him behind me following, I didn't have much time left!"
]
########################################################################################
Scene_StevensFinal1 = []
for line in Lines_StevensFinal1_1:
  Scene_StevensFinal1.append(["CutsceneStevens", "Font", "Music", "Stevens", line])
for line in Lines_StevensFinal1_2:
  Scene_StevensFinal1.append(["CutsceneShadowMan", "Font", "Music", "Shock", line])
########################################################################################
Scene_StevensFinal2 = []
for line in Lines_StevensFinal2_1:
  Scene_StevensFinal2.append(["CutsceneStevens", "Font", "Music", "Stevens", line])
for line in Lines_StevensFinal2_2:
  Scene_StevensFinal2.append(["CutsceneShadowMan", "Font", "Music", "Shock", line])
########################################################################################

########################################################################################
# ShadowMan Introduction
Lines_ShadowManIntro1 = [
"I looked closer at the painting.  It had a strange resemblance to it of someone I knew, but I couldn't put my finger on it.",
"It was a painting of a woman, apparently someone prominent who lived here before.  The placard says 'Lady Rose'.",
"Hmmm, the pendant she is wearing is very similar to the one I have....how strange.......",
"I heard a noise from behind me, someone opened a door and I could hear footsteps.  Figuring it was Stevens again, I turned around, about to ask him who this was supposed to be......",
]
Lines_ShadowManIntro2 = [
"!!!",
]
Lines_ShadowManIntro3 = [
"The strange figure advanced closer and closer to me, and I could hear him grating two knives together... he never even blinked, just kept those beady eyes on me.",
"I've got to get away from him and find a place to hide!"
]
########################################################################################
Scene_ShadowManIntro = []
for line in Lines_ShadowManIntro1:
  Scene_ShadowManIntro.append(["CutscenePainting", "Font", "Music", "Stevens", line])
for line in Lines_ShadowManIntro2:
  Scene_ShadowManIntro.append(["CutsceneShadowMan", "Font", "Music", "Surprise", line])
for line in Lines_ShadowManIntro3:
  Scene_ShadowManIntro.append(["CutsceneShadowMan", "Font", "Sounds", "Knives", line])
########################################################################################

########################################################################################
# ShadowMan Death
Scene_ShadowManDeath = []
Scene_ShadowManDeath.append(["CutsceneShadowMan", "Font", "Music", "Surprise", "!!!!"])
########################################################################################

########################################################################################
# Shadowman Final
Lines_ShadowManFinal1 = [
"I ran into the cave, hearing the blinding storm rage on behind me.  I could tell that the storm wasn't going to let up any time soon, and in fact it looked like it was getting worse.",
"I ran around a little bit, taking out a flashlight that I had stored in my pocket earlier, and hid in a crevice to catch my breath...",
"But I heard him cackle like he was right there in front of me!  I ran around to try to find the exit..."
]
Lines_ShadowManFinal2 = [
"...and ran straight into him!",
"'Hehehehe hahaha hehehe!  Oh you are a joy to chase every which way, aren't you?  Heheheh hahahaha!'",
"'What do you want from me?' I asked him frightened.",
"'You still don't get it do you?  Oh silly me, I guess I haven't been a good host have I?  I should have properly introduced myself, but I don't think I need to! Hahahaha!'",
"'Do you remember me now?  Do you remember what they did to us?'",
"'No....' I said meekly... 'No!'",
"'Hehehe, it remembers, it does!'  It chuckled at me horribly.",
"'They left us out in the storm, they did!  You got away, some kind nun found you, but me?  Nobody!!  No pretty princess life came to save me, no sirree!  Hahahahahaha!'",
"'That can't be true!' I yelled.",
"'Oh but it is, don't deny it.  Liar... liar... pants on fire! Hehehehe!'",
"'We're one and the same, you and me!  We're of the same seed you know!  And what I do...'",
"'.... you do as well!  Or... don't you remember what you did to your foster father...?'",
"'What are you talking about?  My father died of old age!'",
"'No.  You killed him.  Just like I killed our real father and mother... after they locked us up like animals, tried to kill us!",
"'We're not so different, I've just embraced what I am!  How about it, sis?  Hahahaha!'",
"'Shut up!!  You're a liar!' I screamed.",
"'Heheehee!  The mouse has a mouth on it, yes it does!  Well, let's see if this cat can teach the mouse some manners!  Run, run little mouse!  Run and find your mousey hole!  Hahahahahahaha!'"
]
Lines_ShadowManFinal3 = [
"I ran and ran, hearing his horrifying laughter behind me... and the words he had said....",
"He's lying...he just has to be!",
"I saw an opening to the cave, there was another exit!  I flew to the opening and found myself back in the storm again...",
"I could still hear him following me though... I have to get to that snowplow!  It's my only chance!"
]
########################################################################################
Scene_ShadowManFinal = []
for line in Lines_ShadowManFinal1:
  Scene_ShadowManFinal.append(["CutsceneCave1", "Font", "Music", "Stevens", line])
for line in Lines_ShadowManFinal2:
  Scene_ShadowManFinal.append(["CutsceneShadowMan", "Font", "Music", "Shock", line])
for line in Lines_ShadowManFinal3:
  Scene_ShadowManFinal.append(["CutsceneCave2", "Font", "Music", "Shock", line])
########################################################################################

########################################################################################
# Diary
Lines_Diary = [
"It's an old diary... lots of the pages are missing, but some are still intact.",
"October 12, 1970\nI had to discipline the children again today... Rose wouldn't hear of it... As much as I try to love these children, I can't help but wonder sometimes... In any case, I can't have them going around hurting the animals, least of all our prize winning dogs.  Somebody has to teach them discipline, or they won't know any better later on.  My father strongly disciplined me and I turned out fine.  I would want the same for them",
"October 17, 1970\nRose's favorite vase was smashed... It wouldn't have been such a burden normally for her, but after all this, I decided I would hide it from her.",
"October 25, 1970\nThe caretaker again forgot to feed the children... After our maid left, he's been assigned some extra duties, but he can't even seem to handle something like this... what a simpleton.",
"October 27, 1970\nThe children incessantly bothered me today about going out.  I had to again try to instill some manners in them.  Honestly, I think I'm the only person who even tries to!",
"There's some more pages missing here, it continues later on.",
"November 19, 1972\nMore problems with these children today.  Honestly, I don't even know why I bother.  They are such pitiful things... and I've always been unnerved by the stares they give me.... like there's something behind them waiting to get out...",
"December 21, 1972\nChristmas is coming soon.  I have to do some shopping, but I have to be honest, I'm finding myself more and more afraid of these children by the day.  They've almost completely stopped acting rambunctious when I'm around, but I know they still get into trouble.  The carcasses I find in the woods nearby are a little too coincidental to be from an animal... I better not take them with me into town.",
"December 25, 1972\nThe little brats!  They were playing around with my guns!  I gave David quite a number and made an example out of him for his sister.  These children have no hope left.... Maybe that crazy caretaker is right after all.  He babbles on sometimes about how they always give him the evil eye, that there's something 'mighty wrong' with them.  I figured he was just being simpleminded but I don't know now...  I burned their presents as part of their punishment.",
"January 5, 1973\nRose's niece is coming to stay with us for a month, I certainly hope these children can behave themselves for such a small amount of time.",
"January 18, 1973\nThese truly are monsters!  They again played around with my guns while I was away, and as they were with our niece Julia, the cretins shot her in the leg!  I completely lost it.  No matter what Rose says, these really are the devil's children.  No son or daughter of mine would be so afflicted!  Julia survived her encounter and returned home, while I constructed a room for these... things.  I'm ashamed that they are even part of my flesh and blood.  They'll stay here until I can figure out what to do with them.",
"....The rest of the diary is burned away or missing......."
]
########################################################################################
Scene_Diary = []
for line in Lines_Diary:
  Scene_Diary.append(["CutsceneDiary", "Font", "Music", "Stevens", line])
########################################################################################

########################################################################################
# Scrapbook
Lines_Scrapbook = [
"It's apparently a scrapbook of some sort...",
"There are numerous drawings of people being murdered or having their heads chopped off...",
"And photographs of apparent family members that have been gouged with what appears to be knifemarks.",
"One childrens book in particular has had all of the pictures vandalized and mutilated to look like monsters...",
"There's a few notes and diary entries here, but they've either been scribbled upon past recognition or burned.",
"One of them just repeats the same words over and over: 'Knify knife, whether is wife, slippery handle, ending it's life!'....",
"Whoever wrote and drew these things must have had some serious problems, there's some seriously disturbing stuff here...."
]
########################################################################################
Scene_Scrapbook = []
for line in Lines_Scrapbook:
  Scene_Scrapbook.append(["CutsceneScrapbook", "Font", "Music", "Stevens", line])
########################################################################################

########################################################################################
# Bunny
Lines_Bunny1 = [
"I picked up the stuffed bunny, it looked a little old and misused, and I could feel that there was something heavy inside.",
"Taking the letter opener in hand, I cut into the side of it, and found there was a locket inside!"
]
Lines_Bunny2 = [
"The locket was pretty old and rusty, but I managed to open it.",
"Inside, I saw there two old photographs, apparently of children.  One of them looked happy smiling for the picture while the other looked like he hated it...",
"Hey!  Wait a minute, this photo of the girl looks like me as a kid!  How on earth is that possible?  I guess what they say is true, everyone does have a twin out there somewhere..."
]
Lines_Bunny3 = [
"However, soon enough I saw my hands were getting covered in something slimy!",
"Looking down, I saw to my horror that the stuffed bunny had actually been holding a live animal inside!!  Oh my god!  What have I done!?!"
]
########################################################################################
Scene_Bunny = []
for line in Lines_Bunny1:
  Scene_Bunny.append(["CutsceneBunny", "Font", "Music", "Stevens", line])
for line in Lines_Bunny2:
  Scene_Bunny.append(["CutsceneLocket1", "Font", "Music", "Stevens", line])
for line in Lines_Bunny3:
  Scene_Bunny.append(["CutsceneBunny", "Font", "Music", "Stevens", line])
########################################################################################

########################################################################################
# Fall
Lines_Fall1 = [
"I walked over to go pick up the note on the floor, paying no attention to the weakened floorboards underneath my feet.  As soon as I picked up the note, the floor gave way beneath me and I plummeted into darkness....  The last thing I remember seeing is the note in my bloody hands...."
]
Lines_Fall2 = [
"It read: SURPRISE! HAHAHAHAHA!"
]
########################################################################################
Scene_Fall = []
for line in Lines_Fall1:
  Scene_Fall.append(["CutsceneFall", "Font", "Music", "Collapse", line])
for line in Lines_Fall2:
  Scene_Fall.append(["CutsceneDark", "Font", "Music", "Surprise", line])
########################################################################################

########################################################################################
# Dark
Lines_Dark1 = [
"With the gas tank emptying in the car, the sound of the sputtering vehicle got softer and softer... and then the motor went dead.",
"With it, so did the only light in the garage...",
"I stumbled around for a few minutes, and finally found the door.  It was locked!",
"....That's when I heard him cackle at me from within the darkness...."
]
Lines_Dark2 = [
"!!!!!!!!"
]
########################################################################################
Scene_Dark = []
for line in Lines_Dark1:
  Scene_Dark.append(["CutsceneDark", "Font", "Music", "Stevens", line])
for line in Lines_Dark2:
  Scene_Dark.append(["CutsceneShadowMan", "Font", "Music", "Surprise", line])
########################################################################################

########################################################################################
# Ending A - Forgiveness
Lines_EndingA1 = [
"The explosion of the dynamite was enormous!  It sent a wave of snow coming down the mountainside.  The Shadow Man was buried under tons of rock and slush, there was no sign of him at all..."
]
Lines_EndingA2 = [
"I got into the plow, which thankfully was still running, and had a half full tank of gas still.  I started the motor and put it into gear and started driving off."
]
Lines_EndingA3 = [
"I had one visit to make though... once I got home...",
"'Dad... I'm sorry for what happened...  I understand it now, and I'm finally getting help... I just wanted you to know what happened, so you can finally be at peace yourself...'",
"'I know you weren't my real dad... but I love you anyway, and I miss you'...",
"....I drove back to my old home, my real home... not some figment of a nightmare long past..."
]
########################################################################################
Scene_EndingA = []
for line in Lines_EndingA1:
  Scene_EndingA.append(["CutsceneExplosion", "Font", "Music", "Avalanche", line])
for line in Lines_EndingA2:
  Scene_EndingA.append(["CutsceneSnowplow", "Font", "Music", "Plow", line])
for line in Lines_EndingA3:
  Scene_EndingA.append(["CutsceneFathersGrave", "Font", "Music", "Stevens", line])
########################################################################################

########################################################################################
# Ending B - Mind
Lines_EndingB1 = [
"The explosion of the dynamite was enormous!  It sent a wave of snow coming down the mountainside.  The Shadow Man was buried under tons of rock and slush, there was no sign of him at all..."
]
Lines_EndingB2 = [
"I got into the plow, which thankfully was still running, and had a half full tank of gas still.  I started the motor and put it into gear and started driving off."
]
Lines_EndingB3 = [
"....I must have dozed off at the wheel at some point, since I found myself drifting on the road still...",
"My car was barely able to stay in a straight line..."
]
Lines_EndingB4 = [
"Suddenly a figure jumped out in the middle of the road!  I had to swerve to avoid hitting him, but it sent me into a tailspin..."
]
Lines_EndingB5 = [
"....I had blacked out from the accident... it was day now apparently, and I wasn't even sure where I was now.  But I saw a house up ahead..."
]
Lines_EndingB6 = [
"............Stevens.....snow....shadows.....",
"'This one in particular is an interesting case,' one man explained to another.",
"'This woman, she's been in here ever since she murdered her father.  She suffered a complete nervous breakdown from the incident, and now as you can see, she spends most of her day muttering about a Stevens or whatnot.'",
"'Clearly a case of psychosis.  Now, moving on we have this other patient.......'"
]
########################################################################################
Scene_EndingB = []
for line in Lines_EndingB1:
  Scene_EndingB.append(["CutsceneExplosion", "Font", "Music", "Avalanche", line])
for line in Lines_EndingB2:
  Scene_EndingB.append(["CutsceneSnowplow", "Font", "Music", "Plow", line])
for line in Lines_EndingB3:
  Scene_EndingB.append(["CutsceneDriving", "Font", "Music", "Introduction", line])
for line in Lines_EndingB4:
  Scene_EndingB.append(["CutsceneHallucination", "Font", "Music", "Introduction", line])
for line in Lines_EndingB5:
  Scene_EndingB.append(["CutsceneAccident", "Font", "Music", "Introduction", line])
for line in Lines_EndingB6:
  Scene_EndingB.append(["CutsceneMentalHospital", "Font", "Music", "Stevens", line])
########################################################################################

########################################################################################
# Ending C - Fate
Lines_EndingC1 = [
"The explosion of the dynamite was enormous!  It sent a wave of snow coming down the mountainside.  The Shadow Man was buried under tons of rock and slush, there was no sign of him at all..."
]
Lines_EndingC2 = [
"I got into the plow, which thankfully was still running, and had a half full tank of gas still.  I started the motor and put it into gear and started driving off."
]
Lines_EndingC3 = [
"What a night that turned out to be!",
"Now... with that pesky brother out of the way, I really needed to go out and have a little fun of my own this time....",
"I think I can find a good use for this axe after all.......",
"Hehe hehehehe hahahaha!!"
]
########################################################################################
Scene_EndingC = []
for line in Lines_EndingC1:
  Scene_EndingC.append(["CutsceneExplosion", "Font", "Music", "Avalanche", line])
for line in Lines_EndingC2:
  Scene_EndingC.append(["CutsceneSnowplow", "Font", "Music", "Plow", line])
for line in Lines_EndingC3:
  Scene_EndingC.append(["CutsceneEvil", "Font", "Music", "GameOver", line])
########################################################################################

########################################################################################
# Ending D - Death
Lines_EndingD1 = [
"I made it to the snowplow!  I can finally get out of this nightmare and away from that crazy psycho.",
"It was running already, I guess Stevens had already warmed it up for himself earlier.  Still had some gas too.",
"I was so glad that this whole night was finally over.  This was probably one of the worst birthdays of my life....."
]
Lines_EndingD2 = [
"As I started to get the plow in gear and slowly moving, I heard that sound again... those knives being grated against each other... oh god no!",
"I tried to make a run for it, but it was too late... he was already at the door!!",
]
Lines_EndingD3 = [
"!!!!!"
]
########################################################################################
Scene_EndingD = []
for line in Lines_EndingD1:
  Scene_EndingD.append(["CutsceneSnowplow", "Font", "Music", "Storm", line])
for line in Lines_EndingD2:
  Scene_EndingD.append(["CutsceneKnives", "Font", "Music", "Chase1", line])
for line in Lines_EndingD3:
  Scene_EndingD.append(["CutsceneShadowMan", "Font", "Music", "Surprise", line])
########################################################################################

########################################################################################
# Game Over
Scene_GameOver = []
Scene_GameOver.append(["CutsceneGameOver", "Font", "Music", "GameOver", "You are dead."])
########################################################################################

########################################################################################
# Credits
Scene_Credits = []
Scene_Credits.append(["CutsceneCredits1", "Font", "Music", "Credits", ""])
Scene_Credits.append(["CutsceneCredits2", "Font", "Music", "Credits", ""])
Scene_Credits.append(["CutsceneCredits3", "Font", "Music", "Credits", ""])
Scene_Credits.append(["CutsceneCredits4", "Font", "Music", "Credits", ""])
########################################################################################
