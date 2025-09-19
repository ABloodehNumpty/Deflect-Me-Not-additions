"""

FUNCTIONS FOR EDITING Deflect Me Not Mod
Script designed to build formatting for certain kinds of updates,
as well as automation updates for certain files pertaining to the Deflect Me Not mod.

-- DMNscript.py written by James Duncan / ABloodehNumpty on nexus
-- DMN mod owned and made by Aiketuido on Nexus
https://www.nexusmods.com/eldenring/mods/4138?tab=description

"""
import subprocess
import shutil
import os
import csv
import xml.etree.ElementTree as ET
import time
import re


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

def helperMain(startID, title1, title2, amount, currentEventAmount):
    """
    Main function that prints out the necessary 
    information for moves being added to DMN

    Laid out for simple copy/paste to other files
    """
    print("--------------- Event IDs ---------------")
    printDMN_EventnameIDEntries(currentEventAmount, amount, title1)
    print("--------------- IDs/Names ---------------")
    printDMN_IDandNameLists(title1, startID, amount)
    print("--------------- Functions ---------------")
    printDMN_Functions(title1, amount)
    #Redundant version of method below
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

#Full list of names and IDs, collected for merging mod for release.
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
#test_event_path =  "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\eventnameid.txt"
#test_state_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\statenameid.txt"
#updateEvent(test_event_path, FULL_STORED_NAMES)
#updateState(test_state_path, FULL_STORED_NAMES)

#############
# Section 3 #
##############################################################################################################
# #                              c0000.hks update functions                                               #  #
##############################################################################################################

def updateSuperFindAttackFunction(new_func, hks_file_path):
    """
    Function that updates c0000.hks Combo_FindAttackInComboTable function to include Super Combos feature
    
    """
    with open(hks_file_path, "r") as f:
        hks_content = f.read()
    
    pattern = re.compile(
        r"(function\s+Combo_FindAttackInComboTable[\s\S]*?)(?=function\s+Combo_OverrideAttack)",
        re.MULTILINE
    )
    
    replacement = new_func.rstrip() + "\n\n"
    updated_content, count = pattern.subn(replacement, hks_content)

    if count == 0:
        raise ValueError("Function Combo_FindAttackInComboTable not found in file or Combo_OverrideAttack anchor missing.")
    
    elif count > 1: 
        raise ValueError("Function Combo_FindAttackInComboTable appears multiple times, careful with your copy pastes!")

    # Write back to file
    with open(hks_file_path, "w") as w:
        w.write(updated_content)

    print(f"Replaced Combo_FindAttackInComboTable in {hks_file_path}")

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
    print("Initalizing .hks update...")
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
#hks_test_path = "C:\\Desktop\\Test folder\\Code Testing\\c0000.hks"
#function_test_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\newfunctions.txt"
#move_test_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\newmoves.txt"
#super_function_test = REMOVED BECAUSE BIG

#updateHKSfile(hks_test_path, move_test_path, function_test_path)
#updateSuperFindAttackFunction(super_function_test, hks_test_path)

#############
# Section 4 #
##############################################################################################################
# #                              c0000.anibnd.dcxc / a66.tae update functions                              # #
##############################################################################################################

#test_tae_update_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\c0000.anibnd.dcx"
#new_tae_path = "C:\\Users\\james\Desktop\\Test folder\\Code Testing\\a66.tae"
#witchybnd_path = "C:\\Users\\james\\Desktop\\Mods\\WitchyBND\\WitchyBND.exe"

def replace_a66_tae(anibnd_path, new_tae_path, witchybnd_path):
    """
    Takes an updated a66.tae and replaces the old one in c0000.anibnd.dcx.

    Uses Witchybnd to unpack c0000.anibnd.dcx, replaces the a66.tae, then repacks.
    """
    print("Initializing a66 tae update...")
    #Gather directories
    base_dir = os.path.dirname(anibnd_path)
    file_base = os.path.basename(anibnd_path).replace(".", "-") + "-wanibnd"
    extracted_dir = os.path.join(base_dir, file_base)

    #Unpack c0000.anibnd.dcx
    subprocess.run([witchybnd_path, anibnd_path], check=True, stdout=subprocess.DEVNULL)

    #Replace a66.tae
    tae_target_path = os.path.join(
        extracted_dir, "INTERROOT_win64", "chr", "c0000", "tae", "a66.tae"
    )
    shutil.copyfile(new_tae_path, tae_target_path)

    #Repack the folder
    subprocess.run([witchybnd_path, extracted_dir], check=True, stdout=subprocess.DEVNULL)

    #State that the update is complete.
    print(f"c0000.anibnd.dcx updated with new a66.tae")
    
    #Delete the unpacked folder, as it is now redundant clutter
    if os.path.exists(extracted_dir):
        shutil.rmtree(extracted_dir)
        print(f"Deleted unpacked folder: {extracted_dir}")
    else:
        print(f"Unpacked folder not found: {extracted_dir}")

#replace_a66_tae(test_tae_update_path, new_tae_path, witchybnd_path)

#############
# Section 5 #
##############################################################################################################
# #                              SFX/sfxbnd_commoneffects_dlc02.ffxbnd.dcx update functions                # #
##############################################################################################################

#test_sfx_file = "C:\\Users\\james\\Desktop\\Test folder\\Code Testing\\sfxbnd_commoneffects_dlc02.ffxbnd.dcx"
#test_EffectsToBeAdded = "C:\\Users\\james\\Desktop\\Test folder\\Code Testing\\effects-to-be-added"
#witchybnd_path = "C:\\Desktop\\Mods\\WitchyBND\\WitchyBND.exe" #Already above but putting here for clarity


def replace_sfx_effects(base_path, effects_dir, witchybnd_path):
    """
    
    """
    print("Initalizing sfx update...")
    #Initialize
    base_dir = os.path.dirname(base_path)
    file_base = os.path.basename(base_path).replace(".", "-") + "-wffxbnd"
    extracted_dir = os.path.join(base_dir, file_base)

    #Unpack
    subprocess.run([witchybnd_path, base_path], check=True, stdout=subprocess.DEVNULL)

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
    subprocess.run([witchybnd_path, extracted_dir], check=True, stdout=subprocess.DEVNULL)
    print("sfxbnd_commoneffects_dlc02.ffxbnd.dcx update complete.")
    
    #Delete the unpacked folder, as it is now redundant clutter
    if os.path.exists(extracted_dir):
        shutil.rmtree(extracted_dir)
        print(f"Deleted unpacked folder: {extracted_dir}")
    else:
        print(f"Unpacked folder not found: {extracted_dir}")

#replace_sfx_effects(test_sfx_file, test_EffectsToBeAdded, witchybnd_path)

#############
# Section 6 #
##############################################################################################################
# #                                           BEH Injector script calling function                         # #
##############################################################################################################

#Paths to tools used in Section 6
hklib_path_test = "C:\\Desktop\\Mods\\HKLibCLI.v0.1.2\\net7.0\\HKLib.CLI.exe"
erbeh_injector_test = "C:\\Desktop\\Mods\\ERBEHInjector"
witchybnd_test = "C:\\Desktop\\Mods\\WitchyBND\\WitchyBND.exe"
#c0000.behbnd.dcx path
beh_test_path = "C:\\Desktop\\Test folder\\Code Testing\\c0000.behbnd.dcx"
#Variables that script will change in the other script file, test names
#Variables like stateMachineParent ('Attack_SM') and taeSection ('a066_') remain as are
#This is because we are updating Attacks for time being, and DMN only uses a066 TAE file
IDs_test = ['913001', '913002', '913003']
names_test = ['SuperCrazyMove1', 'SuperCrazyMove2', 'SuperCrazyMove3']

def updateBEHfile(behbnd_path, witchybnd_path, hklib_path, erbeh_injector_dir, ids, names):
    """
    Updates the behavior file (c0000.behbnd.dcx) with new states via XML injection.

    1. Unpacks behbnd.dcx via WitchyBND
    2. Converts c0000.hkx -> XML
    3. Injects states using ERBehXmlInjector
    4. Converts modified XML -> c0000.hkx
    5. Repacks behavior folder back to .dcx
    """
    print("Initalizing Behavior update...")
    #Initialize, collect directories of appropriate areas
    base_dir = os.path.dirname(behbnd_path)
    folder_name = os.path.basename(behbnd_path).replace(".", "-")
    extracted_path = os.path.join(base_dir, folder_name)
    hkx_path = os.path.join(extracted_path, "Behaviors\\c0000.hkx")
    erbeh_injector_path = os.path.join(erbeh_injector_dir, "ERBehXmlInjector.py")
    xml_path = os.path.join(erbeh_injector_dir, "c0000.xml")
    #Part 1. Unpack with WitchyBND
    print("[1/6] Unpacking behavior file...")
    subprocess.run([witchybnd_path, behbnd_path], check=True, stdout=subprocess.DEVNULL)
    print(f"Checking if .hkx file exists at: {hkx_path}")
    print(f"File exists: {os.path.exists(hkx_path)}")
    #Part 2. Convert HKX to XML
    print("[2/6] Converting .hkx to .xml...")
    subprocess.run([hklib_path, hkx_path], check=True)

    #Move the generated XML to your target path
    auto_xml_path = os.path.splitext(hkx_path)[0] + ".xml"
    shutil.move(auto_xml_path, xml_path)
    print(f"Moved generated XML to: {xml_path}")

    #Part 3. Inject via ERBehXmlInjector.py
    print("[3/6] Injecting XML changes with ERBehXmlInjector...")
    with open(erbeh_injector_path, "r", encoding="utf-8") as file:
        script_content = file.read()

    #Rewrite ERBehXmlInjector.py variables dynamically
    #IDs/Names are set to [...] as placeholders in ERBehXmlInjector.py
    #This is not a default setting when initially downloading ERBehXmlInjector.py
    #Please adjust each to [...] to ensure this script runs.
    script_content = script_content.replace("IDs = [...]", f"IDs = {ids}")
    script_content = script_content.replace("Names = [...]", f"Names = {names}")

    #Write a temporary copy of script with adjusted variables to execute
    temp_script = os.path.join(erbeh_injector_dir, "ERBehXmlInjector_temp.py")
    with open(temp_script, "w", encoding="utf-8") as file:
        file.write(script_content)
    #Run the temporary script. Also have an automatic '\n' input to auto-bypass the 'Enter to continue...' prompt
    subprocess.run(["python", temp_script], input=b"\n", check=True)
    #Delete the temporary script
    if os.path.exists(temp_script):
        os.remove(temp_script)
        print(f"Deleted temporary script: {temp_script}")
    else:
        print(f"Temporary script python file not found: {temp_script}")

    #Part 4. Convert XML back to HKX
    print("[4/6] Converting modified .xml to .hkx...")
    subprocess.run([hklib_path, xml_path], check=True)
    
    #Move the generated hkx file back to original folder, replace old one
    auto_hkx_path = os.path.splitext(xml_path)[0] + ".hkx"
    shutil.move(auto_hkx_path, hkx_path)
    print(f"Moved generated HKX to: {hkx_path}")

    #Delete the XML, as it is now redundant clutter
    if os.path.exists(xml_path):
        os.remove(xml_path)
        print(f"Deleted temporary XML: {xml_path}")
    else:
        print(f"c0000.xml file not found: {xml_path}")

    # Step 5: Repack
    print("[5/6] Repacking behavior folder...")
    subprocess.run([witchybnd_path, extracted_path], check=True, stdout=subprocess.DEVNULL)
    
    #Delete the unpacked folder, as it is now redundant clutter
    if os.path.exists(extracted_path):
        shutil.rmtree(extracted_path)
        print(f"Deleted unpacked folder: {extracted_path}")
    else:
        print(f"Unpacked folder not found: {extracted_path}")

    print("[6/6] Behavior file updated successfully.")
    
#updateBEHfile(beh_test_path, witchybnd_test, hklib_path_test, erbeh_injector_test, IDs_test, names_test)

#############
# Section 7 #
##############################################################################################################
# #                                           Regulation.bin Update Function                               # #
##############################################################################################################

reg_bin_test = "C:\\Desktop\\Test folder\\Code Testing\\param-update\\regulation.bin"
param_test_location = "C:\\Desktop\\Test folder\\Code Testing\\param-update\\param update"
witchybnd_test = "C:\\Desktop\\Mods\\WitchyBND\\WitchyBND.exe"
update_source = "C:\\Desktop\\Test folder\\Code Testing\\param-update\\source regulation bin\\regulation.bin"

def updateRegBinfile(regulation_bin_path, param_update_location, witchybnd_path):
    """
    Updates the regulation.bin file by extracting XMLs and adding information from given CSVs.

    1. Unpack regulation.bin and source regulation.bin (one with the updated lines in it)
    2. Loop through given update CSVs:
        A. Unpack .param of same name as CSV in both regulation-bin's
        B. Read CSV and get the id values of lines being added as a list
        C. Read .xml of same name that was unpacked from source reg-bin
        D. Copy the lines of each id to a list
        E. Write lines to and sort .xml being updated.
        F. Delete source .xml as it is now finished with.
        G. Repack .xml to .param
        H. Delete .param.bak (backup) and .xml to save space. 
    3. After looping through CSVs, repack regulation-bin and delete source regulation-bin.
    4. Delete regulation-bin after repack, as it is now unnecessary clutter.
    
    Note: Chose to leave regulation.bin's backup, gives user a backup if update isn't working. 
          Deleted the param.bak and not this one because the regulation.bin backup backs that up already.
    
    """
    print("Initalizing...")
    #Establish main directories
    base_dir = os.path.dirname(regulation_bin_path)
    source_dir = os.path.join(param_update_location, "source regulation bin")
    source_regulation_bin_path = os.path.join(source_dir, "regulation.bin")
    folder_name = os.path.basename(regulation_bin_path).replace(".", "-")
    source_folder_name = os.path.basename(source_regulation_bin_path).replace(".", "-")
    extracted_path = os.path.join(base_dir, folder_name)
    source_extracted_path = os.path.join(source_dir, source_folder_name)
    param_csv_location = os.path.join(param_update_location, "param update")
    #Unpack regulation.bin for update, and the update source regulation.bin
    subprocess.run([witchybnd_path, "-u", regulation_bin_path], check=True, stdout=subprocess.DEVNULL)
    subprocess.run([witchybnd_path, "-u", source_regulation_bin_path], check=True, stdout=subprocess.DEVNULL)
    time.sleep(0.1)
    #Loop through given param updates
    for filename in os.listdir(param_csv_location):
        print(f"Unpacking... updating params using {filename}")
        #Get directories for specific params files/extracted files
        param_file = filename[:-3] + 'param'
        xml_file = param_file + '.xml' #It merely appends .xml when Witchybnd extracts it (.param.xml)
        backup_file = param_file + '.bak'
        #File paths within the extracted folder
        csv_path = os.path.join(param_csv_location, filename)
        param_path = os.path.join(extracted_path, param_file)
        xml_path = os.path.join(extracted_path, xml_file)
        backup_path = os.path.join(extracted_path, backup_file)
        #Source paths within the source extracted folder
        source_param_path = os.path.join(source_extracted_path, param_file)
        source_xml_path = os.path.join(source_extracted_path, xml_file)
        #Unpack .param to .param.xml
        subprocess.run([witchybnd_path, param_path], check=True, stdout=subprocess.DEVNULL)
        time.sleep(0.1)
        #Unpack source .param to source .param.xml
        subprocess.run([witchybnd_path, source_param_path], check=True, stdout=subprocess.DEVNULL)
        time.sleep(0.1)
        #Run update_param to add information from csv to the xml (Also sorting the xml)
        update_param(xml_path, source_xml_path, csv_path)
        #Repack .param.xml to .param
        subprocess.run([witchybnd_path, "-p", xml_path], check=True, stdout=subprocess.DEVNULL)
        #subprocess.run([witchybnd_path, xml_path], check=True, stdout=subprocess.DEVNULL)
        #Short delay to ensure repacking before deletion
        time.sleep(0.1)
        #State file has been updated
        print(f"Updated: {param_file}")

        #Delete .param.xml file
        if os.path.exists(xml_path):
            os.remove(xml_path)
            print(f"Deleted: {xml_file}")
        else:
            print(f"File not found: {xml_file}")
        
        #Delete source .param.xml file. This happens later anyways when source folder gets deleted, since it does not get repacked, but better to reduce any clutter asap.
        if os.path.exists(source_xml_path):
            os.remove(source_xml_path)
            print(f"Deleted at source folder: {xml_file}")
        else:
            print(f"File not found at source solder: {xml_file}")

        #Delete .param.bak file
        if os.path.exists(backup_path):
            os.remove(backup_path)
            print(f"Deleted: {backup_file}")
        else:
            print(f"File not found: {backup_file}")
        
        print("----------------------------------------------")
        
    #State all files have been updated
    print("All param updates complete. Repacking...")
    #Repack regulation-bin
    subprocess.run([witchybnd_path, "-p", extracted_path], check=True, stdout=subprocess.DEVNULL)
    print("regulation.bin update complete.")

    #Delete source regulation-bin, as is now clutter
    if os.path.exists(source_extracted_path):
        shutil.rmtree(source_extracted_path)
        print(f"Deleted folder: {source_extracted_path}")
    else:
        print(f"Folder not found: {source_extracted_path}")
    #Delete regulation-bin, as is now clutter
    if os.path.exists(extracted_path):
        shutil.rmtree(extracted_path)
        print(f"Deleted folder: {extracted_path}")
    else:
        print(f"Folder not found: {extracted_path}")
    
    print("Clutter deleted! All done!")

def update_param(xml_path, source_xml_path, csv_path):
    """
        1. Read CSV and get the id values of lines being added as a list
        2. Read source .xml
        3. Copy the lines of related to each id to a list
        4. Write lines to and sort .xml being updated.
    """
    #Working logic of getting the IDs from the CSV
    #Open and read CSV file contents
    with open(csv_path, "r", encoding="utf-8") as csv_file:
        csv_contents = csv_file.readlines()
    #Ensure choosing IDs index correctly, might change in future CSVs, so better to be fluid than assuming 0 index always
    for i, value in enumerate(csv_contents[0].split(',')):
        if value == "ID":
            id_index = i
    #Collect IDs to parse for in xml files
    id_list = []
    for entry in csv_contents[1:]:
        entry_list = entry.split(',')
        id_list.append(entry_list[id_index])

    #Open source xml file and read contents
    with open(source_xml_path, "r", encoding="utf-8") as source_xml:
        source_xml_content = source_xml.readlines()
    #Initialize xml parse
    start_index = None
    xml_lines = []
    for index, line in enumerate(source_xml_content):
        #Search for when rows begins
        if line == "<rows>\n":
            start_index = index
        #End early when rows ends
        elif line == "</rows>\n": 
            break
        #Check lines to see if they contain ID in CSV, if so, copy line to list
        if start_index != None:
            for id in id_list:
                if f'<row id="{id}"' in line:
                    xml_lines.append(line)
    
    #Open destination xml file and read contents
    with open(xml_path, "r", encoding="utf-8") as xml:
        xml_content = xml.readlines()
    #Initialize xml parse
    for index, line in enumerate(xml_content):
        #Search for when rows begins
        if line == "<rows>\n":
            start_index = index
        
        elif line == "</rows>\n":
            end_index = index
            break
   
    #Add source xml lines to row lines
    row_lines = xml_lines + xml_content[start_index+1:end_index]
    #Function to extract id number from a row string
    def get_id(line):
        start = line.find('id="') + 4
        end = line.find('"', start)
        return int(line[start:end])

    #Sort rows by extracted ID
    sorted_rows = sorted(row_lines, key=get_id)

    #Rebuild full list of xml_content with now new and sorted IDs
    sorted_xml_content = xml_content[:start_index+1] + sorted_rows + xml_content[end_index:]
    with open(xml_path, "w", encoding="utf-8") as write_xml:
        write_xml.writelines(sorted_xml_content)

#updateRegBinfile(reg_bin_test, update_source, param_test_location, witchybnd_test)

#############
# Section 8 #
##############################################################################################################
# #                                           Main function                                                # #
##############################################################################################################

#Paths of files within each DMN folder, this remains constant, as its the form that DMN and Elden Ring mod folders in general take
hks_path = "action\\script\\c0000.hks"
event_path = "action\\eventnameid.txt"
state_path = "action\\statenameid.txt"
anibnd_path = "chr\\c0000.anibnd.dcx" #Any edits on the file being replaced are done by DSAnimStudio by MeowMaritus
sfx_path = "sfx\\sfxbnd_commoneffects_dlc02.ffxbnd.dcx"
behavior_path = "chr\\c0000.behbnd.dcx" #Uses a python script someone else provided to the mod community, BEH injector
regulation_path = "regulation.bin" #Regulation.bin is updated via Smithbox app

#Tools needed for updates

#WitchyBND path, needed for unpacking/repacking folders, used in Sections 4, 5, 6
witchy_bnd_path = "C:\\Desktop\\Mods\\WitchyBND\\WitchyBND.exe"
#Paths to tools used in Section 6
hklib_path = "C:\\Desktop\\Mods\\HKLibCLI.v0.1.2\\net7.0\\HKLib.CLI.exe"
erbeh_injector_path = "C:\\Desktop\\Mods\\ERBEHInjector"

def updateMods(DMN_variants_to_update, hks_path_boolean, event_path_boolean, state_path_boolean, anibnd_path_boolean, sfx_path_boolean, beh_path_boolean, regulation_path_boolean):
    """
    Main function that applies all updates user wants to apply.

    Highly advise throughly checking everything above to ensure it is correctly written so you're not updating wrong things.

    Double check that the previous editions details are not still written in, overwriting previous versions is bad :)
    """

    #Error checks
    if DMN_variants_to_update == None:
        print("Path isn't specified. Add a path to the DMN variants folder for your update.")
        return
    if (hks_path_boolean == None) or (event_path_boolean == None) or (state_path_boolean == None) or (anibnd_path_boolean == None) or (sfx_path_boolean == None) or (beh_path_boolean == None) or (regulation_path_boolean) == None:
        print("Ensure you are stating booleans true/false for each potential update, no accidentals allowed!")
        return
    if (hks_path_boolean == (False, False)) and (event_path_boolean == False) and (state_path_boolean == False) and (anibnd_path_boolean == False) and (sfx_path_boolean == False) and (beh_path_boolean == False) and (regulation_path_boolean) == False:
        print("You have successfully updated nothing, try changing something to True.")
        return
    #Loop through folder with all variants/merges of DMN
    for filename in os.listdir(DMN_variants_to_update):
        print(f"Processing variant: {filename}")
        #Create path to the DMN variants folder
        variant_folder = os.path.join(DMN_variants_to_update, filename)
        #Check if updating c0000.hks
        if hks_path_boolean[0] == True:
            variant_hks_path = os.path.join(variant_folder, hks_path)
            new_moves = os.path.join(hks_update, "newmoves.txt")
            new_functions = os.path.join(hks_update, "newfunctions.txt")
            try:
                updateHKSfile(variant_hks_path, new_moves, new_functions)
            except FileNotFoundError:
                print(f"ERROR: c0000.hks not found in {filename}, skipping HKS update.")
        
        if hks_path_boolean[1] == True:
            variant_hks_path = os.path.join(variant_folder, hks_path)
            try:
                updateSuperFindAttackFunction(super_function, variant_hks_path)
            except FileNotFoundError:
                print(f"ERROR: c0000.hks not found in {filename}, skipping HKS update.")
        
        #Check if updating eventnameid.txt, if true then state_path_boolean ought to be true too (Your call!)
        if event_path_boolean == True:
            variant_event_path = os.path.join(variant_folder, event_path)
            try:
                updateEvent(variant_event_path, STORED_NAMES)
            except FileNotFoundError:
                print(f"ERROR: eventnameid.txt not found in {filename}, skipping event update.")
        #Check if updating statenameid.txt, if true then event_path_boolean ought to be true too (Your call!)
        if state_path_boolean == True:
            variant_state_path = os.path.join(variant_folder, state_path)
            try:
                updateState(variant_state_path, STORED_NAMES)
            except FileNotFoundError:
                print(f"ERROR: statenameid.txt not found in {filename}, skipping state update.")
        
        #Check if updating a66.tae in c0000.anibnd.dcx
        if anibnd_path_boolean == True:
            variant_anibnd_path = os.path.join(variant_folder, anibnd_path)
            try:
                replace_a66_tae(variant_anibnd_path, tae_update, witchy_bnd_path)
            except FileNotFoundError:
                print(f"ERROR: c0000.anibnd.dcx not found in {filename}, skipping anibnd update.")
        
        #Check if updating sfx files
        if sfx_path_boolean == True:
            variant_sfx_path = os.path.join(variant_folder, sfx_path)
            try:
                replace_sfx_effects(variant_sfx_path, sfx_update, witchy_bnd_path)
            except FileNotFoundError:
                print(f"ERROR: sfx file not found in {filename}, skipping sfx update.")
        
        #Check if updating c0000.behbnd.dcx file
        if beh_path_boolean == True:
            variant_beh_path = os.path.join(variant_folder, behavior_path)
            try:
                updateBEHfile(variant_beh_path, witchy_bnd_path, hklib_path, erbeh_injector_path, STORED_IDS, STORED_NAMES)
            
            except FileNotFoundError:
                print(f"ERROR: c0000.behbnd.dcx not found in {filename}, skipping behbnd update.")
        
        #Check if updating regulation.bin file
        if regulation_path_boolean == True:
            variant_reg_path = os.path.join(variant_folder, regulation_path)
            try:
                updateRegBinfile(variant_reg_path, param_update, witchy_bnd_path)
            except FileNotFoundError:
                print(f"ERROR: regulation.bin not found in {filename}, skipping param update(s).")

        #State individual update complete!        
        print(f"Update complete for variant: {filename}")
        #Testing, press Y to continue so can see where script isnt working
        while True:
            user_input = input("Type 'Y' to continue: ").strip().upper()
            if user_input == 'Y':
                break
            else:
                print("Invalid input. Please type 'Y'.")

    #State that all updates are complete!
    print("All updates complete.")
            
#############
# Section 9 #
##############################################################################################################
# #                                           Settings, run function below                                 # #
##############################################################################################################

"""ADJUST THESE SETTINGS FOR HELPER MAIN"""
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

#Prints out helpful functions/formats/lines of text for files needed in updating DMN
#helperMain(startID, title1, title2, amount, currentEventAmount)

"""ADJUST THESE SETTINGS FOR MOD UPDATE"""
#Details needed for some functions below

#Full list of names and IDs, collected for merging mod for release
#These were collected manually by using the helper functions in Section 1, if editing same moves in future these are not required for updates again, only for new moves/animations
#Needed for adding event/states (Autonomous) and BEH injector
STORED_NAMES = ['DMN_SuperSekiro1', 'DMN_SuperSekiro2', 'DMN_SuperSekiro3', 'DMN_SuperSekiro4', 'DMN_SuperSekiro5', 'DMN_SuperSekiro6', 'DMN_SuperSekiro7', 'DMN_SuperSekiro8', 'DMN_SuperSekiro9', 'DMN_SuperSekiro10', 'DMN_SuperSekiro11', 'DMN_SuperSekiro12',
                     'DMN_SuperLoadedFireball1', 'DMN_SuperLoadedFireball2', 'DMN_SuperLoadedFireball3', 'DMN_SuperSakuraDance1', 'DMN_SuperShadowrush1', 'DMN_SuperShadowrush2', 'DMN_SuperPrayingStrikes1', 'DMN_SuperPrayingStrikes2', 'DMN_SuperPrayingStrikes3', 'DMN_SuperSenpouLeapingKicks1', 'DMN_SuperSenpouLeapingKicks2', 'DMN_SuperSenpouLeapingKicks3', 'DMN_SuperFloatingPassage1', 'DMN_SuperFloatingPassage2', 'DMN_SuperFloatingPassage3', 'DMN_SuperFloatingPassage4', 'DMN_SuperFloatingPassage5', 'DMN_SuperFloatingPassage6', 'DMN_SuperLoadedShuriken1', 'DMN_SuperLoadedShuriken2', 'DMN_SuperLoadedShuriken3', 'DMN_SuperWhirlwindSlash1', 'DMN_SuperNightjarSlash1', 'DMN_SuperNightjarSlash2', 'DMN_SuperIchimonji1', 'DMN_SuperIchimonji2', 'DMN_SuperIchimonji3', 'DMN_SuperDragonFlash1', 'DMN_SuperDragonFlash2', 'DMN_SuperAshinaCross1', 'DMN_SuperOneMind1', 'DMN_SuperOneMind2',
                     'DMN_SuperGenichiro1', 'DMN_SuperGenichiro2', 'DMN_SuperGenichiro3', 'DMN_SuperGenichiro4', 'DMN_SuperGenichiro5', 'DMN_SuperGenichiro6', 'DMN_SuperGenichiro7', 'DMN_SuperGenichiro8', 'DMN_SuperGenichiro9', 'DMN_SuperGenichiro10', 'DMN_SuperGenichiro11', 'DMN_SuperGenichiro12', 'DMN_SuperGenichiro13', 'DMN_SuperGenichiro14', 'DMN_SuperGenichiro15', 'DMN_SuperGenichiro16', 'DMN_SuperGenichiro17', 'DMN_SuperGenichiro18', 'DMN_SuperGenichiro19', 'DMN_SuperGenichiro20', 'DMN_SuperGenichiro21', 'DMN_SuperGenichiro22',
                     'DMN_SuperGreatShinobiOwl1', 'DMN_SuperGreatShinobiOwl2', 'DMN_SuperGreatShinobiOwl3', 'DMN_SuperGreatShinobiOwl4', 'DMN_SuperGreatShinobiOwl5', 'DMN_SuperGreatShinobiOwl6', 'DMN_SuperGreatShinobiOwl7', 'DMN_SuperGreatShinobiOwl8', 'DMN_SuperGreatShinobiOwl9', 'DMN_SuperGreatShinobiOwl10', 'DMN_SuperGreatShinobiOwl11', 'DMN_SuperGreatShinobiOwl12', 'DMN_SuperGreatShinobiOwl13', 'DMN_SuperGreatShinobiOwl14', 'DMN_SuperGreatShinobiOwl15', 'DMN_SuperGreatShinobiOwl16', 'DMN_SuperGreatShinobiOwl17', 'DMN_SuperGreatShinobiOwl18', 'DMN_SuperGreatShinobiOwl19',
                     'DMN_SuperLoneShadow1', 'DMN_SuperLoneShadow2', 'DMN_SuperLoneShadow3', 'DMN_SuperLoneShadow4', 'DMN_SuperLoneShadow5', 'DMN_SuperLoneShadow6', 'DMN_SuperLoneShadow7', 'DMN_SuperLoneShadow8', 'DMN_SuperLoneShadow9', 'DMN_SuperLoneShadow10', 'DMN_SuperLoneShadow11',
                     'DMN_SuperIsshin1', 'DMN_SuperIsshin2', 'DMN_SuperIsshin3', 'DMN_SuperIsshin4', 'DMN_SuperIsshin5', 'DMN_SuperIsshin6', 'DMN_SuperIsshin7', 'DMN_SuperIsshin8', 'DMN_SuperIsshin9', 'DMN_SuperIsshin10', 'DMN_SuperIsshin11', 'DMN_SuperIsshin12', 'DMN_SuperIsshin13', 'DMN_SuperIsshin14', 'DMN_SuperIsshin15', 'DMN_SuperIsshin16', 'DMN_SuperIsshin17', 'DMN_SuperIsshin18', 'DMN_SuperIsshin19', 'DMN_SuperIsshin20', 'DMN_SuperIsshin21', 'DMN_SuperIsshin22', 'DMN_SuperIsshin23', 'DMN_SuperIsshin24', 'DMN_SuperIsshin25', 'DMN_SuperIsshin26', 'DMN_SuperIsshin27', 'DMN_SuperIsshin28', 'DMN_SuperIsshin29', 'DMN_SuperIsshin30', 'DMN_SuperIsshin31'
                    ]


#Needed for BEH injector
STORED_IDS = ['911435', '911436', '911437', '911438', '911439', '911440', '911441', '911442', '911443', '911444', '911445', '911446',
                   '911461', '911462', '911463', '911563', '911561', '911562', '911551', '911552', '911553', '911541', '911542', '911543', '911531', '911532', '911533', '911534', '911535', '911536', '911458', '911459', '911460', '911470', '911480', '911481', '911491', '911492', '911493', '911501', '911502', '911511', '911521', '911522',
                   '911601', '911602', '911603', '911604', '911605', '911606', '911607', '911608', '911609', '911610', '911611', '911612', '911613', '911614', '911615', '911616', '911617', '911618', '911619', '911620', '911621', '911622',
                   '911801', '911802', '911803', '911804', '911805', '911806', '911807', '911808', '911809', '911810', '911811', '911812', '911813', '911814', '911815', '911816', '911817', '911818', '911819',
                   '911901', '911902', '911903', '911904', '911905', '911906', '911907', '911908', '911909', '911910', '911911',
                   '912001', '912002', '912003', '912004', '912005', '912006', '912007', '912008', '912009', '912010', '912011', '912012', '912013', '912014', '912015', '912016', '912017', '912018', '912019', '912020', '912021', '912022', '912023', '912024', '912025', '912026', '912027', '912028', '912029', '912030', '912031'
                  ]

super_function = """function Combo_FindAttackInComboTable(r1, r2, b1, b2)
	local WieldingTable = Combo_GetWieldingTable()
	if WieldingTable == nil then
		return nil
	end

	local IsNormal = FALSE
	local ComboTable = nil
	if r1 == RIGHT_DASH1 or r2 == RIGHT_DASH2 or b1 == BOTH_DASH1 or b2 == BOTH_DASH2 then
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_DASH_COMBO) == "table" and 0 < #WieldingTable.SUPER_DASH_COMBO then
			ComboTable = WieldingTable.SUPER_DASH_COMBO
		else
			ComboTable = WieldingTable.DASH_COMBO
		end
	elseif r1 == RIGHT_ROLL or b1 == BOTH_ROLL then
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_ROLL_COMBO) == "table" and 0 < #WieldingTable.SUPER_ROLL_COMBO then
			ComboTable = WieldingTable.SUPER_ROLL_COMBO
		else
			ComboTable = WieldingTable.ROLL_COMBO
		end
	elseif r1 == RIGHT_STEP or b1 == BOTH_STEP then
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_BACKSTEP_COMBO) == "table" and 0 < #WieldingTable.SUPER_BACKSTEP_COMBO then
			ComboTable = WieldingTable.SUPER_BACKSTEP_COMBO
		else
			ComboTable = WieldingTable.BACKSTEP_COMBO
		end
	elseif r1 == RIGHT_STEALTH or b1 == BOTH_STEALTH then
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_STEALTH_COMBO) == "table" and 0 < #WieldingTable.SUPER_STEALTH_COMBO then
			ComboTable = WieldingTable.SUPER_STEALTH_COMBO
		else
			ComboTable = WieldingTable.STEALTH_COMBO
		end
	elseif Combo_IsGuardStance() == TRUE then
		Combo_SetGuardStance(FALSE)
		Action_SetSpecialRequest(TRUE)
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_GUARD_STANCE) == "table" and 0 < #WieldingTable.SUPER_GUARD_STANCE then
			ComboTable = WieldingTable.SUPER_GUARD_STANCE
		else
			ComboTable = WieldingTable.GUARD_STANCE
		end
		if GV_Combo.Custom == GC_MODES.MOVESETS_DEFAULT or ComboTable == nil or #ComboTable == 0 then
			ComboTable = GC_COMBO.GUARD_STANCE1
		end
	elseif Action_IsGuardCounterPossible() == TRUE then
		Action_EndGuardCounterStatus()
		ComboTable = WieldingTable.GUARD_COUNTER
		if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_GUARD_COUNTER) == "table" and 0 < #WieldingTable.SUPER_GUARD_COUNTER then
			ComboTable = WieldingTable.SUPER_GUARD_COUNTER
		else
			ComboTable = WieldingTable.GUARD_COUNTER
		end
		if ComboTable == nil or #ComboTable == 0 then
			if c_Style == HAND_RIGHT_BOTH or c_Style == HAND_LEFT_BOTH then
				ComboTable = GC_COMBO.GUARD_COUNTER2
			else
				ComboTable = GC_COMBO.GUARD_COUNTER1
			end
		end
	else
		IsNormal = TRUE
		if 0 < #Combo_GetComboTable() then
			ComboTable = Combo_GetComboTable()
		else
			if Accumulate_IsReady() == TRUE and type(WieldingTable.SUPER_NORMAL_COMBO) == "table" and 0 < #WieldingTable.SUPER_NORMAL_COMBO then
				ComboTable = WieldingTable.SUPER_NORMAL_COMBO
			else
				ComboTable = WieldingTable.NORMAL_COMBO
			end
		end
	end

	if ComboTable == nil or #ComboTable == 0 then
		ComboTable = {}
	else
		if Combo_GetComboTable() ~= ComboTable then
			Combo_ShiftComboActions()
			Combo_SwitchComboTable(ComboTable)
		end
	end

	local AttackIndex = 0
	local CurrentActions = Combo_GetComboActions()
	local NextAttack = Combo_FindNextAttack(ComboTable)
	if NextAttack == nil and IsNormal == FALSE then
		Combo_ShiftComboActions()
		NextAttack = Combo_FindNextAttack(ComboTable)
	end

	if NextAttack == nil and WieldingTable.NORMAL_COMBO ~= nil and (1 < #CurrentActions or Action_IsGuardCounterPossible() == TRUE) then
		Combo_ShiftComboActions()
		Combo_SwitchComboTable(WieldingTable.NORMAL_COMBO)
		NextAttack = Combo_FindNextAttack(WieldingTable.NORMAL_COMBO)
	end

	return NextAttack
end"""

#Path of DMN variants folder, 
#These will be manually added as mod author adds more merges
#Path to folder is to be changed when making another mod version, and after an update the updated files should be removed from 'To be added'
DMN_variants_to_update = "C:\\Desktop\\Mods\\DeflectMeNot\\DMN V3 EXP37 Update Resources\\DMN_V3_EXP37.2\\To be added"

#Update locations

#This folder changes for each update, e.g. DMN_V3_EXP37.2\\Updated files, 37.2 is subject to change
updated_files_folder = "C:\\Desktop\\Mods\\DeflectMeNot\\DMN V3 EXP37 Update Resources\\DMN_V3_EXP37.2\\Updated files"
#These remain constant, depend on updated_files_folder location
hks_update = os.path.join(updated_files_folder, "hks update")
tae_update = os.path.join(updated_files_folder, "anibnd update\\a66.tae")
sfx_update = os.path.join(updated_files_folder, "sfx update\\effects-to-be-added")
param_update = os.path.join(updated_files_folder, "param-update")

#Magic button, only run if certain...

#updateMods(DMN_variants_to_update, (False, True), False, False, False, False, False, False)
updateMods(DMN_variants_to_update, (True, True), True, True, True, True, True, True)