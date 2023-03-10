# simple_camera_capture
Very simple recording tool using only OpenCV. Automatically record the camera capture to mp4, press **`C`** key or left mouse button click to take a still image.

## Environment
- opencv-python==4.1.2.30

## Usage
### 1. Start of Recording
```bash
$ sudo apt update && sudo apt install v4l-utils
$ pip install -U simpcamcap opencv-python==4.1.2.30
$ simpcamcap
```
or
```bash
$ xhost +local: && \
docker run --rm -it \
-v `pwd`:/workdir \
-w /workdir \
-v /tmp/.X11-unix/:/tmp/.X11-unix:rw \
-e DISPLAY=$DISPLAY \
-e QT_X11_NO_MITSHM=1 \
--device /dev/video0:/dev/video0 \
ghcr.io/pinto0309/simple_camera_capture:latest simpcamcap
```
```
usage: simpcamcap
[-h]
[-cn CAMERA_NO]
[-cw CAMERA_CAP_WIDTH]
[-ch CAMERA_CAP_HEIGHT]
[-mi MOVIE_OR_IMAGE_PATH]
[-dvr]
[-dcr]
[-V]

optional arguments:
  -h, --help
    show this help message and exit.
  -cn CAMERA_NO, --camera_no CAMERA_NO
  -cw CAMERA_CAP_WIDTH, --camera_cap_width CAMERA_CAP_WIDTH
  -ch CAMERA_CAP_HEIGHT, --camera_cap_height CAMERA_CAP_HEIGHT
  -mi MOVIE_OR_IMAGE_PATH, --movie_or_image_path MOVIE_OR_IMAGE_PATH
  -dvr, --disable_video_recording
  -dcr, --display_camera_resolutions
    Displays a list of resolutions supported by the camera.
    Cannot be used in conjunction with other options other than -cn.
    Linux only option.
    sudo apt update && sudo apt install v4l-utils
  -V, --version
    Show version and exit.
```
### 2. Saving a still image
Press **`C`** key on the keyboard or left mouse button click.
### 3. End of Recording
Press the **`Q`** key or **`ESC`** key on the keyboard or right mouse button click.
### 4. Sample
![image](https://user-images.githubusercontent.com/33194443/209312941-e826214a-640b-49fc-9fc0-97f0758cab97.png)

https://user-images.githubusercontent.com/33194443/209317321-78aa1f7a-3d1e-4538-982c-83ea37ee5e29.mp4

Use the left click of a Bluetooth mouse as a remote control shutter. Right click ends video recording.

https://user-images.githubusercontent.com/33194443/209420179-91ef77fc-2730-45da-a0a9-1dde6d97a288.mp4

The moment a still image is taken, the outer perimeter glows red.
![image](https://user-images.githubusercontent.com/33194443/209331346-479a0733-6eb1-4f2f-be58-208c623d8682.png)

```
$ simpcamcap -dcr
ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture

	[0]: 'YUYV' (YUYV 4:2:2)
		Size: Discrete 1280x720
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
			Interval: Discrete 0.100s (10.000 fps)
			Interval: Discrete 0.125s (8.000 fps)
			Interval: Discrete 0.167s (6.000 fps)
			Interval: Discrete 0.500s (2.000 fps)
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
			Interval: Discrete 0.100s (10.000 fps)
			Interval: Discrete 0.125s (8.000 fps)
			Interval: Discrete 0.167s (6.000 fps)
			Interval: Discrete 0.500s (2.000 fps)
		Size: Discrete 800x600
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
			Interval: Discrete 0.100s (10.000 fps)
			Interval: Discrete 0.125s (8.000 fps)
			Interval: Discrete 0.167s (6.000 fps)
			Interval: Discrete 0.500s (2.000 fps)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
			Interval: Discrete 0.100s (10.000 fps)
   :
   :
```
