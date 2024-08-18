import sys

def main():
    arguments = sys.argv[1:]
    uppercased_arguments = [arg.upper() for arg in arguments]
    
    for arg in uppercased_arguments:
        print(arg)

if __name__ == "__main__":
    main()


# python convert-upper.py abc def