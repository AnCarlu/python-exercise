import sys

length_of_argv = len(sys.argv)
script_name = sys.argv[0]
other_arguments = sys.argv[1:]

print(f"Length of argv list     : {length_of_argv}")
print(f"Name of the script      : {script_name} ")
print(f"Arguments of the script : {other_arguments}")