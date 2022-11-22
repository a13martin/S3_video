import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import subprocess


# FUNCTIONS FOR COMMANDS/FFMPEG
def ex1():
    """
    This function does the same as in VideoUtils.py but integrated in the interface,
    once the videos have been collected
    """
    showinfo(message="Generating videos... ")
    subprocess.call(
        f'ffmpeg -i bbb_480pav1.mp4 -i bbb_480ph265.mp4 -i bbb_480pvp8.webm -i bbb_480pvp9.webm '
        f'-filter_complex hstack=inputs=4 output_480p.mp4')


def instructions():
    ins = tk.Toplevel(root)
    ins.geometry("750x250")
    ins.title("Child Window")
    txt = tk.Label(ins, text="Press a button to convert any video to the corresponding format. ").pack()
    txt = tk.Label(ins, text="Once you click, the program will ask you to input a video from your computer.").pack()
    txt = tk.Label(ins, text="The output will be in the folder in which the script is on, called output.format").pack()


def select_file():
    filetypes = (
        ('Video files', '*.*'),
        ('All files', '*.*')
    )
    # global video
    v = (str(fd.askopenfilename(
        title='Select the video for conversion',
        initialdir='/',
        filetypes=filetypes)))
    if v == '':
        showinfo(
            title='Woops',
            message='Nothing was selected'
        )
    else:
        showinfo(
            title='Video selected',
            message="Video selected: " + v
        )
    return v


def to_vp8():
    vv = select_file()
    if vv == '':
        showinfo(title='ERROR!',
                 message="No video has been selected")
    else:
        subprocess.call(f"ffmpeg -i {vv} -c:v libvpx -b:v 1M -c:a libvorbis outInVP8.webm")
        showinfo(title='Processing...',
                 message=f'Converting {vv} to VP9, it could take some time...')


def to_vp9():
    vv = select_file()
    if vv == '':
        showinfo(title='ERROR!',
                 message="No video has been selected")
    else:
        subprocess.call(f"ffmpeg -i {vv} -c:v libvpx-vp9 -crf 30 -b:v 0 outInVP9.webm")
        showinfo(title='Processing...',
                 message=f'Converting {vv} to VP9, it could take some time...')


def to_h265():
    vv = select_file()
    if vv == '':
        showinfo(title='ERROR!',
                 message="No video has been selected")
    else:
        subprocess.call(f"ffmpeg -i {vv} -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k outInH265.mp4")
        showinfo(title='Processing...',
                 message=f'Converting {vv} to H265, it could take some time...')


def to_av1():
    vv = select_file()
    if vv == '':
        showinfo(title='ERROR!',
                 message="No video has been selected")
    else:
        subprocess.call(f"ffmpeg -i {vv} -c:v libaom-av1 -minrate 500k -b:v 2000k -maxrate 2500k outInAV1.mp4")
        showinfo(title='Processing...',
                 message=f'Converting {vv} to AV1, it could take some time...')


# CREATING INTERFACE
root = tk.Tk()
root.title("Àlex' Video Converter")
root.geometry("500x550")  # Creating a 500x400 window
root['bg'] = 'blue'
label = tk.Label(root, text="VIDEO CONVERTER")
label.pack(anchor='center')
label.config(fg="red",  # Foreground
             bg="blue",  # Background
             font=("Comic Sans MS", 24))

# CREATING BUTTONS
vp8 = tk.Button(root, text='to VP8', command=to_vp8, width=10, height=5, bg='red')
vp9 = tk.Button(root, text='to VP9', command=to_vp9, width=10, height=5, bg='red')
h265 = tk.Button(root, text='to H265', command=to_h265, width=10, height=5, bg='red')
av1 = tk.Button(root, text='to AV1', command=to_av1, width=10, height=5, bg='red')
concat = tk.Button(root, text='Exercise 1', command=ex1, bg='red')
exit = tk.Button(root, text='EXIT', command=root.quit, bg='red')

vp8.pack(anchor='center')
vp9.pack()
h265.pack()
av1.pack()
concat.pack()
exit.pack()

# CREATING THE MENU BAR
menubar = tk.Menu(root, tearoff=0)
root.config(menu=menubar)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=filemenu)
filemenu.add_command(label="Instructions", command=instructions)
filemenu.add_command(label="Exit", command=root.quit)

root.mainloop()
