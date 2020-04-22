/*
 * Copyright (c) 2015 Terry Cain <terrys-home.co.uk>
 */

/*
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the Free
 * Software Foundation; either version 2 of the License, or (at your option)
 * any later version.
 */

#ifndef __HID_RAZER_CONTROLLER_H
#define __HID_RAZER_CONTROLLER_H

#define USB_DEVICE_ID_RAZER_WOLVERINE_TOURNAMENT_EDITION 0x0A15

#define USB_INTERFACE_PROTOCOL_CONTROLLER 208

struct razer_controller_device {
    struct usb_device *usb_dev;
    struct input_dev *input;
    struct mutex lock;
    unsigned char usb_interface_protocol;

    unsigned short usb_vid;
    unsigned short usb_pid;

    char serial[23];
    // 3 Bytes, first byte is whether fw version is collected, 2nd byte is major version, 3rd is minor, should be printed out in hex form as are bcd
    unsigned char firmware_version[3];
};

/*
 * USB INTERRUPT
 *
 * */

#endif
