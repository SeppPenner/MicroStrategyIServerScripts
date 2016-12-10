import commands

#Script to show the MicroStrategy Intelligence Server's version
#Works with Python Version 2.6.8
path = "/bi/MSTR/bin/mstrctl"

def isversion():
	"isversion"
	val = str(commands.getstatusoutput(path + ' -s IntelligenceServer gs |grep -i product_version'))
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
isversion()