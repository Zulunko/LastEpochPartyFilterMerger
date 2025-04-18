# Builds a party-wide filter from individual filters in Last Epoch.
# Final filter will be of the order (filter names in quotes):
# [filter_prefix]
# "p_start"
# In a random order: any filter matching "pp_*"
# "p_end"
# [filter_suffix]
# The filter will be named "pf_" with all names appended in an order (e.g. pf_ZRevyaFluoRizRaz)

import os
import random


# takes a filename as infilename and an open file as outfile,
# appends the data from the file infilename to outfile. Always adds a newline.
def copy_all_file_contents(infilename, outfile):
    with open(infilename, "r") as infile:
        for line in infile:
            outfile.write(line)
        outfile.write("\n")


# takes a filename as infilename and an open file as outfile,
# appends the data from the file infilename to outfile. Always adds a newline.
# Only copies lines after a line that contains <rules> and before </rules>.
def copy_filter_rules(infilename, outfile):
    with open(infilename, "r") as infile:
        before = True
        for line in infile:
            if before:
                if "<rules>" in line: ## skipping until the line after <rules>
                    before = False
                continue
            else:
                if "</rules>" in line:
                    break
                outfile.write(line)
        outfile.write("\n")

filter_name = "../pf_"
with open("tmp.xml", "w") as tmpfilter:
    copy_all_file_contents("filter_prefix", tmpfilter)
    # Filter is listed in reverse for some reason...
    candidate_files = os.listdir("../")
        
    if "p_end.xml" in candidate_files:
        copy_filter_rules("../p_end.xml", tmpfilter)

    pp_files = []
    for file in candidate_files:
        if file.startswith("pp_"):
            pp_name = (file.split("_", 1)[1]).split(".xml")[0]
            filter_name += pp_name
            pp_files.append(pp_name)
    random.shuffle(pp_files)
    for pp_name in pp_files:
        copy_filter_rules("../pp_"+pp_name+".xml", tmpfilter)
    
    if "p_start.xml" in candidate_files:
        copy_filter_rules("../p_start.xml", tmpfilter)
        
    copy_all_file_contents("filter_suffix", tmpfilter)

filter_name += ".xml"
os.replace("tmp.xml", filter_name)
    