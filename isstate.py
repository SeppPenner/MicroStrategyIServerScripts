import commands

#Script to show the MicroStrategy Intelligence Server's status
#Works with Python Version 2.6.8
def isstate():
	"isstate"
	val = str(commands.getstatusoutput('/MicroStrategy/bin/mstrctl -s IntelligenceServer gs |grep -i state'))
	print formatOutput(val)
	return
	
def formatOutput(input):
	"formatOutput"
	output = ""
	for i, c in enumerate(input):
		if c == ">":
			output = input[i+1:]
			for j, d in enumerate(output):
				if d == "<":
					output = output[:-j]
					output = output.rpartition('<')[0]
					return output
	return output	

#Programm
isstate()