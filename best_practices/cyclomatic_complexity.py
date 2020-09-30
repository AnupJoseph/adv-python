import sys

def main():
	if len(sys.argv) > 1:
		filepath = sys.argv[1]
	else:
		print("Please provide afile path")
		exit(1)
	if filepath:
		with open(filepath) as fp:
			for line in fp:
				if line != "\n":
					print(line,end = "")

main()