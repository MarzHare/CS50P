import sys
import random
from pyfiglet import Figlet


figlet = Figlet()


def main():
    # Expect 0 or 2 command-line argumments
    # If zero -- output text in random font
    if len(sys.argv) == 1:
        # Desired font
        font = random.choice(figlet.getFonts())
        rfont = figlet_font(font)
    # If two -- output text in specific font (arg1 will be -f or --font, and arg2 will be name of font)
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            # Desired font
            font = sys.argv[2]
            sfont = figlet_font(font)
        else:
            sys.exit("Invalid usage")
    # If neither of these happen, sys.exit + error message
    else:
        sys.exit("Invalid usage")

    # Prompt user for string
    fig = input("Input: ")
    # Output text in desired font
    print(f"Output: {figlet.renderText(fig)}")

# Maybe I need a font function?
def figlet_font(font):
    figgied = figlet.setFont(font=f'{font}')
    return figgied

main()