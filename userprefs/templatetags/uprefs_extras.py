from django import template
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from mailng import userprefs
from mailng.lib import events

register = template.Library()

@register.simple_tag
def uprefs_menu(user):
    entries = [
        {"name"  : "userprefs",
         "img"   : "/static/pics/user.png",
         "label" : _("Options"),
         "class" : "topdropdown",
         "menu"  : [
                {"name" : "changepwd",
                 "url" : reverse(userprefs.views.changepassword),
                 "img" : "/static/pics/edit.png",
                 "label" : _("Change password"),
                 "class" : "boxed",
                 "rel" : "{handler:'iframe',size:{x:350,y:220}}"},
                {"name" : "preferences",
                 "img" : "/static/pics/user.png",
                 "label" : _("Preferences"),
                 "url" : reverse(userprefs.views.preferences),
                 }
                ]
         },
        ]
    entries[0]["menu"] += events.raiseQueryEvent("UserMenuDisplay", 
                                                 target="user_menu_bar")

    return render_to_string('common/menulist.html', 
                            {"entries" : entries, "user" : user})

@register.simple_tag
def loadextmenu(user):
    menu = events.raiseQueryEvent("UserMenuDisplay", target="user_menu_box", 
                                  user=user)
    return render_to_string('common/menulist.html', 
                            {"entries" : menu, "user" : user})