# -*-python-*-
# GemRB - Infinity Engine Emulator
# Copyright (C) 2003 The GemRB Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# $Header: /data/gemrb/cvs2svn/gemrb/gemrb/gemrb/GUIScripts/bg2/GUIOPT.py,v 1.4 2004/11/26 23:00:27 avenger_teambg Exp $


# GUIOPT.py - scripts to control options windows mostly from GUIOPT winpack

# GUIOPT:
# 0 - Main options window (peacock tail)
# 1 - Video options window
# 2 - msg win with 1 button
# 3 - msg win with 2 buttons
# 4 - msg win with 3 buttons
# 5 - Audio options window
# 6 - Gameplay options window
# 8 - Feedback options window
# 9 - Autopause options window


###################################################
import GemRB
from GUIDefines import *

import MessageWindow

###################################################
OptionsWindow = None
VideoOptionsWindow = None
AudioOptionsWindow = None
GameplayOptionsWindow = None
FeedbackOptionsWindow = None
AutopauseOptionsWindow = None
LoadMsgWindow = None
QuitMsgWindow = None
MoviesWindow = None
KeysWindow = None

###################################################
def OpenOptionsWindow ():
	"""Open main options window (peacock tail)"""
	global OptionsWindow

	GemRB.HideGUI()

	if OptionsWindow:
		if VideoOptionsWindow: OpenVideoOptionsWindow ()
		if AudioOptionsWindow: OpenAudioOptionsWindow ()
		if GameplayOptionsWindow: OpenGameplayOptionsWindow ()
		if FeedbackOptionsWindow: OpenFeedbackOptionsWindow ()
		if AutopauseOptionsWindow: OpenAutopauseOptionsWindow ()
		if LoadMsgWindow: OpenLoadMsgWindow ()
		if QuitMsgWindow: OpenQuitMsgWindow ()
		if KeysWindow: OpenKeysWindow ()
		if MoviesWindow: OpenMoviesWindow ()
		
		GemRB.UnloadWindow (OptionsWindow)
		OptionsWindow = None
		GemRB.SetVar ("OtherWindow", -1)
		
		GemRB.UnhideGUI ()
		return
		
	GemRB.LoadWindowPack ("GUIOPT")
	OptionsWindow = Window = GemRB.LoadWindow (0)
	GemRB.SetVar ("OtherWindow", OptionsWindow)
	
	# Return to Game
	Button = GemRB.GetControl (Window, 0)
	GemRB.SetText (Window, Button, 28638)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenOptionsWindow")	

	# Quit Game
	Button = GemRB.GetControl (Window, 1)
	GemRB.SetText (Window, Button, 2595)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenQuitMsgWindow")

	# Load Game
	Button = GemRB.GetControl (Window, 2)
	GemRB.SetText (Window, Button, 2592)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenLoadMsgWindow")

	# Save Game
	Button = GemRB.GetControl (Window, 3)
	GemRB.SetText (Window, Button, 20639)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenSaveWindow")

	# Video Options
	Button = GemRB.GetControl (Window, 4)
	GemRB.SetText (Window, Button, 28781)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenVideoOptionsWindow")

	# Audio Options
	Button = GemRB.GetControl (Window, 5)
	GemRB.SetText (Window, Button, 29720)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenAudioOptionsWindow")

	# Gameplay Options
	Button = GemRB.GetControl (Window, 6)
	GemRB.SetText (Window, Button, 29722)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenGameplayOptionsWindow")

	# Keyboard Mappings
	Button = GemRB.GetControl (Window, 7)
	GemRB.SetText (Window, Button, 29723)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenKeyboardMappingsWindow")

	# Movies
	Button = GemRB.GetControl (Window, 9)
	GemRB.SetText (Window, Button, 38156)   # or  2594
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenMoviesWindow")

	# game version, e.g. v1.1.0000
	#Label = GemRB.GetControl (Window, 0x10000007)
	#GemRB.SetText (Window, Label, GEMRB_VERSION)
	
	GemRB.UnhideGUI ()


	
###################################################

def OpenVideoOptionsWindow ():
	"""Open video options window"""
	global VideoOptionsWindow, VideoHelpText

	GemRB.HideGUI ()

	if VideoOptionsWindow:
		GemRB.UnloadWindow (VideoOptionsWindow)
		VideoOptionsWindow = None
		GemRB.SetVar ("OtherWindow", OptionsWindow)
		
		GemRB.UnhideGUI ()
		return

	
	VideoOptionsWindow = Window = GemRB.LoadWindow (1)
	GemRB.SetVar ("OtherWindow", VideoOptionsWindow)


	VideoHelpText = OptHelpText ('VideoOptions', Window, 9, 31052)

	OptDone ('VideoOptions', Window, 7)
	OptCancel ('VideoOptions', Window, 8)

	OptSlider ('Brightness', Window, 1, 10, 31234)
	OptSlider ('Contrast', Window, 2, 11, 31429)

	OptCheckbox ('SoftwareBlitting', Window, 6, 15, 30898)
	OptCheckbox ('SoftwareMirroring', Window, 4, 13, 30896)
	OptCheckbox ('SoftwareTransparency', Window, 5, 14, 30897)

	#GemRB.SetVisible (Window, 1)
	GemRB.UnhideGUI ()
	
	

def DisplayHelpBrightness ():
	GemRB.SetText (VideoOptionsWindow, VideoHelpText, 31431)

def DisplayHelpContrast ():
	GemRB.SetText (VideoOptionsWindow, VideoHelpText, 31459)

def DisplayHelpSoftwareBlitting ():
	GemRB.SetText (VideoOptionsWindow, VideoHelpText, 31221)

def DisplayHelpSoftwareMirroring ():
	GemRB.SetText (VideoOptionsWindow, VideoHelpText, 31216)

def DisplayHelpSoftwareTransparency ():
	GemRB.SetText (VideoOptionsWindow, VideoHelpText, 31220)



###################################################

def OpenAudioOptionsWindow ():
	"""Open audio options window"""
	global AudioOptionsWindow, AudioHelpText

	GemRB.HideGUI ()

	if AudioOptionsWindow:
		GemRB.UnloadWindow (AudioOptionsWindow)
		AudioOptionsWindow = None
		GemRB.SetVar ("OtherWindow", OptionsWindow)
		
		GemRB.UnhideGUI ()
		return

	
	AudioOptionsWindow = Window = GemRB.LoadWindow (5)
	GemRB.SetVar ("OtherWindow", AudioOptionsWindow)
	

	AudioHelpText = OptHelpText ('AudioOptions', Window, 9, 31210)

	OptDone ('AudioOptions', Window, 7)
	OptCancel ('AudioOptions', Window, 8)

	OptSlider ('AmbientVolume', Window, 1, 10, 31460)
	OptSlider ('SoundFXVolume', Window, 2, 11, 31466)
	OptSlider ('VoiceVolume', Window, 3, 12, 31467)
	OptSlider ('MusicVolume', Window, 4, 13, 31468)
	OptSlider ('MovieVolume', Window, 5, 14, 31469)
	
	OptCheckbox ('CreativeEAX', Window, 6, 15, 30900)
	OptCheckbox ('SoundProcessing', Window, 16, 17, 63242)
	OptCheckbox ('MusicProcessing', Window, 18, 19, 63243)


	#GemRB.SetVisible (AudioOptionsWindow, 1)
	GemRB.UnhideGUI ()
	

def DisplayHelpAmbientVolume ():
	GemRB.SetText (AudioOptionsWindow, AudioHelpText, 31227)
	
def DisplayHelpSoundFXVolume ():
	GemRB.SetText (AudioOptionsWindow, AudioHelpText, 31228)

def DisplayHelpVoiceVolume ():
	GemRB.SetText (AudioOptionsWindow, AudioHelpText, 31226)

def DisplayHelpMusicVolume ():
	GemRB.SetText (AudioOptionsWindow, AudioHelpText, 31225)

def DisplayHelpMovieVolume ():
	GemRB.SetText (AudioOptionsWindow, AudioHelpText, 31229)

def DisplayHelpCreativeEAX ():
	GemRB.SetText (AudioOptionsWindow, AudioHelpText, 31224)

def DisplayHelpSoundProcessing ():
	GemRB.SetText (AudioOptionsWindow, AudioHelpText, 63244)
	
def DisplayHelpMusicProcessing ():
	GemRB.SetText (AudioOptionsWindow, AudioHelpText, 63247)



###################################################

def OpenGameplayOptionsWindow ():
	"""Open gameplay options window"""
	global GameplayOptionsWindow, GameplayHelpText

	GemRB.HideGUI ()

	if GameplayOptionsWindow:
		if FeedbackOptionsWindow: OpenFeedbackOptionsWindow()
		if AutopauseOptionsWindow: OpenAutopauseOptionsWindow()

		GemRB.UnloadWindow (GameplayOptionsWindow)
		GameplayOptionsWindow = None
		GemRB.SetVar ("OtherWindow", OptionsWindow)
		
		GemRB.UnhideGUI ()
		return

	
	GameplayOptionsWindow = Window = GemRB.LoadWindow (6)
	GemRB.SetVar ("OtherWindow", GameplayOptionsWindow)
	

	GameplayHelpText = OptHelpText ('GameplayOptions', Window, 12, 31212)

	OptDone ('GameplayOptions', Window, 10)
	OptCancel ('GameplayOptions', Window, 11)

	OptSlider ('TooltipDelay', Window, 1, 13, 31481)
	OptSlider ('MouseScrollingSpeed', Window, 2, 14, 31482)
	OptSlider ('KeyboardScrollingSpeed', Window, 3, 15, 31480)
	OptSlider ('Difficulty', Window, 4, 16, 31479)

	OptCheckbox ('DitherAlways', Window, 5, 17, 31217)
	OptCheckbox ('Gore', Window, 6, 18, 31218)
	OptCheckbox ('AlwaysRun', Window, 22, 23, 62418)

	OptButton ('FeedbackOptions', Window, 8, 20, 31478)
	OptButton ('AutopauseOptions', Window, 9, 21, 31470)

	#GemRB.SetVisible (Window, 1)
	GemRB.UnhideGUI ()


def DisplayHelpTooltipDelay ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 31232)

def DisplayHelpMouseScrollingSpeed ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 31230)

def DisplayHelpKeyboardScrollingSpeed ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 31231)

def DisplayHelpDifficulty ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 31233)


def DisplayHelpDitherAlways ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 31222)

def DisplayHelpGore ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 31223)

def DisplayHelpAlwaysRun ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 62419)


def DisplayHelpFeedbackOptions ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 31213)

def DisplayHelpAutopauseOptions ():
	GemRB.SetText (GameplayOptionsWindow, GameplayHelpText, 31214)



###################################################
	
def OpenFeedbackOptionsWindow ():
	"""Open feedback options window"""
	global FeedbackOptionsWindow, FeedbackHelpText
	
	GemRB.HideGUI ()

	if FeedbackOptionsWindow:
		GemRB.UnloadWindow (FeedbackOptionsWindow)
		FeedbackOptionsWindow = None
		GemRB.SetVar ("OtherWindow", GameplayOptionsWindow)
		
		GemRB.UnhideGUI ()
		return

	
	FeedbackOptionsWindow = Window = GemRB.LoadWindow (8)
	GemRB.SetVar ("OtherWindow", FeedbackOptionsWindow)


	FeedbackHelpText = OptHelpText ('FeedbackOptions', Window, 9, 37410)

	OptDone ('FeedbackOptions', Window, 7)
	OptCancel ('FeedbackOptions', Window, 8)

	OptSlider ('MarkerFeedback', Window, 1, 10, 37463)
	OptSlider ('LocatorFeedback', Window, 2, 11, 37586)
	OptSlider ('SelectionFeedbackLevel', Window, 20, 21, 54879)
	OptSlider ('CommandFeedbackLevel', Window, 22, 23, 55012)

	OptCheckbox ('CharacterStates', Window, 6, 15, 37594)
	OptCheckbox ('MiscellaneousMessages', Window, 17, 19, 37596)
	OptCheckbox ('ToHitRolls', Window, 3, 12, 37588)
	OptCheckbox ('CombatInfo', Window, 4, 13, 37590)
	OptCheckbox ('SpellCasting', Window, 5, 14, 37592)


	#GemRB.SetVisible (FeedbackOptionsWindow, 1)
	GemRB.UnhideGUI ()
	

def DisplayHelpMarkerFeedback ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 37411)

def DisplayHelpLocatorFeedback ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 37447)

def DisplayHelpSelectionFeedbackLevel ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 54878)

def DisplayHelpCommandFeedbackLevel ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 54880)

def DisplayHelpCharacterStates ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 37460)

def DisplayHelpMiscellaneousMessages ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 37462)

def DisplayHelpToHitRolls ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 37453)

def DisplayHelpCombatInfo ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 37457)

def DisplayHelpSpellCasting ():
	GemRB.SetText (FeedbackOptionsWindow, FeedbackHelpText, 37458)


###################################################

def OpenAutopauseOptionsWindow ():
	"""Open autopause options window"""
	global AutopauseOptionsWindow, AutopauseHelpText
	
	GemRB.HideGUI ()

	if AutopauseOptionsWindow:
		GemRB.UnloadWindow (AutopauseOptionsWindow)
		AutopauseOptionsWindow = None
		GemRB.SetVar ("OtherWindow", GameplayOptionsWindow)
		
		GemRB.UnhideGUI ()
		return

	
	AutopauseOptionsWindow = Window = GemRB.LoadWindow (9)
	GemRB.SetVar ("OtherWindow", AutopauseOptionsWindow)


	AutopauseHelpText = OptHelpText ('AutopauseOptions', Window, 1, 31214)

	OptDone ('AutopauseOptions', Window, 16)
	OptCancel ('AutopauseOptions', Window, 17)

	OptCheckbox ('CharacterHit', Window, 2, 9, 37598)
	OptCheckbox ('CharacterInjured', Window, 3, 10, 37681)
	OptCheckbox ('CharacterDead', Window, 4, 11, 37682)
	OptCheckbox ('CharacterAttacked', Window, 5, 12, 37683)
	OptCheckbox ('WeaponUnusable', Window, 6, 13, 37684)
	OptCheckbox ('TargetGone', Window, 7, 14, 37685)
	OptCheckbox ('EndOfRound', Window, 8, 15, 37686)

	#GemRB.SetVisible (AutopauseOptionsWindow, 1)
	GemRB.UnhideGUI ()
	

def DisplayHelpCharacterHit ():
	GemRB.SetText (AutopauseOptionsWindow, AutopauseHelpText, 37688)

def DisplayHelpCharacterInjured ():
	GemRB.SetText (AutopauseOptionsWindow, AutopauseHelpText, 37689)

def DisplayHelpCharacterDead ():
	GemRB.SetText (AutopauseOptionsWindow, AutopauseHelpText, 37690)

def DisplayHelpCharacterAttacked ():
	GemRB.SetText (AutopauseOptionsWindow, AutopauseHelpText, 37691)

def DisplayHelpWeaponUnusable ():
	GemRB.SetText (AutopauseOptionsWindow, AutopauseHelpText, 37692)

def DisplayHelpTargetGone ():
	GemRB.SetText (AutopauseOptionsWindow, AutopauseHelpText, 37693)

def DisplayHelpEndOfRound ():
	GemRB.SetText (AutopauseOptionsWindow, AutopauseHelpText, 37694)


###################################################
###################################################

def OpenSaveWindow ():
	OpenOptionsWindow ()
	GemRB.SetNextScript ('GUISAVE')
	


###################################################

def OpenLoadMsgWindow ():
	global LoadMsgWindow

	GemRB.HideGUI()

	if LoadMsgWindow:		
		GemRB.UnloadWindow (LoadMsgWindow)
		LoadMsgWindow = None
		GemRB.SetVar ("FloatWindow", -1)
		
		GemRB.UnhideGUI ()
		return
		
	LoadMsgWindow = Window = GemRB.LoadWindow (3)
	GemRB.SetVar ("FloatWindow", LoadMsgWindow)
	
	# Load
	Button = GemRB.GetControl (Window, 0)
	GemRB.SetText (Window, Button, 28648)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "LoadGame")

	# Cancel
	Button = GemRB.GetControl (Window, 1)
	GemRB.SetText (Window, Button, 4196)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenLoadMsgWindow")

	# Loading a game will destroy ...
	Text = GemRB.GetControl (Window, 3)
	GemRB.SetText (Window, Text, 39432)

	GemRB.UnhideGUI ()
	GemRB.ShowModal (Window, MODAL_SHADOW_GRAY)


def LoadGame ():
	OpenOptionsWindow ()
	GemRB.QuitGame ()
	GemRB.SetNextScript ('GUILOAD')



###################################################

def OpenQuitMsgWindow ():
	global QuitMsgWindow

	GemRB.HideGUI()

	if QuitMsgWindow:		
		GemRB.UnloadWindow (QuitMsgWindow)
		QuitMsgWindow = None
		GemRB.SetVar ("FloatWindow", -1)
		GemRB.SetVisible (GemRB.GetVar ("OtherWindow"), 1)
		
		GemRB.UnhideGUI ()
		return
		
	QuitMsgWindow = Window = GemRB.LoadWindow (4)
	GemRB.SetVar ("FloatWindow", QuitMsgWindow)
	GemRB.SetVisible (GemRB.GetVar ("OtherWindow"), 0)
	
	# Save
	Button = GemRB.GetControl (Window, 0)
	GemRB.SetText (Window, Button, 28645)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "SaveGame")

	# Quit Game
	Button = GemRB.GetControl (Window, 1)
	GemRB.SetText (Window, Button, 2595)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "QuitGame")

	# Cancel
	Button = GemRB.GetControl (Window, 2)
	GemRB.SetText (Window, Button, 4196)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenQuitMsgWindow")

	# The game has not been saved ....
	Text = GemRB.GetControl (Window, 3)
	GemRB.SetText (Window, Text, 39430)  # or 39431 - cannot be saved atm

	GemRB.UnhideGUI ()
	GemRB.ShowModal (Window, MODAL_SHADOW_GRAY)


def QuitGame ():
	OpenOptionsWindow ()
	GemRB.QuitGame ()
	GemRB.SetNextScript ('Start')

def SaveGame ():
	OpenOptionsWindow ()
	GemRB.QuitGame ()
	GemRB.SetNextScript ('GUISAVE')


###################################################

key_list = [
	('GemRB', None),
	('Grab pointer', '^G'),
	('Toggle fullscreen', '^F'),
	('Enable cheats', '^T'),
	('', None),
	
	('IE', None),
	('Open Inventory', 'I'),
	('Open Priest Spells', 'P'),
	('Open Mage Spells', 'S'),
	('Pause Game', 'SPC'),
	('Select Weapon', ''),
	('', None),
	]


KEYS_PAGE_SIZE = 60
KEYS_PAGE_COUNT = ((len (key_list) - 1) / KEYS_PAGE_SIZE)+ 1

def OpenKeyboardMappingsWindow ():
	global KeysWindow
	global last_key_action

	last_key_action = None

	GemRB.HideGUI()

	if KeysWindow:		
		GemRB.UnloadWindow (KeysWindow)
		KeysWindow = None
		GemRB.SetVar ("OtherWindow", OptionsWindow)
		
		GemRB.LoadWindowPack ("GUIOPT")
		GemRB.UnhideGUI ()
		return
		
	GemRB.LoadWindowPack ("GUIKEYS")
	KeysWindow = Window = GemRB.LoadWindow (0)
	GemRB.SetVar ("OtherWindow", KeysWindow)


	# Default
	Button = GemRB.GetControl (Window, 3)
	GemRB.SetText (Window, Button, 49051)
	#GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "")	

	# Done
	Button = GemRB.GetControl (Window, 4)
	GemRB.SetText (Window, Button, 1403)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenKeyboardMappingsWindow")	

	# Cancel
	Button = GemRB.GetControl (Window, 5)
	GemRB.SetText (Window, Button, 4196)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenKeyboardMappingsWindow")	

	keys_setup_page (0)


	#GemRB.SetVisible (KeysWindow, 1)
	GemRB.UnhideGUI ()


def keys_setup_page (pageno):
	Window = KeysWindow


	# Page n of n
	Label = GemRB.GetControl (Window, 0x10000001)
	#txt = GemRB.ReplaceVarsInText (49053, {'PAGE': str (pageno + 1), 'NUMPAGES': str (KEYS_PAGE_COUNT)})
	GemRB.SetToken ('PAGE', str (pageno + 1))
	GemRB.SetToken ('NUMPAGES', str (KEYS_PAGE_COUNT))
	GemRB.SetText (Window, Label, 49053)


	for i in range (KEYS_PAGE_SIZE):
		try:
			label, key = key_list[pageno * KEYS_PAGE_SIZE + i]
		except:
			label = ''
			key = None
			

		if key == None:
			# Section header
			Label = GemRB.GetControl (Window, 0x10000005 + i)
			GemRB.SetText (Window, Label, '')

			Label = GemRB.GetControl (Window, 0x10000041 + i)
			GemRB.SetText (Window, Label, label)
			GemRB.SetLabelTextColor (Window, Label, 0, 255, 255)

		else:
			Label = GemRB.GetControl (Window, 0x10000005 + i)
			GemRB.SetText (Window, Label, key)
			GemRB.SetEvent (Window, Label, IE_GUI_LABEL_ON_PRESS, "OnActionLabelPress")	
			GemRB.SetVarAssoc (Window, Label, "KeyAction", i)	
			
			Label = GemRB.GetControl (Window, 0x10000041 + i)
			GemRB.SetText (Window, Label, label)
			GemRB.SetEvent (Window, Label, IE_GUI_LABEL_ON_PRESS, "OnActionLabelPress")	
			GemRB.SetVarAssoc (Window, Label, "KeyAction", i)	
		


last_key_action = None
def OnActionLabelPress ():
	global last_key_action
	
	Window = KeysWindow
	i = GemRB.GetVar ("KeyAction")

	if last_key_action != None:
		Label = GemRB.GetControl (Window, 0x10000005 + last_key_action)
		GemRB.SetLabelTextColor (Window, Label, 255, 255, 255)
		Label = GemRB.GetControl (Window, 0x10000041 + last_key_action)
		GemRB.SetLabelTextColor (Window, Label, 255, 255, 255)
		
	Label = GemRB.GetControl (Window, 0x10000005 + i)
	GemRB.SetLabelTextColor (Window, Label, 255, 255, 0)
	Label = GemRB.GetControl (Window, 0x10000041 + i)
	GemRB.SetLabelTextColor (Window, Label, 255, 255, 0)

	last_key_action = i

	# 49155
	
###################################################

def OpenMoviesWindow ():
	global MoviesWindow

	GemRB.HideGUI()

	if MoviesWindow:		
		GemRB.UnloadWindow (MoviesWindow)
		MoviesWindow = None
		GemRB.SetVar ("FloatWindow", -1)

		GemRB.LoadWindowPack ("GUIOPT")
		GemRB.UnhideGUI ()
		return
		
	GemRB.LoadWindowPack ("GUIMOVIE")
	# FIXME: clean the window to black
	MoviesWindow = Window = GemRB.LoadWindow (0)
	GemRB.SetVar ("FloatWindow", MoviesWindow)


	# Play Movie
	Button = GemRB.GetControl (Window, 2)
	GemRB.SetText (Window, Button, 33034)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OnPlayMoviePress")	

	# Credits
	Button = GemRB.GetControl (Window, 3)
	GemRB.SetText (Window, Button, 33078)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OnCreditsPress")	

	# Done
	Button = GemRB.GetControl (Window, 4)
	GemRB.SetText (Window, Button, 1403)
	GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenMoviesWindow")

	# movie list
	List = GemRB.GetControl (Window, 0)
	GemRB.SetTextAreaSelectable (Window, List, 1)
	GemRB.SetVarAssoc (Window, List, 'SelectedMovie', -1)
	
	#GemRB.SetEvent (Window, Button, IE_GUI_BUTTON_ON_PRESS, "OpenMoviesWindow")


	MovieTable = GemRB.LoadTable ("MOVIDESC")

	for i in range (GemRB.GetTableRowCount (MovieTable)):
		#key = GemRB.GetTableRowName (MovieTable, i)
		desc = GemRB.GetTableValue (MovieTable, i, 0)
		GemRB.TextAreaAppend (Window, List, desc, i)

	GemRB.UnloadTable (MovieTable)


	GemRB.UnhideGUI ()
	GemRB.ShowModal (Window, MODAL_SHADOW_BLACK)


###################################################
def OnPlayMoviePress ():
	selected = GemRB.GetVar ('SelectedMovie')

	# FIXME: This should not happen, when the PlayMovie button gets
	#   properly disabled/enabled, but it does not now
	if selected == -1:
		return
	
	MovieTable = GemRB.LoadTable ("MOVIDESC")
	key = GemRB.GetTableRowName (MovieTable, selected)
	GemRB.UnloadTable (MovieTable)

	GemRB.SetVisible (MoviesWindow, 0)
	GemRB.PlayMovie (key)
	GemRB.SetVisible (MoviesWindow, 1)

###################################################
def OnCreditsPress ():
	GemRB.SetVisible (MoviesWindow, 0)
	GemRB.PlayMovie ("CREDITS")
	GemRB.SetVisible (MoviesWindow, 1)

###################################################
###################################################

# These functions help to setup controls found
#   in Video, Audio, Gameplay, Feedback and Autopause
#   options windows

# These controls are usually made from an active
#   control (button, slider ...) and a label


def OptSlider (name, window, slider_id, label_id, label_strref):
	"""Standard slider for option windows"""
	slider = GemRB.GetControl (window, slider_id)
	#GemRB.SetEvent (window, slider, IE_GUI_MOUSE_OVER_BUTTON, "DisplayHelp" + name)
	
	label = GemRB.GetControl (window, label_id)
	GemRB.SetText (window, label, label_strref)
	GemRB.SetButtonFlags (window, label, IE_GUI_BUTTON_NO_IMAGE, OP_SET)
	GemRB.SetButtonState (window, label, IE_GUI_BUTTON_LOCKED)
	#GemRB.SetEvent (window, label, IE_GUI_MOUSE_OVER_BUTTON, "DisplayHelp" + name)
	GemRB.SetEvent (window, label, IE_GUI_MOUSE_ENTER_BUTTON, "DisplayHelp" + name)

	return slider


def OptCheckbox (name, window, button_id, label_id, label_strref):
	"""Standard checkbox for option windows"""

	button = GemRB.GetControl (window, button_id)
	GemRB.SetButtonFlags (window, button, IE_GUI_BUTTON_CHECKBOX, OP_OR)
	GemRB.SetButtonState (window, button, IE_GUI_BUTTON_SELECTED)
	GemRB.SetEvent (window, button, IE_GUI_MOUSE_OVER_BUTTON, "DisplayHelp" + name)

	label = GemRB.GetControl (window, label_id)
	GemRB.SetText (window, label, label_strref)
	GemRB.SetButtonFlags (window, label, IE_GUI_BUTTON_NO_IMAGE, OP_SET)
	GemRB.SetButtonState (window, label, IE_GUI_BUTTON_LOCKED)
	#GemRB.SetEvent (window, label, IE_GUI_MOUSE_OVER_BUTTON, "DisplayHelp" + name)
	GemRB.SetEvent (window, label, IE_GUI_MOUSE_ENTER_BUTTON, "DisplayHelp" + name)

	return button

def OptButton (name, window, button_id, label_id, label_strref):
	"""Standard subwindow button for option windows"""
	button = GemRB.GetControl (window, button_id)
	GemRB.SetEvent (window, button, IE_GUI_BUTTON_ON_PRESS, "Open%sWindow" %name)	
	GemRB.SetEvent (window, button, IE_GUI_MOUSE_OVER_BUTTON, "DisplayHelp" + name)

	label = GemRB.GetControl (window, label_id)
	GemRB.SetText (window, label, label_strref)
	GemRB.SetButtonFlags (window, label, IE_GUI_BUTTON_NO_IMAGE, OP_SET)
	GemRB.SetButtonState (window, label, IE_GUI_BUTTON_LOCKED)
	#GemRB.SetEvent (window, label, IE_GUI_MOUSE_OVER_BUTTON, "DisplayHelp" + name)
	GemRB.SetEvent (window, label, IE_GUI_MOUSE_ENTER_BUTTON, "DisplayHelp" + name)

def OptDone (name, window, button_id):
	"""Standard `Done' button for option windows"""
	button = GemRB.GetControl (window, button_id)
	GemRB.SetText (window, button, 1403) # Done
	GemRB.SetEvent (window, button, IE_GUI_BUTTON_ON_PRESS, "Open%sWindow" %name)	

def OptCancel (name, window, button_id):
	"""Standard `Cancel' button for option windows"""
	button = GemRB.GetControl (window, button_id)
	GemRB.SetText (window, button, 4196) # Cancel
	GemRB.SetEvent (window, button, IE_GUI_BUTTON_ON_PRESS, "Open%sWindow" %name)	

def OptHelpText (name, window, text_id, text_strref):
	"""Standard textarea with context help for option windows"""
	text = GemRB.GetControl (window, text_id)
	GemRB.SetText (window, text, text_strref)
	return text


###################################################
# End of file GUIOPT.py
