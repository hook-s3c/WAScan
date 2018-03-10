#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from lib.utils.check import *
from lib.utils.printer import *
from lib.utils.readfile import *
from lib.request.request import *

class multitarget():

  def __init__(self,targetPath):
    self.targetPath = targetPath

  def run(self):
    targets = []
    with open(self.targetPath) as f:
      content = f.readlines()
      targets = content
    return targets