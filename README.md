Installation steps:
1. Install Python.
2. In a Windows command prompt (type "cmd" in the Windows search bar), paste "py -m pip install requests" (without quotes) and hit enter. It'll download a package used for HTTP requests.
2. Download the files in this repository (e.g. by clicking the top link under "Releases" to the right and then clicking "Source code (zip)"). If you want to download via git clone, clone it after step 4 (in the folder you create).
3. Go to your Last Epoch filter folder. You can go to the filters in-game, click the button to add a new filter, and click "Open Filter Folder" to get here.
4. Make a new folder in the filter folder, named whatever you want (probably something like "Party Filter Generator").
5. Place the repository files in the folder (not in a subdirectory).

To make your filter:
1. Log into pastebin (check discord channel pin for username/password)
2. Press the green +PASTE button at the top to make a new pastebin
3. Paste your filter into the giant text box
4. Select Paste Exposure: Unlisted
5. Type some sort of paste name in
6. Hit Create New Paste
7. Tell me what your paste name or paste URL is
PLEASE NOTE: I must manually publish a new version of the script (and other people must manually download it) if you're being added for the first time. After the first time, any updates you make to the pastebin will automatically be applied whenever someone runs the script.

To set up the filter:
1. [Optional] In-game, you can create a filter called "p_start" which will add any custom rules you want *at the start* of the generated filter. You can do this at any time, just re-run the script afterward.
2. In-game ensure you have a "p_end" filter which should, at a baseline, hide all normal/magic/rare/exalted items and idols. This will be added to the end of the group's filter. You can add additional rules to this if you'd like (for example, showing certain affixes). There is a basic p_end filter in a pin on the discord channel if you want one.
3. In the subdirectory you created for this script, double-click on build_filter.py.
4. In-game, the filter list should now include a filter named "pf_[names]". This is the aggregate filter for your party, select it and everything should be good. If someone is missing, let me know. Note that it will download separate "pp_[name]" filters for each party member; you can ignore these unless I ask you to help me debug.

Warnings / how to use:
1. If you want to update your part of the filter, edit your pastebin with the new filter text, **DESELECT THE FILTER IN-GAME**, run build_filter.py, reselect the filter, and notify people that the filter has been updated.
2. If you want to update the filter because someone's part was updated, **DESELECT THE FILTER IN-GAME FIRST**, run build_filter.py, and then reselect the filter in-game.
3. Do NOT attempt to change the pf_[names] filter directly. You can change p_start and p_end in-game if you want to in order to add specific rules (these won't get overwritten). If you want your changes to appear on your party members' filters, you must update your pastebin and tell them to run the script.


