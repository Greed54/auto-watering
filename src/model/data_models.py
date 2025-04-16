from dataclasses import dataclass, field
from datetime import datetime, time
from enum import Enum
from typing import Optional, Dict


class ChannelType(Enum):
    VALVE = 'valve'
    PUMP = 'pump'


@dataclass
class Channel:
    id: int
    name: str
    last_activation: Optional[datetime] = None
    type: ChannelType = ChannelType.VALVE
    group_id: Optional[int] = None
    is_active: bool = False
    is_enabled: bool = False


@dataclass
class Group:
    id: int
    water_duration_seconds: int = None


@dataclass
class Schedule:
    start_time: time
    end_time: time
    cycle_interval_seconds: int
    active: bool = True


@dataclass
class ApplicationState:
    selected_channel_id: int = None
    pump: Channel = field(default_factory=lambda: Channel(0, "Pump", type=ChannelType.PUMP, is_active=True))
    channels: Dict[int, Channel] = field(default_factory=dict)
    groups: Dict[int, Group] = field(default_factory=list)
    schedule: Optional[Schedule] = None

    @staticmethod
    def _default_state():
        channels = {
            1: Channel(1, "Channel 1", group_id=1),
            2: Channel(2, "Channel 2", group_id=1),
            3: Channel(3, "Channel 3", group_id=1),
            4: Channel(4, "Channel 4", group_id=1),
            5: Channel(5, "Channel 5", group_id=1),
            6: Channel(6, "Channel 6", group_id=1),
            7: Channel(7, "Channel 7", group_id=1),
        }

        groups = {
            1: Group(1)
        }

        return ApplicationState(channels=channels, groups=groups)
