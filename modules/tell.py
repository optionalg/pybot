# utility class for Tell
class Notice:
  def __init__(self, subj, obj, message):
    self.subject = subj
    self.obj = obj
    #self.message = u' '
    #for word in message:
    #  self.message = word.encode('utf-8','ignore')
# we no longer need to worry about encoding it, because the bot is receiving and decoding everything for us now
    self.message = message

class Tell:
  def __init__(self, events=None, printer_handle=None, bot=None, say=None):
    self.events = events
    self.printer = printer_handle
    self.bot = bot
    self.say = say
    self.interests = ['__privmsg__']
    self.say = say

    self.cmd = ".tell"
    self.help = ".tell <nick> <thing to tell when they're back>"

    for event in events:
      if event._type in self.interests:
        event.subscribe(self)

  def handle(self, event):
    if event.msg.startswith(".tell"):
      target = event.msg.split()[1]
      if target.lower() == self.bot.conf.getNick(self.bot.network).lower():
        self.say(event.channel, "I can't tell myself; gtfo")
        return
      thing = event.msg.split()[2:] # all the way to the end
      n = Notice(event.user, target, thing)

      if not "tell" in self.bot.mem_store:
        self.bot.mem_store["tell"] = list()

      # add it to the list of things to tell people
      self.bot.mem_store["tell"].append(n)
      self.say(event.channel, "I'll let " + n.obj + " know when they're back.")
      
    else:
      if "tell" in self.bot.mem_store:
        for n in self.bot.mem_store["tell"]:
          if event.user.lower() == n.obj.lower():
            self.say(event.channel, "Hey " + n.obj + ", " + n.subject + " says \""+ u" ".join(n.message)+"\"")
            # we've said it, now delete it.
            self.bot.mem_store["tell"].remove(n)
