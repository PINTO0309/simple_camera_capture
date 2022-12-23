#! /usr/bin/env python

import os
import re
import sys
import cv2
import copy
import datetime
import argparse
import subprocess
__path__ = (os.path.dirname(__file__), )
with open(os.path.join(__path__[0], '__init__.py')) as f:
    init_text = f.read()
    __version__ = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        param['status'] = 'capture'
    elif event == cv2.EVENT_RBUTTONDOWN:
        param['status'] = 'exit'
    else:
        param['status'] = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-cn", "--camera_no", type=int, default=0)
    parser.add_argument("-cw", "--camera_cap_width", type=int, default=640)
    parser.add_argument("-ch", "--camera_cap_height", type=int, default=480)
    parser.add_argument("-mi", "--movie_or_image_path", type=str, default=None)
    parser.add_argument("-dvr", "--disable_video_recording", action="store_true")
    parser.add_argument(
        "-dcr",
        "--display_camera_resolutions",
        action="store_true",
        help=\
            "Displays a list of resolutions supported by the camera. " +
            "Cannot be used in conjunction with other options other than -cn. " +
            "Linux only option. " +
            "sudo apt update && sudo apt install v4l-utils",
    )
    parser.add_argument(
        '-V',
        '--version',
        action='store_true',
        help='Show version and exit.'
    )
    args = parser.parse_args()
    camera_no: int = args.camera_no
    cap_width: int = args.camera_cap_width
    cap_height: int = args.camera_cap_height
    movie_or_image_path: str = args.movie_or_image_path
    disable_video_recording: bool = args.disable_video_recording
    display_camera_resolutions: bool = args.display_camera_resolutions
    version: bool = args.version
    # Print version
    if version:
        print(__version__)
        sys.exit(0)
    if display_camera_resolutions:
        try:
            result = subprocess.check_output(
                [
                    'v4l2-ctl',
                    '-d',
                    f'/dev/video{camera_no}',
                    '--list-formats-ext',
                ],
                stderr=subprocess.PIPE
            ).decode('utf-8')
            print(result)
            sys.exit(0)
        except Exception as e:
            import traceback
            traceback.print_exc()
            sys.exit(0)
    ext: str = None
    window_title: str = None
    if movie_or_image_path is None:
        cap = cv2.VideoCapture(camera_no)
        window_title = "Video"
    else:
        cap = cv2.VideoCapture(movie_or_image_path)
        ext = os.path.splitext(movie_or_image_path)[1][1:].lower()
        if ext in ['mp4','avi','wmv','mov']:
            window_title = "Video"
        elif ext in ['jpg','png','bmp','dib','pbm','pgm','ppm']:
            window_title = "Image"
        else:
            raise Exception(f'{os.path.basename(movie_or_image_path)} is an unsupported file format.')
    cv2.namedWindow(window_title, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
    cv2.resizeWindow(window_title, cap_width, cap_height)
    param = {'status': None}
    cv2.setMouseCallback(window_title, onMouse, param)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap_height)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
    key_input = cv2.waitKey(100)
    cap_fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    movie_now = datetime.datetime.now()
    save_folder_path = f"{movie_now.strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(save_folder_path, exist_ok=True)
    video_writer = None
    if not disable_video_recording:
        video_writer = cv2.VideoWriter(
            filename=f"{save_folder_path}/output_movie_{save_folder_path}.mp4",
            fourcc=fourcc,
            fps=cap_fps,
            frameSize=(cap_width, cap_height),
        )
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        if not disable_video_recording:
            video_writer.write(frame)
        cv2.imshow(window_title, frame)
        key_input = cv2.waitKey(1) & 0xFF \
            if ext is None else cv2.waitKey(0) & 0xFF
        if key_input == ord('q') or key_input == 27 or param['status'] is not None and param['status'] == 'exit':
            break
        if key_input == ord('c') or param['status'] is not None and param['status'] == 'capture':
            image_now = datetime.datetime.now()
            cv2.imwrite(f"{save_folder_path}/output_image_{image_now.strftime('%Y%m%d_%H%M%S')}.png", frame)
            debug_frame = copy.deepcopy(frame)
            cv2.rectangle(
                debug_frame,
                (int(5),int(5)),
                (int(cap_width-5),int(cap_height-5)),
                (0,0,255),
                5,
                cv2.LINE_AA,
            )
            cv2.imshow(window_title, debug_frame)
            key_input = cv2.waitKey(1)
    if video_writer:
        video_writer.release()
    if cap:
        cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
