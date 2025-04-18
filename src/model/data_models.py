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
    watering_duration: time = field(default_factory=lambda: time(minute=1))


@dataclass
class Schedule:
    sunsetMode: bool = True
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    cycle_interval: time = field(default_factory=lambda: time(hour=1, minute=0))
    is_auto_watering_enabled: bool = False


@dataclass
class ApplicationState:
    pump: Channel = field(default_factory=lambda: Channel(0, "Pump", type=ChannelType.PUMP, is_active=True))
    channels: Dict[int, Channel] = field(default_factory=dict)
    groups: Dict[int, Group] = field(default_factory=list)
    schedule: Schedule = field(default_factory=Schedule)

    selected_channel_id: int = None

    @staticmethod
    def default_state():
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
            1: Group(1),
            2: Group(2),
            3: Group(3),
            4: Group(4),
            5: Group(5),
            6: Group(6),
            7: Group(7),
        }

        return ApplicationState(channels=channels, groups=groups)
