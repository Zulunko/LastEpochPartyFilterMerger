Installation steps:
1. Install Python.
2. Download the files in this repository (e.g. via zip download). If you want to download via git clone, clone it after step 4 (in the folder you create).
3. Go to your Last Epoch filter folder. You can go to the filters in-game, click the button to add a new filter, and click "Open Filter Folder" to get here.
4. Make a new folder in the filter folder, named whatever you want (probably something like "Party Filter Generator").
5. Place the repository files in the new folder.

To set up the filter:
1. [Optional] In-game, you can create a filter called "p_start" which will add any custom rules you want *at the start* of the generated filter.
2. In-game, ensure any filters for any players you will be playing with are added with the name "pp_[name]". E.g. Z's filter should be named "pp_Z".
3. In-game ensure you have a "p_end" filter which should, at a baseline, hide all normal/magic/rare/exalted items. You can add additional rules to this if you'd like.
4. In the subdirectory you created for this script, double-click on build_filter.py.
5. In-game, the filter list should now include a filter named "pf_[names]". This is the aggregate filter for your party, select it and everything should be good.

Warnings / how to use:
1. If you want to update your part of the filter, update your pp_[name] on Last Epoch Tools, download the filter for yourself, run build_filter.py, and notify people that the filter has been updated.
2. If you want to update the filter because someone's part was updated, first update any pp_[name] filters that need to be updated and then run build_filter.py. You may need to deselect / reselect the filter to make the game recognize the new version (I'm not sure about this).
3. Do NOT attempt to change the pf_[names] filter directly. You can change p_start and p_end in-game if you want to without using Last Epoch Tools, but any time you want to update your pp_[name] it's best to do it on Last Epoch Tools so other people can also get your updated filter.

TODO:
If anyone feels motivated to figure out how, it'd be much better to automatically download all pp_[name] filters from Last Epoch Tools rather than requiring people to manage those files themselves. I'm not sure how to do this; Last Epoch Tools has no public API as far as I know.
