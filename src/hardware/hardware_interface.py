from abc import ABC, abstractmethod


class HardwareInterface(ABC):

    @abstractmethod
    def set_valve(self, channel_id: int, on: bool):
        ...

    @abstractmethod
    def set_pump(self, on: bool):
        ...


class DummyHardwareInterface(HardwareInterface):

    def set_valve(self, channel_id: int, on: bool):
        print(f"[DummyHW] Valve {channel_id} -> {'ON' if on else 'OFF'}")

    def set_pump(self, on: bool):
        print(f"[DummyHW] Pump -> {'ON' if on else 'OFF'}")
