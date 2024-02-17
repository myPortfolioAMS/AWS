# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.supersim.v1.esim_profile import EsimProfileList
from twilio.rest.supersim.v1.fleet import FleetList
from twilio.rest.supersim.v1.ip_command import IpCommandList
from twilio.rest.supersim.v1.network import NetworkList
from twilio.rest.supersim.v1.network_access_profile import NetworkAccessProfileList
from twilio.rest.supersim.v1.settings_update import SettingsUpdateList
from twilio.rest.supersim.v1.sim import SimList
from twilio.rest.supersim.v1.sms_command import SmsCommandList
from twilio.rest.supersim.v1.usage_record import UsageRecordList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Supersim

        :returns: V1 version of Supersim
        :rtype: twilio.rest.supersim.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._esim_profiles = None
        self._fleets = None
        self._ip_commands = None
        self._networks = None
        self._network_access_profiles = None
        self._settings_updates = None
        self._sims = None
        self._sms_commands = None
        self._usage_records = None

    @property
    def esim_profiles(self):
        """
        :rtype: twilio.rest.supersim.v1.esim_profile.EsimProfileList
        """
        if self._esim_profiles is None:
            self._esim_profiles = EsimProfileList(self)
        return self._esim_profiles

    @property
    def fleets(self):
        """
        :rtype: twilio.rest.supersim.v1.fleet.FleetList
        """
        if self._fleets is None:
            self._fleets = FleetList(self)
        return self._fleets

    @property
    def ip_commands(self):
        """
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandList
        """
        if self._ip_commands is None:
            self._ip_commands = IpCommandList(self)
        return self._ip_commands

    @property
    def networks(self):
        """
        :rtype: twilio.rest.supersim.v1.network.NetworkList
        """
        if self._networks is None:
            self._networks = NetworkList(self)
        return self._networks

    @property
    def network_access_profiles(self):
        """
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileList
        """
        if self._network_access_profiles is None:
            self._network_access_profiles = NetworkAccessProfileList(self)
        return self._network_access_profiles

    @property
    def settings_updates(self):
        """
        :rtype: twilio.rest.supersim.v1.settings_update.SettingsUpdateList
        """
        if self._settings_updates is None:
            self._settings_updates = SettingsUpdateList(self)
        return self._settings_updates

    @property
    def sims(self):
        """
        :rtype: twilio.rest.supersim.v1.sim.SimList
        """
        if self._sims is None:
            self._sims = SimList(self)
        return self._sims

    @property
    def sms_commands(self):
        """
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandList
        """
        if self._sms_commands is None:
            self._sms_commands = SmsCommandList(self)
        return self._sms_commands

    @property
    def usage_records(self):
        """
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordList
        """
        if self._usage_records is None:
            self._usage_records = UsageRecordList(self)
        return self._usage_records

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1>'
