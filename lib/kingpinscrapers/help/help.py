# -*- coding: utf-8 -*-
"""
	kingpinscrapers Module
"""

from kingpinscrapers.modules.control import addonPath, addonVersion, joinPath
from kingpinscrapers.windows.textviewer import TextViewerXML


def get(file):
	kingpinscrapers_path = addonPath()
	kingpinscrapers_version = addonVersion()
	helpFile = joinPath(kingpinscrapers_path, 'lib', 'kingpinscrapers', 'help', file + '.txt')
	r = open(helpFile, 'r', encoding='utf-8', errors='ignore')
	text = r.read()
	r.close()
	heading = '[B]kingpinScrapers -  v%s - %s[/B]' % (kingpinscrapers_version, file)
	windows = TextViewerXML('textviewer.xml', kingpinscrapers_path, heading=heading, text=text)
	windows.run()
	del windows