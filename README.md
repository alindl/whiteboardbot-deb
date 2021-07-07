This is a fork of the [original project](https://git.sbg.ac.at/center-for-hci/whiteboardbot/whiteboardbot-deb) from the Center of HCI at the University of Salzburg.

# Whiteboardbot

The Whiteboard capture, enhancement and sharing tool

WhiteboardBot implements a system that uses a Raspberry Pi 3/4, or similar
devices, to plug in one or a set of cameras that would be able to capture
a white- or blackboard. This capture is triggered by a BLE remote.
After taking the picture, the files can automatically be sent to Slack
(to a specific channel or user), to one or several email addresses or
to a arbitrary mix of those.

There is also an optional enhancement feature for those pictures, such as
whiteboard enhancement, lens distortion fix and cropping. It also has an
optional feedback system through audio and visuals.

All those settings can be set, cameras, buttons and emails can be
dynamically added and removed. Buttons can be configured, so that pressing a
specific button will result in sharing through different channels.
This is done through a configuration menu, which is a website that is locally
reachable through whiteboardbot.local.
