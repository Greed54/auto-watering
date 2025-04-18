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
    next_watering_time: Optional[datetime] = None
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
    sunset_mode: bool = True
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    cycle_interval: time = field(default_factory=lambda: time(hour=1, minute=0))
    is_auto_watering_enabled: bool = False


@dataclass
class SchedulerState:
    in_progress: bool = False  # whether a watering cycle is running
    last_cycle_start: Optional[datetime] = None
    current_group_id: Optional[int] = None
    group_remaining_sec: int = 0  # seconds left in the current group
    next_cycle_time: Optional[datetime] = None
    paused: bool = False  # are we currently paused?


@dataclass
class ApplicationState:
    pump: Channel = field(default_factory=lambda: Channel(0, "Pump", type=ChannelType.PUMP, is_active=True))
    channels: Dict[int, Channel] = field(default_factory=dict)
    groups: Dict[int, Group] = field(default_factory=list)
    schedule: Schedule = field(default_factory=Schedule)

    selected_channel_id: int = None
    scheduler_state: SchedulerState = field(default_factory=SchedulerState)

    @staticmethod
    def default_state():
        channels = {i: Channel(i, f"Channel {i}", group_id=1) for i in range(1, 8)}
        groups = {i: Group(i) for i in range(1, 8)}

        return ApplicationState(channels=channels, groups=groups)
