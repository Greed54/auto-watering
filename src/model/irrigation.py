from hardware.hardware_interface import HardwareInterface
from model.data_models import ApplicationState


class IrrigationController:

    def __init__(self, hardware: HardwareInterface, state: ApplicationState):
        self._hardware = hardware
        self._state = state

    def on_pump(self):
        self._hardware.set_pump(True)
        self._state.pump.is_enabled = True

    def off_pump(self):
        self._hardware.set_pump(False)
        self._state.pump.is_enabled = False

    def open_valve(self, channel_id: int):
        self._hardware.set_valve(channel_id, True)
        self._state.channels[channel_id].is_enabled = True

    def close_valve(self, channel_id: int):
        self._hardware.set_valve(channel_id, False)
        self._state.channels[channel_id].is_enabled = False

    def close_all(self):
        self.off_pump()

        for channel_id in self._state.channels.keys():
            self.close_valve(channel_id)
