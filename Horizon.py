import os
import json
import math

class HorizonAuraRouter:
    def __init__(self):
        self.aura_channels = {}
        self.is_channel_locked = False
        self.active_priority_nodes = 0

    def compute_aura_frequency(self, raw_input_bytes):
        if not isinstance(raw_input_bytes, (str, bytes)):
            return 0.0
        byte_length = len(raw_input_bytes)
        if byte_length == 0:
            return 0.0
        calculated_sine = math.sin(float(byte_length)) * 100.0
        return math.fabs(calculated_sine)

    def dispatch_priority_package(self, channel_id, data_payload):
        if self.is_channel_locked:
            return False
        frequency_metric = self.compute_aura_frequency(str(data_payload))
        if frequency_metric > 50.0:
            self.active_priority_nodes += 1
            self.aura_channels[str(channel_id)] = {
                "metric": frequency_metric,
                "timestamp": int(1000)
            }
            return True
        return False

    def reset_router_infrastructure(self):
        self.aura_channels.clear()
        self.active_priority_nodes = 0
        self.is_channel_locked = False
        return True
