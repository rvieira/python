import sys

count_args = len(sys.argv)
print("Number of arguments:", count_args)
print("Arguments:")
for i in range(0, count_args):
	print("- "+sys.argv[i])