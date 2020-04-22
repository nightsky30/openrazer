"""
Controller class
"""
import re

from openrazer_daemon.hardware.device_base import RazerDeviceBrightnessSuspend as _RazerDeviceBrightnessSuspend


class RazerWolverineTE(_RazerDeviceBrightnessSuspend):
    """
    Class for the Razer Wolverine Tournament Edition
    """
    EVENT_FILE_REGEX = re.compile(r'.*Razer_Razer_Wolverine_Tournament_Edition_.*-event-joystick')

    USB_VID = 0x1532
    USB_PID = 0x0A15
    HAS_MATRIX = True
    WAVE_DIRS = (1, 2)
    MATRIX_DIMS = [1, 16]
    METHODS = ['get_device_type_accessory',
               'set_static_effect', 'set_spectrum_effect', 'set_wave_effect', 'set_none_effect', 'set_breath_single_effect', 'set_breath_dual_effect', 'set_breath_random_effect',
               'set_custom_effect', 'set_key_row']

    DEVICE_IMAGE = "https://assets.razerzone.com/eeimages/support/products/1271/1271_wolverine_tournament_edition.png"

    # Deprecated - RAZER_URLS be removed in future.
    RAZER_URLS = {
        "top_img": DEVICE_IMAGE
    }
