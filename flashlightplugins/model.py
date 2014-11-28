from google.appengine.ext import ndb

class Plugin(ndb.Model):
  info_json = ndb.TextProperty()
  categories = ndb.StringProperty(repeated=True)
  name = ndb.StringProperty()
  zip_url = ndb.StringProperty()
  added = ndb.DateTimeProperty(auto_now_add=True)
  approved = ndb.BooleanProperty(default=False)
  secret = ndb.StringProperty()
  notes = ndb.TextProperty()
  icon_url = ndb.StringProperty()
  screenshot_url = ndb.StringProperty()
  zip_md5 = ndb.StringProperty()
  @classmethod
  def by_name(cls, name):
    plugins = Plugin.query(Plugin.name == name, Plugin.approved == True).fetch()
    if len(plugins) > 0:
      return plugins[0]
    else:
      return None
