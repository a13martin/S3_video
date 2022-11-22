import subprocess


def convert_all_formats(vid):
    name = vid.replace(".mp4", "")
    vp8 = name + "vp8.webm "
    vp9 = name + "vp9.webm "
    h265 = name + "h265.mp4 "
    av1 = name + "av1.mp4 "
    subprocess.call("ffmpeg -i " + vid + " -c:v libvpx -b:v 1M -c:a libvorbis " + vp8)
    print("vp8 done")
    subprocess.call("ffmpeg -i " + vid + " -c:v libvpx-vp9 -crf 30 -b:v 0 " + vp9)
    print("vp9 done")
    subprocess.call("ffmpeg -i " + vid + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k " + h265)
    print("h256 done")
    subprocess.call(f"ffmpeg -i {vid} -c:v libaom-av1 -minrate 500k -b:v 2000k -maxrate 2500k {av1}")
    print("avi done")
    return vp8, vp9, h265, av1


class VideoUtils:

    def __init__(self, vid):
        self.vid = vid

    def stack_videos(self):
        vp8, vp9, h265, av1 = convert_all_formats(self.vid)

        subprocess.call(
            f'ffmpeg -i {vp8} -i {vp9} -i {h265} -i {av1} -filter_complex hstack=inputs=4 output{self.vid}.mp4')


if __name__ == '__main__':
    video_low = "bbb_160x120.mp4"
    video360 = "bbb_360x240.mp4"
    video480 = "bbb_480p.mp4"
    videohd = "bbb_720p.mp4"
    vv = VideoUtils(video_low)
    vv2 = VideoUtils(video360)
    vv3 = VideoUtils(video480)
    vv4 = VideoUtils(videohd)

    vv.stack_videos()
    vv2.stack_videos()
    vv3.stack_videos()
    vv4.stack_videos()  # Generating the concatenated videos for all the resolutions
