#!/usr/bin/python3
import logging

#
#
#
# PDF HIDE
#

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
#
# Copyright (C) 2013 Nicolas Canceill
#

#
# logger.py
__version__ = "0.0a"
#
# This is a logging engine for pdf_hide v0.0a
#
# Written by Nicolas Canceill
# Last updated on Sept 29, 2013
# Hosted at https://github.com/ncanceill/pdf_hide
#

#
#
#
# STATIC
#

LOG_FORMAT = "%(levelname)s:	%(message)s"

CRITICAL=-1
ERROR=0
INFO=1
DEBUG=2

MSG_VERSION = "This is PDF_HIDE v" + __version__
MSG_DESC = """A steganographic tool for hiding data inside PDF files
Hosted at https://github.com/ncanceill/pdf_hide"""
MSG_LICENSE = """PDF_HIDE  Copyright (C) 2013  Nicolas Canceill
Distributed under GNU General Public License v3
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
Please see LICENSE.md or http://www.gnu.org/licenses/ for details."""

#
#
#
# CLASSES
#

class rootLogger:
	def __init__(self,verbose=0):
		logging.basicConfig(format=LOG_FORMAT)
		if verbose == CRITICAL:
			logging.getLogger().setLevel(logging.CRITICAL)
		elif verbose == ERROR:
			logging.getLogger().setLevel(logging.ERROR)
		elif verbose == INFO:
			logging.getLogger().setLevel(logging.INFO)
		self.DEBUG = False
		if verbose == DEBUG:
			logging.getLogger().setLevel(logging.DEBUG)
			self.DEBUG=True

	def print_splash(self,parser):
		print("====================")
		print(MSG_VERSION)
		print("====================")

	def print_discl(self,parser):
		print("====================")
		print(MSG_LICENSE)
		print("====================")

	def critical(self,msg):
		logging.critical(msg)

	def error(self,msg):
		logging.error(msg)

	def warn(self,msg):
		logging.warning(msg)

	def info(self,msg):
		logging.info(msg)

	def debug(self,msg):
		logging.debug(msg)
