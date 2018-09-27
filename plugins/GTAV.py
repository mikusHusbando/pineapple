import requests
import re
import discord
from util import Events

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm
        self.name = "GTAV"

    @staticmethod
    def register_events():
        return [Events.Message("GTAV")]

    async def handle_message(self, message_object):
        
        #credits to this guy https://docs.google.com/spreadsheets/d/1mX8wGG1Oy76nhv-tBZ-oPmKiynng8fMS87EMxmoyB0Y/htmlview#gid=827245973
        
        #wenn message_object.content hat !so und so
        
        
        !supplied docs weed cash meth cocaine bunker
        !sold docs weed cash meth cocaine bunker
        !pause {docs weed cash meth cocaine bunker}
        !resume {docs weed cash meth cocaine bunker}
