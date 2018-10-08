from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Steven'

LOGGER = getLogger(__name__)


class ThreeIntentSkill(MycroftSkill):
    def __init__(self):
        super(ThreeIntentSkill, self).__init__(name="ThreeIntentSkill")

    def initialize(self):
        color_sun_intent = IntentBuilder("ColorSunIntent"). \
            require("ColorSun").build()
        self.register_intent(color_sun_intent, self.handle_color_sun_intent)

        fun_fact_intent = IntentBuilder("FunFactIntent"). \
            require("FunFact").build()
        self.register_intent(fun_fact_intent,
                             self.handle_fun_fact_intent)

        play_instrument_intent = IntentBuilder("PlayInstrumentIntent"). \
            require("PlayInstrument").build()
        self.register_intent(play_instrument_intent,
                             self.handle_play_instruments_intent)

    def handle_color_sun_intent(self, message):
        self.speak_dialog("color")

    def handle_fun_fact_intent(self, message):
        self.speak_dialog("fact")

    def handle_play_instruments_intent(self, message):
        self.speak_dialog("instruments")

    def stop(self):
        pass


def create_skill():
    return ThreeIntentSkill()
