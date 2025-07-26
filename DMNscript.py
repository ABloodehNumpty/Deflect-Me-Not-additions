"""

FUNCTIONS FOR EDITING Deflect Me Not Mod
Script designed to build formatting for certain kinds of updates,
as well as automation updates for certain files pertaining to the Deflect Me Not mod.

-- DMNscript.py written by James Duncan / ABloodehNumpty on nexus
-- DMN mod owned and made by Aiketuido on Nexus
https://www.nexusmods.com/eldenring/mods/4138?tab=description

"""



#############
# Section 1 #
##############################################################################################################
# #   Section of functions for automatically writing and formatting the code/text to update files with    #  #
##############################################################################################################
def printDMN_EventnameIDEntries(current_amount, amount, title1):
    for i in range(1, amount+1):
        print(f'{current_amount+i} = "W_{title1}{i}"')

def printDMN_IDandNameLists(title, startID, amount):
    temp_num = int(startID)
    id_list = []
    name_list = []
    for i in list(range(1, amount+1)):
        id_list.append(str(temp_num))
        name_list.append(title + str(i))
        temp_num +=1
    print(id_list)
    print(name_list)


def printDMN_Functions(title, amount):
    for i in range(1, amount+1):
        print(f"function {title}{i}_onUpdate()\n    Action_AttackAction_onUpdate()\nend\n")

def printDMN_MoveNames(title1, title2, amount):
    i=0
    while i+6 < amount:
        print(f'{title2}{i+1}, {title2}{i+2}, {title2}{i+3}, {title2}{i+4}, {title2}{i+5}, {title2}{i+6} = "W_{title1}{i+1}", "W_{title1}{i+2}", "W_{title1}{i+3}", "W_{title1}{i+4}", "W_{title1}{i+5}", "W_{title1}{i+6}"')
        i+=6
    if i < amount:
        temp1 = ""
        temp2 = ""
        j = 0
        while i < amount:
            temp1 += f'{title2}{i+1}, '
            i+=1
            j+=1
        i-=j
        while i < amount:
            temp2 += f'"W_{title1}{i+1}", '
            i+=1
        print(temp1[:-2] + " = " + temp2[:-2])

def printDMN_AdjustableMoveNames(title1, title2, amount):
    i=0
    while i+6 < amount:
        print(f'{title2}{i+1}, {title2}{i+2}, {title2}{i+3}, {title2}{i+4}, {title2}{i+5}, {title2}{i+6} = "W_{title1}{i+1}", "W_{title1}{i+2}", "W_{title1}{i+3}", "W_{title1}{i+4}", "W_{title1}{i+5}", "W_{title1}{i+6}"')
        i+=6
    if i < amount:
        temp1 = ""
        temp2 = ""
        j = 0
        while i < amount:
            temp1 += f'{title2}{i+1}, '
            i+=1
            j+=1
        i-=j
        while i < amount:
            temp2 += f'"W_{title1}{i+1}", '
            i+=1
        print(temp1[:-2] + " = " + temp2[:-2])

"""ADJUST THESE SETTINGS"""
startID = '912001'
#ID following aXXX_ ID, e.g. a066_'911601'
title1 = "DMN_SuperIsshin"
#Example "DMN_SuperGenichiro" (Name in behavior/DSAnimStudio)
title2 = "SUPER_ISSHIN"
#Example "SUPER_GENICHIRO" 
amount = 31
#Amount of animations of given section
currentEventAmount = 3094
#current number of entires in EventnameID.txt

"""FUNCTION CALLS"""
print("--------------- Event IDs ---------------")
printDMN_EventnameIDEntries(currentEventAmount, amount, title1)
print("--------------- IDs/Names ---------------")
printDMN_IDandNameLists(title1, startID, amount)
print("--------------- Functions ---------------")
printDMN_Functions(title1, amount)
#print("--------------- MoveNames ---------------")
#printDMN_MoveNames(title1, title2, amount)

print("--------------- MoveNames ---------------")
printDMN_AdjustableMoveNames(title1, title2, amount)


#Sekiro Skills ID list, painful to write out, keeping it here (Author explanation: Sekiro skills is not uniform. Unlike larger movesets like Genichiro 1 - 22 or Isshin 1 - 31...
#Sekiro skills section of has lots of different move names since its a large variety.)
#ids = ['911461', '911462', '911463', '911563', '911561', '911562', '911551', '911552', '911553', '911541', '911542', '911543', '911531', '911532', '911533', '911534', '911535', '911536', '911458', '911459', '911460', '911470', '911480', '911481', '911491', '911492', '911493', '911501', '911502', '911511', '911521', '911522']
#Sekiro Skills name list, painful to write, keeping it here
#names = ['DMN_SuperLoadedFireball1', 'DMN_SuperLoadedFireball2', 'DMN_SuperLoadedFireball3', 'DMN_SuperSakuraDance1', 'DMN_SuperShadowrush1', 'DMN_SuperShadowrush2', 'DMN_SuperPrayingStrikes1', 'DMN_SuperPrayingStrikes2', 'DMN_SuperPrayingStrikes3', 'DMN_SuperSenpouLeapingKicks1', 'DMN_SuperSenpouLeapingKicks2', 'DMN_SuperSenpouLeapingKicks3', 'DMN_SuperFloatingPassage1', 'DMN_SuperFloatingPassage2', 'DMN_SuperFloatingPassage3', 'DMN_SuperFloatingPassage4', 'DMN_SuperFloatingPassage5', 'DMN_SuperFloatingPassage6', 'DMN_SuperLoadedShuriken1', 'DMN_SuperLoadedShuriken2', 'DMN_SuperLoadedShuriken3', 'DMN_SuperWhirlwindSlash1', 'DMN_SuperNightjarSlash1', 'DMN_SuperNightjarSlash2', 'DMN_SuperIchimonji1', 'DMN_SuperIchimonji2', 'DMN_SuperIchimonji3', 'DMN_SuperDragonFlash1', 'DMN_SuperDragonFlash2', 'DMN_SuperAshinaCross1', 'DMN_SuperOneMind1', 'DMN_SuperOneMind2']

#############
# Section 2 #
##############################################################################################################
# #                 eventnameids.txt and statenameids.txt update functions                                #  #
##############################################################################################################

#Full list of names and IDs, collected for merging mod for release
FULL_STORED_NAMES = ['DMN_SuperSekiro1', 'DMN_SuperSekiro2', 'DMN_SuperSekiro3', 'DMN_SuperSekiro4', 'DMN_SuperSekiro5', 'DMN_SuperSekiro6', 'DMN_SuperSekiro7', 'DMN_SuperSekiro8', 'DMN_SuperSekiro9', 'DMN_SuperSekiro10', 'DMN_SuperSekiro11', 'DMN_SuperSekiro12',
                     'DMN_SuperLoadedFireball1', 'DMN_SuperLoadedFireball2', 'DMN_SuperLoadedFireball3', 'DMN_SuperSakuraDance1', 'DMN_SuperShadowrush1', 'DMN_SuperShadowrush2', 'DMN_SuperPrayingStrikes1', 'DMN_SuperPrayingStrikes2', 'DMN_SuperPrayingStrikes3', 'DMN_SuperSenpouLeapingKicks1', 'DMN_SuperSenpouLeapingKicks2', 'DMN_SuperSenpouLeapingKicks3', 'DMN_SuperFloatingPassage1', 'DMN_SuperFloatingPassage2', 'DMN_SuperFloatingPassage3', 'DMN_SuperFloatingPassage4', 'DMN_SuperFloatingPassage5', 'DMN_SuperFloatingPassage6', 'DMN_SuperLoadedShuriken1', 'DMN_SuperLoadedShuriken2', 'DMN_SuperLoadedShuriken3', 'DMN_SuperWhirlwindSlash1', 'DMN_SuperNightjarSlash1', 'DMN_SuperNightjarSlash2', 'DMN_SuperIchimonji1', 'DMN_SuperIchimonji2', 'DMN_SuperIchimonji3', 'DMN_SuperDragonFlash1', 'DMN_SuperDragonFlash2', 'DMN_SuperAshinaCross1', 'DMN_SuperOneMind1', 'DMN_SuperOneMind2',
                     'DMN_SuperGenichiro1', 'DMN_SuperGenichiro2', 'DMN_SuperGenichiro3', 'DMN_SuperGenichiro4', 'DMN_SuperGenichiro5', 'DMN_SuperGenichiro6', 'DMN_SuperGenichiro7', 'DMN_SuperGenichiro8', 'DMN_SuperGenichiro9', 'DMN_SuperGenichiro10', 'DMN_SuperGenichiro11', 'DMN_SuperGenichiro12', 'DMN_SuperGenichiro13', 'DMN_SuperGenichiro14', 'DMN_SuperGenichiro15', 'DMN_SuperGenichiro16', 'DMN_SuperGenichiro17', 'DMN_SuperGenichiro18', 'DMN_SuperGenichiro19', 'DMN_SuperGenichiro20', 'DMN_SuperGenichiro21', 'DMN_SuperGenichiro22',
                     'DMN_SuperGreatShinobiOwl1', 'DMN_SuperGreatShinobiOwl2', 'DMN_SuperGreatShinobiOwl3', 'DMN_SuperGreatShinobiOwl4', 'DMN_SuperGreatShinobiOwl5', 'DMN_SuperGreatShinobiOwl6', 'DMN_SuperGreatShinobiOwl7', 'DMN_SuperGreatShinobiOwl8', 'DMN_SuperGreatShinobiOwl9', 'DMN_SuperGreatShinobiOwl10', 'DMN_SuperGreatShinobiOwl11', 'DMN_SuperGreatShinobiOwl12', 'DMN_SuperGreatShinobiOwl13', 'DMN_SuperGreatShinobiOwl14', 'DMN_SuperGreatShinobiOwl15', 'DMN_SuperGreatShinobiOwl16', 'DMN_SuperGreatShinobiOwl17', 'DMN_SuperGreatShinobiOwl18', 'DMN_SuperGreatShinobiOwl19',
                     'DMN_SuperLoneShadow1', 'DMN_SuperLoneShadow2', 'DMN_SuperLoneShadow3', 'DMN_SuperLoneShadow4', 'DMN_SuperLoneShadow5', 'DMN_SuperLoneShadow6', 'DMN_SuperLoneShadow7', 'DMN_SuperLoneShadow8', 'DMN_SuperLoneShadow9', 'DMN_SuperLoneShadow10', 'DMN_SuperLoneShadow11',
                     'DMN_SuperIsshin1', 'DMN_SuperIsshin2', 'DMN_SuperIsshin3', 'DMN_SuperIsshin4', 'DMN_SuperIsshin5', 'DMN_SuperIsshin6', 'DMN_SuperIsshin7', 'DMN_SuperIsshin8', 'DMN_SuperIsshin9', 'DMN_SuperIsshin10', 'DMN_SuperIsshin11', 'DMN_SuperIsshin12', 'DMN_SuperIsshin13', 'DMN_SuperIsshin14', 'DMN_SuperIsshin15', 'DMN_SuperIsshin16', 'DMN_SuperIsshin17', 'DMN_SuperIsshin18', 'DMN_SuperIsshin19', 'DMN_SuperIsshin20', 'DMN_SuperIsshin21', 'DMN_SuperIsshin22', 'DMN_SuperIsshin23', 'DMN_SuperIsshin24', 'DMN_SuperIsshin25', 'DMN_SuperIsshin26', 'DMN_SuperIsshin27', 'DMN_SuperIsshin28', 'DMN_SuperIsshin29', 'DMN_SuperIsshin30', 'DMN_SuperIsshin31'
                    ]



FULL_STORED_IDS = ['911435', '911436', '911437', '911438', '911439', '911440', '911441', '911442', '911443', '911444', '911445', '911446',
                   '911461', '911462', '911463', '911563', '911561', '911562', '911551', '911552', '911553', '911541', '911542', '911543', '911531', '911532', '911533', '911534', '911535', '911536', '911458', '911459', '911460', '911470', '911480', '911481', '911491', '911492', '911493', '911501', '911502', '911511', '911521', '911522',
                   '911601', '911602', '911603', '911604', '911605', '911606', '911607', '911608', '911609', '911610', '911611', '911612', '911613', '911614', '911615', '911616', '911617', '911618', '911619', '911620', '911621', '911622',
                   '911801', '911802', '911803', '911804', '911805', '911806', '911807', '911808', '911809', '911810', '911811', '911812', '911813', '911814', '911815', '911816', '911817', '911818', '911819',
                   '911901', '911902', '911903', '911904', '911905', '911906', '911907', '911908', '911909', '911910', '911911',
                   '912001', '912002', '912003', '912004', '912005', '912006', '912007', '912008', '912009', '912010', '912011', '912012', '912013', '912014', '912015', '912016', '912017', '912018', '912019', '912020', '912021', '912022', '912023', '912024', '912025', '912026', '912027', '912028', '912029', '912030', '912031'
                  ]

def full_stored_event(amount_event, names):
    update_to_add = []
    for i, name in enumerate(names):
        #Append line with added W_ prefix
        update_to_add.append(f'{amount_event+i+1} = "W_{name}"\n')
    return update_to_add
        
    
def full_stored_state(amount_state, names):
    update_to_add = []
    for i, name in enumerate(names):
        update_to_add.append(f'{amount_state+i+1} = "{name}"\n')
    return update_to_add

def updateEvent(file_path, names):
    """
    Function that updates eventnameid.txt

    """
    #Open and read eventnameid.txt
    with open(file_path, "r", encoding="cp932") as f:
        lines = f.readlines()
    #Extract current num value from file lines
    
    current_amount = int(lines[2][6:])
    #New total
    new_amount = current_amount + len(names)
    update_to_add = full_stored_event(current_amount, names)
    #Update Num value
    lines[2] = f"Num  = {new_amount}\n"
    #Prevents accidental user spaces in file causing appended entries from being weirdly spaced
    while lines and lines[-1].strip() == "":
        lines.pop()

    if not lines[-1].endswith('\n'):
        lines[-1] = lines[-1].rstrip() + '\n'
    #Append new entries
    lines.extend(update_to_add)
    #Write to eventnameid.txt
    with open(file_path, "w", encoding="cp932") as f:
        f.writelines(lines)
    #State update is complete
    print("eventnameid.txt update complete.")

def updateState(file_path, names):
    """
    Function that updates statenameid.txt

    """
    #Open and read statenameid.txt
    with open(file_path, "r", encoding="cp932") as f:
        lines = f.readlines()
    #Extract current num value from file lines
    current_amount = int(lines[2][6:])
    #New total
    new_amount = current_amount + len(names)
    update_to_add = full_stored_state(current_amount, names)
    #Update Num value
    lines[2] = f"Num  = {new_amount}\n"
    #Prevents accidental user spaces in file causing appended entries from being weirdly spaced
    while lines and lines[-1].strip() == "":
        lines.pop()

    if not lines[-1].endswith('\n'):
        lines[-1] = lines[-1].rstrip() + '\n'
    #Append new entries
    lines.extend(update_to_add)
    #Write to statenameid.txt
    with open(file_path, "w", encoding="cp932") as f:
        f.writelines(lines)
    #State update is complete
    print("statenameid.txt update complete.")


#event_file_path = "C:\\Users\\james\Desktop\\Mods\\DeflectMeNot\\DMN V3 EXP37 Update Resources\\DMN_V3_EXP37.2\\To be added\DMN-Vanilla\\action\\eventnameid.txt"
#state_file_path = "C:\\Users\\james\Desktop\\Mods\\DeflectMeNot\\DMN V3 EXP37 Update Resources\\DMN_V3_EXP37.2\\To be added\DMN-Vanilla\\action\\statenameid.txt"
test_event_path =  "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\eventnameid.txt"
test_state_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\statenameid.txt"
#updateEvent(test_event_path, FULL_STORED_NAMES)
#updateState(test_state_path, FULL_STORED_NAMES)

#############
# Section 3 #
##############################################################################################################
# #                              c0000.hks update functions                                               #  #
##############################################################################################################
def functionUpdate(new_functions, hks_file_path):
    """
    Function that updates c0000.hks with any new functions for player moves.

    Functions of format:

    function DMN_Title#_onUpdate()
        Action_AttackAction_onUpdate()
    end

    """
    #Open c0000.hks to read
    with open(hks_file_path, "r") as f:
        lines = f.readlines()

    insert_index = None
    for i, line in enumerate(lines):
        #Check for specific area of c0000.hks
        if line.strip() == '--############################################################################--' and lines[i+1].strip() == '-- CUSTOM: End.':
            #This is where new code can go appropriately
            insert_index = i-1
    if insert_index is None:
        raise ValueError("Marker for insertion not found! Check the file structure. DMN has specific markers announcing the beginning and end of CUSTOM area.")
    else:       
        #Splice in new functions in appropriate place
        new_list = lines[:insert_index] + new_functions + ['\n', '\n'] + lines[insert_index:]
        #Write to c0000.hks
        with open(hks_file_path, "w") as f:
            f.writelines(new_list)

def moveUpdate(new_moves, hks_file_path):
    """
    Function that updates c0000.hks with any new move variable assignments.

    Of format:

    MOVE(#), MOVE(%), MOVE($) ... = "W_DMN_Move(#)", "W_DMN_Move(%)", "W_DMN_Move($)" ...
    
    """
    #Open c0000.hks to read
    with open(hks_file_path, "r") as f:
        lines = f.readlines()
    insert_index = None
    for i, line in enumerate(lines):
        #Check for specific area of c0000.hks
        if line.strip() == '-- Table of custom attacks.':
            #This is where new code can go appropriately
            insert_index = i-1
    if insert_index is None:
        raise ValueError("Marker for insertion not found! Check the file structure. DMN has a specific marker referring to Table of Custom Attacks.")
    
    else:       
        #Splice in new functions in appropriate place
        new_list = lines[:insert_index] + ['\n'] + new_moves + ['\n'] + lines[insert_index:]
        #Write to c0000.hks
        with open(hks_file_path, "w") as f:
            f.writelines(new_list)

def updateHKSfile(hks_file_path, move_file_path, function_file_path):
    """
    Main file for updating c0000.hks

    Applies two updates to code, reads the new code/lines from text files to input.

    Formatted to account for keeping tidy newlines, text files should not have any new lines above or below given text.

    """
    #Open move text file to read new moves being added in list format
    with open(move_file_path, "r") as m:
        new_moves = m.readlines()
    #Open function text file to read new functions being added in list format
    with open(function_file_path, "r") as f:
        new_functions = f.readlines()

    #Apply move update
    moveUpdate(new_moves, hks_file_path)
    #Apply function update
    functionUpdate(new_functions, hks_file_path)
    #State it is finished
    print("c0000.hks update complete.")


#hks_file_path = "C:\\Users\\james\Desktop\\Mods\\DeflectMeNot\\DMN V3 EXP37 Update Resources\\DMN_V3_EXP37.2\\To be added\DMN-Vanilla\\action\\script\\c0000.hks"
hks_test_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\c0000.hks"
function_test_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\newfunctions.txt"
move_test_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\newmoves.txt"

#updateHKSfile(hks_test_path, move_test_path, function_test_path)

#############
# Section 4 #
##############################################################################################################
# #                              c0000.anibnd.dcxc / a66.tae update functions                              # #
##############################################################################################################

test_tae_update_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\c0000.anibnd.dcx"
new_tae_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\a66.tae"
witchybnd_path = "C:\\Users\\james\\Desktop\\Mods\\WitchyBND\\WitchyBND.exe"

import subprocess
import shutil
import os

def replace_a66_tae(anibnd_path, new_tae_path, witchybnd_path):
    """
    Takes an updated a66.tae and replaces the old one in c0000.anibnd.dcx.

    Uses Witchybnd to unpack c0000.anibnd.dcx, replaces the a66.tae, then repacks.
    """
    #Gather directories
    base_dir = os.path.dirname(anibnd_path)
    file_base = os.path.basename(anibnd_path).replace(".", "-") + "-wanibnd"
    extracted_dir = os.path.join(base_dir, file_base)

    #Unpack c0000.anibnd.dcx
    subprocess.run([witchybnd_path, anibnd_path], check=True)

    #Replace a66.tae
    tae_target_path = os.path.join(
        extracted_dir, "INTERROOT_win64", "chr", "c0000", "tae", "a66.tae"
    )
    shutil.copyfile(new_tae_path, tae_target_path)

    #Repack the folder
    subprocess.run([witchybnd_path, extracted_dir], check=True)

    #State that the update is complete.
    print(f"c0000.anibnd.dcx updated with new a66.tae")

#replace_a66_tae(test_tae_update_path, new_tae_path, witchybnd_path)

#############
# Section 5 #
##############################################################################################################
# #                              SFX/sfxbnd_commoneffects_dlc02.ffxbnd.dcx update functions                # #
##############################################################################################################

test_sfx_file = "C:\\Users\\james\\Desktop\\Test folder\\Code Testing\\sfxbnd_commoneffects_dlc02.ffxbnd.dcx"
test_EffectsToBeAdded = "C:\\Users\\james\\Desktop\\Test folder\\Code Testing\\effects-to-be-added"
witchybnd_path = "C:\\Users\\james\\Desktop\\Mods\\WitchyBND\\WitchyBND.exe" #Already above but putting here for clarity


def replace_sfx_effects(base_path, effects_dir, witchybnd_path):
    base_dir = os.path.dirname(base_path)
    file_base = os.path.basename(base_path).replace(".", "-") + "-wffxbnd"
    extracted_dir = os.path.join(base_dir, file_base)

    #Unpack
    subprocess.run([witchybnd_path, base_path], check=True)

    #Copy all effects
    sfx_target_dir = os.path.join(
        extracted_dir, "effect"
    )
    #Check effects directory is present
    if not os.path.isdir(sfx_target_dir):
        raise FileNotFoundError(f"SFX target folder not found: {sfx_target_dir}")
    
    #Check if effects-to-be-added is empty, return function early if so (nothing to add)
    if len(os.listdir(effects_dir)) < 1:
        print("effects-to-be-added empty, add any sfx files you wish to add to file!")
        return
    #Copy all effects
    for filename in os.listdir(effects_dir):
        src = os.path.join(effects_dir, filename)
        dst = os.path.join(sfx_target_dir, filename)
        shutil.copy2(src, dst)  #replaces if exists, adds if not
        print(f"Added: {filename}")

    #Repack
    subprocess.run([witchybnd_path, extracted_dir], check=True)
    print("sfxbnd_commoneffects_dlc02.ffxbnd.dcx update complete.")

#replace_sfx_effects(test_sfx_file, test_EffectsToBeAdded, witchybnd_path)


#############
# Section 6 #
##############################################################################################################
# #                                           Main function                                                # #
##############################################################################################################

#Paths of DMN variants being updated, these will be manually changed
DMN_variants_to_update = "C:\\Users\\james\\Desktop\\Mods\\DeflectMeNot\\DMN V3 EXP37 Update Resources\\DMN_V3_EXP37.2\\To be added"
#Paths of files within each DMN folder, this remains constant
hks_path = "C:\\action\\script\\c0000.hks"
event_path = "C:\\action\\eventnameid.txt"
state_path = "C:\\action\\statenameid.txt"
anibnd_path = "C:\\chr\\c0000.anibnd.dcx" #Any edits on the file being replaced are done by DSAnimStudio by MeowMaritus
sfx_path = "C:\\sfx\\sfxbnd_commoneffects_dlc02.ffxbnd.dcx"
#Files that are yet to be automated, not included in updateMods() till then
behavior_path = "C:\\chr\\c0000.behbnd.dcx" #Uses a python script someone else provided to the mod community, BEH injector
regulation_path = "C:\\regulation.bin" #Regulation.bin is updated via Smithbox app

#Update locations
updated_files_folder = "C:\\Users\\james\\Desktop\\Mods\\DeflectMeNot\\DMN V3 EXP37 Update Resources\\DMN_V3_EXP37.2\\Updated files"
hks_update = os.path.join(updated_files_folder, "C:\\hks update")
tae_update = os.path.join(updated_files_folder, "C:\\anibnd update\\a66.tae")
sfx_update = os.path.join(updated_files_folder, "C:\\sfx update\\effects-to-be-added")

#Details needed for some functions below

#WitchyBND path, needed for unpacking/repacking folders
witchy_bnd_path = "C:\\Users\\james\\Desktop\\Mods\\WitchyBND\\WitchyBND.exe"

#Full list of names and IDs, collected for merging mod for release
#These were collected manually by using the helper functions in Section 1, if editing same moves in future these are not required for updates again, only for new moves/animations
#Needed for adding event/states (Autonomous) and BEH injector (Not used autonomously yet)
STORED_NAMES = ['DMN_SuperSekiro1', 'DMN_SuperSekiro2', 'DMN_SuperSekiro3', 'DMN_SuperSekiro4', 'DMN_SuperSekiro5', 'DMN_SuperSekiro6', 'DMN_SuperSekiro7', 'DMN_SuperSekiro8', 'DMN_SuperSekiro9', 'DMN_SuperSekiro10', 'DMN_SuperSekiro11', 'DMN_SuperSekiro12',
                     'DMN_SuperLoadedFireball1', 'DMN_SuperLoadedFireball2', 'DMN_SuperLoadedFireball3', 'DMN_SuperSakuraDance1', 'DMN_SuperShadowrush1', 'DMN_SuperShadowrush2', 'DMN_SuperPrayingStrikes1', 'DMN_SuperPrayingStrikes2', 'DMN_SuperPrayingStrikes3', 'DMN_SuperSenpouLeapingKicks1', 'DMN_SuperSenpouLeapingKicks2', 'DMN_SuperSenpouLeapingKicks3', 'DMN_SuperFloatingPassage1', 'DMN_SuperFloatingPassage2', 'DMN_SuperFloatingPassage3', 'DMN_SuperFloatingPassage4', 'DMN_SuperFloatingPassage5', 'DMN_SuperFloatingPassage6', 'DMN_SuperLoadedShuriken1', 'DMN_SuperLoadedShuriken2', 'DMN_SuperLoadedShuriken3', 'DMN_SuperWhirlwindSlash1', 'DMN_SuperNightjarSlash1', 'DMN_SuperNightjarSlash2', 'DMN_SuperIchimonji1', 'DMN_SuperIchimonji2', 'DMN_SuperIchimonji3', 'DMN_SuperDragonFlash1', 'DMN_SuperDragonFlash2', 'DMN_SuperAshinaCross1', 'DMN_SuperOneMind1', 'DMN_SuperOneMind2',
                     'DMN_SuperGenichiro1', 'DMN_SuperGenichiro2', 'DMN_SuperGenichiro3', 'DMN_SuperGenichiro4', 'DMN_SuperGenichiro5', 'DMN_SuperGenichiro6', 'DMN_SuperGenichiro7', 'DMN_SuperGenichiro8', 'DMN_SuperGenichiro9', 'DMN_SuperGenichiro10', 'DMN_SuperGenichiro11', 'DMN_SuperGenichiro12', 'DMN_SuperGenichiro13', 'DMN_SuperGenichiro14', 'DMN_SuperGenichiro15', 'DMN_SuperGenichiro16', 'DMN_SuperGenichiro17', 'DMN_SuperGenichiro18', 'DMN_SuperGenichiro19', 'DMN_SuperGenichiro20', 'DMN_SuperGenichiro21', 'DMN_SuperGenichiro22',
                     'DMN_SuperGreatShinobiOwl1', 'DMN_SuperGreatShinobiOwl2', 'DMN_SuperGreatShinobiOwl3', 'DMN_SuperGreatShinobiOwl4', 'DMN_SuperGreatShinobiOwl5', 'DMN_SuperGreatShinobiOwl6', 'DMN_SuperGreatShinobiOwl7', 'DMN_SuperGreatShinobiOwl8', 'DMN_SuperGreatShinobiOwl9', 'DMN_SuperGreatShinobiOwl10', 'DMN_SuperGreatShinobiOwl11', 'DMN_SuperGreatShinobiOwl12', 'DMN_SuperGreatShinobiOwl13', 'DMN_SuperGreatShinobiOwl14', 'DMN_SuperGreatShinobiOwl15', 'DMN_SuperGreatShinobiOwl16', 'DMN_SuperGreatShinobiOwl17', 'DMN_SuperGreatShinobiOwl18', 'DMN_SuperGreatShinobiOwl19',
                     'DMN_SuperLoneShadow1', 'DMN_SuperLoneShadow2', 'DMN_SuperLoneShadow3', 'DMN_SuperLoneShadow4', 'DMN_SuperLoneShadow5', 'DMN_SuperLoneShadow6', 'DMN_SuperLoneShadow7', 'DMN_SuperLoneShadow8', 'DMN_SuperLoneShadow9', 'DMN_SuperLoneShadow10', 'DMN_SuperLoneShadow11',
                     'DMN_SuperIsshin1', 'DMN_SuperIsshin2', 'DMN_SuperIsshin3', 'DMN_SuperIsshin4', 'DMN_SuperIsshin5', 'DMN_SuperIsshin6', 'DMN_SuperIsshin7', 'DMN_SuperIsshin8', 'DMN_SuperIsshin9', 'DMN_SuperIsshin10', 'DMN_SuperIsshin11', 'DMN_SuperIsshin12', 'DMN_SuperIsshin13', 'DMN_SuperIsshin14', 'DMN_SuperIsshin15', 'DMN_SuperIsshin16', 'DMN_SuperIsshin17', 'DMN_SuperIsshin18', 'DMN_SuperIsshin19', 'DMN_SuperIsshin20', 'DMN_SuperIsshin21', 'DMN_SuperIsshin22', 'DMN_SuperIsshin23', 'DMN_SuperIsshin24', 'DMN_SuperIsshin25', 'DMN_SuperIsshin26', 'DMN_SuperIsshin27', 'DMN_SuperIsshin28', 'DMN_SuperIsshin29', 'DMN_SuperIsshin30', 'DMN_SuperIsshin31'
                    ]


#Needed for BEH injector (Not used autonomously yet)
STORED_IDS = ['911435', '911436', '911437', '911438', '911439', '911440', '911441', '911442', '911443', '911444', '911445', '911446',
                   '911461', '911462', '911463', '911563', '911561', '911562', '911551', '911552', '911553', '911541', '911542', '911543', '911531', '911532', '911533', '911534', '911535', '911536', '911458', '911459', '911460', '911470', '911480', '911481', '911491', '911492', '911493', '911501', '911502', '911511', '911521', '911522',
                   '911601', '911602', '911603', '911604', '911605', '911606', '911607', '911608', '911609', '911610', '911611', '911612', '911613', '911614', '911615', '911616', '911617', '911618', '911619', '911620', '911621', '911622',
                   '911801', '911802', '911803', '911804', '911805', '911806', '911807', '911808', '911809', '911810', '911811', '911812', '911813', '911814', '911815', '911816', '911817', '911818', '911819',
                   '911901', '911902', '911903', '911904', '911905', '911906', '911907', '911908', '911909', '911910', '911911',
                   '912001', '912002', '912003', '912004', '912005', '912006', '912007', '912008', '912009', '912010', '912011', '912012', '912013', '912014', '912015', '912016', '912017', '912018', '912019', '912020', '912021', '912022', '912023', '912024', '912025', '912026', '912027', '912028', '912029', '912030', '912031'
                  ]

def updateMods(DMN_variants_to_update, hks_path_boolean, event_path_boolean, state_path_boolean, anibnd_path_boolean, sfx_path_boolean):
    """
    Main function that applies all updates user wants to apply.

    Highly advise throughly checking everything above to ensure it is correctly written so you're not updating wrong things.

    Double check that the previous editions details are not still written in, overwriting previous versions is bad :)
    """

    #Error checks
    if DMN_variants_to_update == None:
        print("Path isn't specified. Add a path to the DMN variants folder for your update.")
        return
    if (hks_path_boolean == None) or (event_path_boolean == None) or (state_path_boolean == None) or (anibnd_path_boolean == None) or (sfx_path_boolean == None):
        print("Ensure you are stating booleans true/false for each potential update, no accidentals allowed!")
        return
    if (hks_path_boolean == False) and (event_path_boolean == False) and (state_path_boolean == False) and (anibnd_path_boolean == False) and (sfx_path_boolean == False):
        print("You have successfully updated nothing, try changing something to True.")
    
    #Loop through folder with all variants/merges of DMN
    for filename in os.listdir(DMN_variants_to_update):
        #Create path to the DMN variants folder
        variant_folder = os.path.join(DMN_variants_to_update, filename)

        #Check if updating c0000.hks
        if hks_path_boolean == True:
            variant_hks_path = os.path.join(variant_folder, hks_path)
            new_moves = os.path.join(hks_update, "C:\\newmoves.txt")
            new_functions = os.path.join(hks_update, "C:\\newfunctions.txt")
            updateHKSfile(variant_hks_path, new_moves, new_functions)
        
        #Check if updating eventnameid.txt, if true then state_path_boolean ought to be true too (Your call!)
        if event_path_boolean == True:
            variant_event_path = os.path.join(variant_folder, event_path)
            updateEvent(variant_event_path, STORED_NAMES)
        #Check if updating statenameid.txt, if true then event_path_boolean ought to be true too (Your call!)
        if state_path_boolean == True:
            variant_state_path = os.path.join(variant_folder, state_path)
            updateState(variant_state_path, STORED_NAMES)
        
        #Check if updating a66.tae in c0000.anibnd.dcx
        if anibnd_path_boolean == True:
            variant_anibnd_path = os.path.join(variant_folder, anibnd_path)
            replace_a66_tae(variant_anibnd_path, tae_update, witchy_bnd_path)
        
        #Check if updating sfx files
        if sfx_path_boolean == True:
            variant_sfx_path = os.path.join(variant_folder, sfx_path)
            replace_sfx_effects(variant_sfx_path, sfx_update, witchy_bnd_path)
        
        #State that all updates are complete!
        print("All updates complete.")
            
        
#Magic button, only run if certain...
#updateMods(DMN_variants_to_update, True, True, True, True, True)