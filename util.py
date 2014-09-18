import re
class bcolors:
  """
  Allows for prettyprinting to the console for debugging.
  """
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  CYAN = '\033[36m'
  GREEN = '\033[32m'
  YELLOW = '\033[33m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

def strip_nick(nick):
  """
  Clean up nicks of their op levels (&Schooly_D, ~BoneKin, etc)
  """
  nick = re.sub('[@~+]', '', nick)
  return nick

def __prettyDate(time):
  """
  Similar to Rails's nice time since thing.
  """
  now = datetime.now()
  if type(time) is int:
    diff = now - datetime.fromtimestamp(time)
  elif isinstance(time,datetime):
    diff = now - time 
  elif not time:
    diff = now - now
  second_diff = diff.seconds
  day_diff = diff.days

  if day_diff < 0:
    return ''

  if day_diff == 0:
    if second_diff < 10:
      return "just now"
    if second_diff < 60:
      return str(second_diff) + " seconds ago"
    if second_diff < 120:
      return  "a minute ago"
    if second_diff < 3600:
      return str( second_diff / 60 ) + " minutes ago"
    if second_diff < 7200:
      return "an hour ago"
    if second_diff < 86400:
      return str( second_diff / 3600 ) + " hours ago"
    if day_diff == 1:
      return "Yesterday"
    if day_diff < 7:
      return str(day_diff) + " days ago"
    if day_diff < 31:
      return str(day_diff/7) + " weeks ago"
    if day_diff < 365:
      return str(day_diff/30) + " months ago"
    return str(day_diff/365) + " years ago"
