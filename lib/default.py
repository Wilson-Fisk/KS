# -*- coding: utf-8 -*-
"""
	kingpinscrapers Module
"""

from sys import argv
from urllib.parse import parse_qsl
from kingpinscrapers import sources_kingpinscrapers
from kingpinscrapers.modules import control

params = dict(parse_qsl(argv[2].replace('?', '')))
action = params.get('action')
mode = params.get('mode')
query = params.get('query')
name = params.get('name')

if action is None:
	control.openSettings('0.0', 'script.module.kingpinscrapers')

if action == "kingpinScrapersSettings":
	control.openSettings('0.0', 'script.module.kingpinscrapers')

elif mode == "kingpinScrapersSettings":
	control.openSettings('0.0', 'script.module.kingpinscrapers')

elif action == 'ShowChangelog':
	from kingpinscrapers.modules import changelog
	changelog.get()

elif action == 'ShowHelp':
	from kingpinscrapers.help import help
	help.get(name)

elif action == "Defaults":
	sourceList = []
	sourceList = sources_kingpinscrapers.all_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		value = control.getSettingDefault(source_setting)
		control.setSetting(source_setting, value)

elif action == "toggleAll":
	sourceList = []
	sourceList = sources_kingpinscrapers.all_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllHosters":
	sourceList = []
	sourceList = sources_kingpinscrapers.hoster_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllTorrent":
	sourceList = []
	sourceList = sources_kingpinscrapers.torrent_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllPackTorrent":
	control.execute('RunPlugin(plugin://script.module.kingpinscrapers/?action=toggleAllTorrent&amp;setting=false)')
	control.sleep(500)
	sourceList = []
	from kingpinscrapers import pack_sources
	sourceList = pack_sources()
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == 'openMyAccount':
	from myaccounts import openMASettings
	openMASettings('0.0')
	control.sleep(500)
	while control.condVisibility('Window.IsVisible(addonsettings)') or control.homeWindow.getProperty('myaccounts.active') == 'true':
		control.sleep(500)
	control.sleep(100)
	control.syncmyaccounts()
	control.sleep(100)
	if params.get('opensettings') == 'true':
		control.openSettings(query, 'script.module.kingpinscrapers')

elif action == 'syncMyAccount':
	control.syncmyaccounts()
	if params.get('opensettings') == 'true':
		control.openSettings(query, 'script.module.kingpinscrapers')

elif action == 'cleanSettings':
	control.clean_settings()

elif action == 'undesirablesSelect':
	from kingpinscrapers.modules.undesirables import undesirablesSelect
	undesirablesSelect()

elif action == 'undesirablesInput':
	from kingpinscrapers.modules.undesirables import undesirablesInput
	undesirablesInput()

elif action == 'undesirablesUserRemove':
	from kingpinscrapers.modules.undesirables import undesirablesUserRemove
	undesirablesUserRemove()

elif action == 'undesirablesUserRemoveAll':
	from kingpinscrapers.modules.undesirables import undesirablesUserRemoveAll
	undesirablesUserRemoveAll()

elif action == 'tools_clearLogFile':
	from kingpinscrapers.modules import log_utils
	cleared = log_utils.clear_logFile()
	if cleared == 'canceled': pass
	elif cleared: control.notification(message='kingpinScrapers Log File Successfully Cleared')
	else: control.notification(message='Error clearing kingpinScrapers Log File, see kodi.log for more info')

elif action == 'tools_viewLogFile':
	from kingpinscrapers.modules import log_utils
	log_utils.view_LogFile(name)

elif action == 'tools_uploadLogFile':
	from kingpinscrapers.modules import log_utils
	log_utils.upload_LogFile()