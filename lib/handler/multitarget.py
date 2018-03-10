#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k), Hook (@hook_s3c)
# @license: See the file 'LICENSE.txt

from plugins.multitarget.multitarget import *
from lib.utils.printer import *

def MultiTarget(targetPath):
	info("Starting multitarget module...")
	return multitarget(targetPath).run()