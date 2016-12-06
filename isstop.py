import commands
import os

#Script to stop the MicroStrategy Intelligence Server and check the state afterwards
#Works with Python Version 2.6.8
def isstate():
	"isstate"
	val = str(commands.getstatusoutput('/MicroStrategy/bin/mstrctl -s IntelligenceServer gs |grep -i state'))
	while "stopping" in val:
		val = str(commands.getstatusoutput('/MicroStrategy/bin/mstrctl -s IntelligenceServer gs |grep -i state'))
	while "unloading" in val:
		val = str(commands.getstatusoutput('/MicroStrategy/bin/mstrctl -s IntelligenceServer gs |grep -i state'))
	val = str(commands.getstatusoutput('/MicroStrategy/bin/mstrctl -s IntelligenceServer gs |grep -i state'))
	print formatOutput(val)
	return

def isstop():
	"isstop"
	os.system('/MicroStrategy/bin/mstrctl -s IntelligenceServer stop')
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
print 'Stopping MicroStrategy Intelligence Server'
isstop()
isstate()