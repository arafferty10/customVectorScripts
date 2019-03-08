#Aidan Rafferty
#First attempt at a Vector script
#Keeping it basic to start
#03/08/2019

import anki_vector

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Greeting overlord...")
        robot.say_text("Hello Master Aidan")

if __name__ == "__main__":
    main()
