import os
import subprocess


def resize(inv, outv, s):
    if os.path.exists(outv):
        os.remove(outv)
    subprocess.call('ffmpeg -i ' + inv + ' -vf scale=' + s + " " + outv)


if __name__ == '__main__':
    print("Type 1 for 720p \nType 2 for 480p \nType 3 for 360x240 \nType 4 for 160x120 \nType 0 to exit")
    option = int(input("Select resizing format: "))
    print("Selecting option: " + str(option))
    video = "bbb.mp4"

    match option:
        case 1:
            resize(video, "bbb_720p.mp4", "1280:720")
        case 2:
            resize(video, "bbb_480p.mp4", "768:480")
        case 3:
            resize(video, "bbb_360x240.mp4", "320:240")
        case 4:
            resize(video, "bbb_160x120.mp4", "160:120")
        case 0:
            print("Exiting...")
        case other:
            print("Error: Incorrect option")
