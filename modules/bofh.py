import urllib2
from event import Event
try:
  from basemodule import BaseModule
except ImportError:
  from modules.basemodule import BaseModule
class Bofh(BaseModule):
  def post_init(self):
    b_event = Event("__.bofh__")

    b_event.define(msg_definition="^\.bofh")
    b_event.subscribe(self)

    self.bot.register_event(b_event, self)

  def handle(self, event):
    try:
      url = "http://zero9f9.com/api/bofh"
      response = urllib2.urlopen(url)
      text = response.read()
      bofhquote = text.splitlines()[2]
      self.say(event.channel, "BOFH: " + bofhquote)
    except:
      pass
