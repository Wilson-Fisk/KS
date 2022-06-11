# -*- coding: utf-8 -*-
"""
	kingpinscrapers Module
"""

from kingpinscrapers.modules.control import addonPath, addonVersion, joinPath
from kingpinscrapers.windows.textviewer import TextViewerXML


def get():
	kingpinscrapers_path = addonPath()
	kingpinscrapers_version = addonVersion()
	changelogfile = joinPath(kingpinscrapers_path, 'changelog.txt')
	r = open(changelogfile, 'r', encoding='utf-8', errors='ignore')
	text = r.read()
	r.close()
	heading = '[B]kingpinScrapers -  v%s - ChangeLog[/B]' % kingpinscrapers_version
	windows = TextViewerXML('textviewer.xml', kingpinscrapers_path, heading=heading, text=text)
	windows.run()
	del windows