#    X-tra-Telegram (userbot for telegram)
#    Copyright (C) 2019-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/

from xtrabot import PPESupport as ppe, UniSupport as uni, MOD_LIST, client, ModLogger
import re
from telethon import events
class SupportMods():
    class UNISupport():
        def reggie(self, events):
            def decorator(func):
                self.logger = ModLogger.log(func.__name__)
                s ="""async def {}(event, func=func, self=self):
    from xtrabot import client, trustUser
    if event.from_id in trustUser and event.from_id != (await client.get_me()).id:
        event2 = await event.respond("Processing,")
        event.edit = event2.edit
    elif event.from_id == (await client.get_me()).id:
        pass
    else:
        return
    try:
        await func(event)
    except Exception as error:
        await event.reply("__Error occured on the current__ `{}`, __do__ `.log` __to show the latest log.__")
        self.logger.exception(error)""".format(func.__name__,"."+func.__name__)
                exec(s, None, locals())
                client.add_event_handler(locals()[func.__name__], events)
            return decorator
        def uniadmin(self, pattern=None, **args):
            args["pattern"] = re.compile(uni.COMMAND_HAND_LER + pattern)
            MOD_LIST[list(MOD_LIST.keys())[-1]].append("."+pattern)
            if not "outgoing" in args:
                if not "incoming" in args:
                   args["outgoing"] = True 
            if "allow sudo" in args:
                del args["allow_sudo"]
            if "allow_edited_updates" in args:
                del args["allow_edited_updates"]
            return events.NewMessage(**args)
    class PPESupport():
        def register(self, **args):
            try:
                MOD_LIST[list(MOD_LIST.keys())[-1]].append(args["pattern"])
            except:
                pass
            def decorator(func):
                kwargs = {}
                kwargs["pattern"] = args["pattern"] if "pattern" in args else None
                kwargs["outgoing"] = args["outgoing"] if "outgoing" in args else False
                kwargs["incoming"] = args["incoming"] if "incoming" in args else False
                logger = ModLogger.log(func.__name__)
                s ="""async def {}(event, func=func, logger=logger, kwargs=kwargs):
    from xtrabot import client, trustUser
    from telethon.events import StopPropagation
    if event.from_id in trustUser and event.from_id != (await client.get_me()).id:
        event2 = await event.respond("Processing,")
        event.edit = event2.edit
    elif event.from_id == (await client.get_me()).id:
        pass
    elif "incoming" in kwargs:
        if kwargs["incoming"] == True:
            pass
    else:
        return
    try:
        await func(event)
    except StopPropagation:
        pass
    except Exception as error:
        await event.reply("__Error occured on the current__ `{}`, __do__ `.log` __to show the latest log.__")
        logger.exception(error)""".format(func.__name__,"."+func.__name__)
                exec(s, None, locals())
                del kwargs["incoming"] 
                client.add_event_handler(locals()[func.__name__], events.NewMessage(incoming=True,**kwargs))
                return func
            return decorator

        def ppevar(self):
            BOTLOG_CHATID = ppe.BOTLOG_CHATID;BOTLOG = ppe.BOTLOG;LOGSPAMMER = ppe.LOGSPAMMER;PM_AUTO_BAN = ppe.PM_AUTO_BAN;CONSOLE_LOGGER_VERBOSE = ppe.CONSOLE_LOGGER_VERBOSE;DB_URI = ppe.DB_URI;OCR_SPACE_API_KEY = ppe.OCR_SPACE_API_KEY;REM_BG_API_KEY = ppe.REM_BG_API_KEY;CHROME_DRIVER = ppe.CHROME_DRIVER;GOOGLE_CHROME_BIN = ppe.GOOGLE_CHROME_BIN;OPEN_WEATHER_MAP_APPID = ppe.OPEN_WEATHER_MAP_APPID;WEATHER_DEFCITY = ppe.WEATHER_DEFCITY;ANTI_SPAMBOT = ppe.ANTI_SPAMBOT;ANTI_SPAMBOT_SHOUT = ppe.ANTI_SPAMBOT_SHOUT;YOUTUBE_API_KEY = ppe.YOUTUBE_API_KEY;ALIVE_NAME = ppe.ALIVE_NAME;COUNTRY = ppe.COUNTRY;TZ_NUMBER = ppe.TZ_NUMBER;CLEAN_WELCOME = ppe.CLEAN_WELCOME;BIO_PREFIX = ppe.BIO_PREFIX;DEFAULT_BIO = ppe.DEFAULT_BIO;LASTFM_API = ppe.LASTFM_API;LASTFM_SECRET = ppe.LASTFM_SECRET;LASTFM_USERNAME = ppe.LASTFM_USERNAME;LASTFM_PASSWORD_PLAIN = ppe.LASTFM_PASSWORD_PLAIN;LASTFM_PASS = ppe.LASTFM_PASS;lastfm = ppe.lastfm;G_DRIVE_CLIENT_ID = ppe.G_DRIVE_CLIENT_ID;G_DRIVE_CLIENT_SECRET = ppe.G_DRIVE_CLIENT_SECRET;G_DRIVE_AUTH_TOKEN_DATA = ppe.G_DRIVE_AUTH_TOKEN_DATA;GDRIVE_FOLDER_ID = ppe.GDRIVE_FOLDER_ID;TEMP_DOWNLOAD_DIRECTORY = ppe.TEMP_DOWNLOAD_DIRECTORY;COUNT_MSG = ppe.COUNT_MSG;USERS = ppe.USERS;COUNT_PM = ppe.COUNT_PM;LASTMSG = ppe.LASTMSG;CMD_HELP = ppe.CMD_HELP;ISAFK = ppe.ISAFK;AFKREASON = ppe.AFKREASON;bot = ppe.bot
            return BOTLOG_CHATID,BOTLOG,LOGSPAMMER,PM_AUTO_BAN,CONSOLE_LOGGER_VERBOSE,DB_URI,OCR_SPACE_API_KEY,REM_BG_API_KEY,CHROME_DRIVER,GOOGLE_CHROME_BIN,OPEN_WEATHER_MAP_APPID,WEATHER_DEFCITY,ANTI_SPAMBOT,ANTI_SPAMBOT_SHOUT,YOUTUBE_API_KEY,ALIVE_NAME,COUNTRY,TZ_NUMBER,CLEAN_WELCOME,BIO_PREFIX,DEFAULT_BIO,LASTFM_API,LASTFM_SECRET,LASTFM_USERNAME,LASTFM_PASSWORD_PLAIN,LASTFM_PASS,lastfm,G_DRIVE_CLIENT_ID ,G_DRIVE_CLIENT_SECRET,G_DRIVE_AUTH_TOKEN_DATA,GDRIVE_FOLDER_ID,TEMP_DOWNLOAD_DIRECTORY,COUNT_MSG,USERS,COUNT_PM,LASTMSG,CMD_HELP,ISAFK,AFKREASON,bot
