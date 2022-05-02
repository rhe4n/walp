from walp.utils import storage
import subprocess

import os
import xcffib
import xcffib.xproto
import cairocffi
import cairocffi.pixbuf


def set_monitor_background_pairs(pairs):
    command = ["feh", "--no-fehbg"]

    for i in list(pairs):
        imgPath = storage.build_path_for_image(pairs[i])
        command.append("--bg-fill")
        command.append(imgPath)

    result = subprocess.run(command, stdout=subprocess.DEVNULL).returncode
    if result == 0:
        return 0
    else:
        print(result)
        return 1


# def set_monitor_background(monitor_number, stashed_image_name):
#     conn = xcffib.Connection(display=os.environ.get("DISPLAY"))
#     screens = conn.get_setup().roots
#     path_to_image = storage.build_path_for_image(stashed_image_name)
#
#     with open(path_to_image, 'rb') as fd:
#         image, _ = cairocffi.pixbuf.decode_to_image_surface(fd.read())
#
#     print(monitor_number)
#     print(len(screens))
#     screen = screens[0]
#     pixmap = conn.generate_id()
#     conn.core.CreatePixmap(
#         screen.root_depth,
#         pixmap,
#         screen.root,
#         screen.width_in_pixels,
#         screen.height_in_pixels,
#     )
#     for depth in screen.allowed_depths:
#         for visual in depth.visuals:
#             if visual.visual_id == screen.root_visual:
#                 root_visual = visual
#                 break
#
#     surface = cairocffi.xcb.XCBSurface(
#         conn, pixmap, root_visual,
#         screen.width_in_pixels, screen.height_in_pixels,
#     )
#
#     with cairocffi.Context(surface) as context:
#         context.set_source_surface(image)
#         context.paint()
#
#     conn.core.ChangeProperty(
#         xcffib.xproto.PropMode.Replace,
#         screen.root,
#         conn.core.InternAtom(False, 13, '_XROOTPMAP_ID').reply().atom,
#         xcffib.xproto.Atom.PIXMAP,
#         32, 1, [pixmap]
#     )
#     conn.core.ChangeProperty(
#         xcffib.xproto.PropMode.Replace,
#         screen.root,
#         conn.core.InternAtom(False, 16, 'ESETROOT_PMAP_ID').reply().atom,
#         xcffib.xproto.Atom.PIXMAP,
#         32, 1, [pixmap]
#     )
#     conn.core.ChangeWindowAttributes(
#         screen.root, xcffib.xproto.CW.BackPixmap, [pixmap]
#     )
#     conn.core.ClearArea(
#         0, screen.root,
#         0, 0,           # x and y position
#         screen.width_in_pixels, screen.height_in_pixels
#     )
#     conn.core.SetCloseDownMode(xcffib.xproto.CloseDown.RetainPermanent)
#     conn.disconnect()
