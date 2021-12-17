#!/usr/bin/python

from subprocess import Popen, PIPE

files = ["twitter_glove", "wikipedia_glove"]
attributes = [("countries_africa", "countries_europe")]
# attributes = [("names_male", "names_female"), ("gender_m",
#                                                "gender_f"), ("names_africa", "names_europe")]
targets = [("art", "science"), ("career", "family"), ("insects", "flowers"),
           ("pleasant", "unpleasant"), ("positive-words", "negative-words"),
           ("computers_and_maths", "medical")]

# attributes = [("names_male", "names_female"), ("gender_m",
#                                                "gender_f")]
# targets = [("computers_and_maths", "medical")]

for file in files:
    for attrs in attributes:
        for target in targets:
            process = Popen(["./weatTest.py", file, attrs[0], attrs[1], target[0],
                            target[1]], stdout=PIPE)
            (output, err) = process.communicate()
            # print(output)
            dupOutput = str(output).split("Effect size: ")[
                1].split("\n\n")[0]
            print("File: %s, targets: (%s, %s), attributes: (%s, %s), Effect size: %s." % (
                file, target[0], target[1], attrs[0], attrs[1], str(dupOutput.strip()[:-5]) if dupOutput != None else "0.0"))
            exit_code = process.wait()
