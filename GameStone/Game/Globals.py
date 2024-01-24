## Silence Unmasked
## Waterstone Productions

# Local imports
import Constants

########################################################################################
Events = {}
########################################################################################
Events["INPUT"] = Constants.EVENT_NOTHING
Events["OBJECT"] = False
########################################################################################

########################################################################################
Counters = {}
########################################################################################
Counters["CHASE_COUNTER"] = 0
########################################################################################

########################################################################################
Flags = {}
########################################################################################
Flags["HARD_DIFFICULTY"] = False
Flags["DISPLAYED_SUBSCREEN"] = False
Flags["BEING_CHASED"] = False
Flags["BEING_CHASED_INSTANTLY"] = False
Flags["SMASHED_LOCKETS"] = False
Flags["USED_EXPLOSIVE"] = False
Flags["USED_GASCAN"] = False
Flags["FALL_WARNING1"] = False
Flags["FALL_WARNING2"] = False
Flags["AXE_WARNING1"] = False
Flags["AXE_WARNING2"] = False
Flags["HOLDING_ITEM"] = False
Flags["CURRENT_ITEM"] = ""
########################################################################################
Flags["PICKED_UP_COURTYARD_KEY"] = False
Flags["PICKED_UP_BEDROOMHALL_KEY"] = False
Flags["PICKED_UP_BATHROOM_KEY"] = False
Flags["PICKED_UP_GARAGE_KEY"] = False
Flags["PICKED_UP_STUDY_KEY"] = False
Flags["PICKED_UP_MUSICBOX_KEYS"] = False
Flags["PICKED_UP_CROWBAR"] = False
Flags["PICKED_UP_BUCKET"] = False
Flags["PICKED_UP_OPENER"] = False
Flags["PICKED_UP_HANGER"] = False
Flags["PICKED_UP_THINNER"] = False
Flags["PICKED_UP_DOORKNOB"] = False
Flags["PICKED_UP_GASCAN"] = False
Flags["PICKED_UP_PINS"] = False
Flags["PICKED_UP_LOCKET1"] = False
Flags["PICKED_UP_LOCKET2"] = False
Flags["PICKED_UP_DYNAMITE"] = False
Flags["PICKED_UP_MATCHES"] = False
Flags["PICKED_UP_BIBLE"] = False
Flags["PICKED_UP_AXE"] = False
########################################################################################
Flags["UNLOCKED_COURTYARD"] = False
Flags["UNLOCKED_LIVINGROOM"] = False
Flags["UNLOCKED_HIDDENROOM"] = False
Flags["UNLOCKED_BEDROOMHALL"] = False
Flags["UNLOCKED_BATHROOM"] = False
Flags["UNLOCKED_MUSICROOM"] = False
Flags["UNLOCKED_SIDEHALL"] = False
Flags["UNLOCKED_KITCHEN"] = False
Flags["UNLOCKED_GARAGE"] = False
Flags["UNLOCKED_BACKAREA"] = False
Flags["UNLOCKED_STUDY"] = False
########################################################################################
Flags["SEEN_STEVENS_INTRO"] = False
Flags["SEEN_STEVENS_BIBLE"] = False
Flags["SEEN_STEVENS_FINAL"] = False
Flags["SEEN_SHADOWMAN_INTRO"] = False
Flags["SEEN_SHADOWMAN_FINAL"] = False
Flags["SEEN_BUNNY"] = False
Flags["SEEN_DIARY"] = False
Flags["SEEN_SCRAPBOOK"] = False
Flags["SEEN_LOCKET1"] = False
Flags["SEEN_LOCKET2"] = False
########################################################################################
Flags["HAVE_BUCKET_NONFILLED"] = False
Flags["HAVE_BUCKET_FILLED"] = False
Flags["HAVE_CROWBAR"] = False
Flags["HAVE_HANGER"] = False
Flags["HAVE_THINNER"] = False
Flags["HAVE_OPENER"] = False
Flags["HAVE_DOORKNOB"] = False
Flags["HAVE_GASCAN"] = False
Flags["HAVE_PINS"] = False
Flags["HAVE_LOCKET1"] = False
Flags["HAVE_LOCKET2"] = False
Flags["HAVE_DYNAMITE"] = False
Flags["HAVE_MATCHES"] = False
Flags["HAVE_BIBLE"] = False
Flags["HAVE_AXE"] = False
Flags["HAVE_MUSICBOX_KEYS"] = False
Flags["HAVE_COURTYARD_KEY"] = False
Flags["HAVE_BEDROOMHALL_KEY"] = False
Flags["HAVE_BATHROOM_KEY"] = False
Flags["HAVE_GARAGE_KEY"] = False
Flags["HAVE_STUDY_KEY"] = False
########################################################################################
