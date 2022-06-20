#                 __
#    ____ _____  |  | _____
#   /    \\__  \ |  | \__  \
#  |   |  \/ __ \|  |__/ __ \_
#  |___|  (____  /____(____  /
#       \/     \/          \/
#
# Copyright (C) 2021, 2022 Blake Lee
#
# This file is part of nala
#
# nala is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# nala is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with nala.  If not, see <https://www.gnu.org/licenses/>.
"""Module for file constants."""
from __future__ import annotations

import re
from enum import IntEnum
from pathlib import Path
from signal import Handlers  # pylint: disable=no-name-in-module #Codacy
from types import FrameType
from typing import Any, Callable, Optional, Union

import apt_pkg

from nala import _, color


def apt_path(key: str, file: bool = False) -> Path:
	"""Return a Path object for the apt dir."""
	if file:
		return Path(apt_pkg.config.find_file(key))
	return Path(apt_pkg.config.find_dir(key))


# File Constants
GPL3_LICENSE = Path("/usr/share/common-licenses/GPL-3")
"""/usr/share/common-licenses/GPL-3"""
NALA_SOURCES = Path("/etc/apt/sources.list.d/nala-sources.list")
"""/etc/apt/sources.list.d/nala-sources.list"""
NALA_DIR = Path("/var/lib/nala")
"""/var/lib/nala"""
NALA_LOGDIR = Path("/var/log/nala")
"""/var/log/nala"""
NALA_DEBUGLOG = NALA_LOGDIR / "nala-debug.log"
"""/var/log/nala/nala.debug.log"""
DPKG_LOG = NALA_LOGDIR / "dpkg-debug.log"
"""/var/log/nala/dpkg-debug.log"""
DPKG_STATUS_LOG = NALA_LOGDIR / "dpkg-status.log"
"""/var/log/nala/dpkg-status.log"""
NALA_TERM_LOG = Path("/var/log/nala/term.log")
"""/var/log/nala/term.log"""
NALA_HISTORY = Path("/var/lib/nala/history.json")
"""/var/lib/nala/history.json"""
# NALA_BUNDLE = Path("/var/lib/nala/bundle.json")
NALA_BUNDLE = Path("./bundle.json.gz")
"""/var/lib/nala/bundle.json"""
PACSTALL_METADATA = Path("/var/log/pacstall/metadata")
"""/var/log/pacstall/metadata"""
REBOOT_REQUIRED = Path("/var/run/reboot-required")
"""/var/run/reboot-required"""
REBOOT_PKGS = Path("/var/run/reboot-required.pkgs")
"""'/var/run/reboot-required.pkgs'"""
NEED_RESTART = Path("/var/run/needrestart")
"""/var/run/needrestart"""
NALA_LOCK_FILE = Path("/var/lock/nala.lock")
"""/var/lock/nala.lock"""
NALA_CONF = Path("/etc/nala/nala.conf")
"""/etc/nala/nala.conf"""

# Apt Directories
ARCHIVE_DIR = apt_path("Dir::Cache::Archives")
"""/var/cache/apt/archives/"""
PARTIAL_DIR = ARCHIVE_DIR / "partial"
"""/var/cache/apt/archives/partial"""
LISTS_DIR = apt_path("Dir::State::Lists")
"""/var/lib/apt/lists/"""
LISTS_PARTIAL_DIR = LISTS_DIR / "partial"
"""/var/lib/apt/lists/partial"""
PKGCACHE = apt_path("Dir::Cache::pkgcache")
"""/var/cache/apt/pkgcache.bin"""
SRCPKGCACHE = apt_path("Dir::Cache::srcpkgcache")
"""/var/cache/apt/srcpkgcache.bin"""
SOURCELIST = apt_path("Dir::Etc::sourcelist", file=True)
"""/etc/apt/sources.list"""
SOURCEPARTS = apt_path("Dir::Etc::sourceparts")
"""/etc/apt/sources.list.d"""
DPKG_STATE = apt_path("Dir::State::status")
"""/var/lib/dpkg/status"""

TRUSTED = apt_path("Dir::Etc::trusted", file=True)
"""/etc/apt/trusted.gpg"""
TRUSTEDPARTS = apt_path("Dir::Etc::trustedparts")
"""/etc/apt/trusted.gpg.d/"""
APT_CONF = apt_path("Dir::Etc::main", file=True)
"""/etc/apt/apt.conf"""
APT_CONF_PARTS = apt_path("Dir::Etc::parts")
"""/etc/apt/apt.conf.d/"""
PREFERENCES = apt_path("Dir::Etc::preferences", file=True)
"""/etc/apt/preferences"""
PREFERENCES_PARTS = apt_path("Dir::Etc::preferencesparts")
"""/etc/apt/preferences.d/"""

HANDLER = Union[Callable[[int, Optional[FrameType]], Any], int, Handlers, None]

ERROR_PREFIX = color(_("Error:"), "RED")
WARNING_PREFIX = color(_("Warning:"), "YELLOW")
NOTICE_PREFIX = color(_("Notice:"), "YELLOW")

# Compiled Regex
ERRNO_PATTERN = re.compile(r"\[.*\]")


class SelectedState(IntEnum):
	"""Selected state constants for pkgs."""

	UNKNOWN = 0
	INSTALL = 1
	HOLD = 2
	DEINSTALL = 3
	PURGE = 4


class CurrentState(IntEnum):
	"""Current state constants for pkgs."""

	NOT_INSTALLED = 0
	UNPACKED = 1
	HALF_CONFIGURED = 2
	HALF_INSTALLED = 4
	CONFIG_FILES = 5
	INSTALLED = 6
	TRIGGERS_AWAITED = 7
	TRIGGERS_PENDING = 8


class InstState(IntEnum):
	"""Installed state constants for pkgs."""

	OK = 0
	REINSTREQ = 1
	HOLD_INST = 2
	HOLD_REINSTREQ = 3


# dpkg constants
CONF_MESSAGE = (
	b"   What would you like to do about it ?  Your options are:\r\n"
	b"    Y or I  : install the package maintainer's version\r\n"
	b"    N or O  : keep your currently-installed version\r\n"
	b"      D     : show the differences between the versions\r\n"
	b"      Z     : start a shell to examine the situation\r\n"
)
CONF_ANSWERS = (
	b"y",
	b"Y",
	b"i",
	b"I",
	b"n",
	b"N",
	b"o",
	b"O",
)
NOTICES = (
	b"The currently running kernel version is not the expected kernel version",
	b"Please remove.",
	b"NOTICE:",
	b"Warning:",
)
SPAM = (
	# Stuff that's pretty useless
	"(Reading database",  #'(Reading database ... 247588 files and directories currently installed.)'
	"files and directories currently installed.)",
	"Selecting previously unselected package",  # 'Selecting previously unselected package chafa.'
	"Preparing to unpack",  # 'Preparing to unpack .../2-chafa_1.8.0-1_amd64.deb ...'
	"Extracting templates from packages:",
	"Fetched",
)
DPKG_STATUS = (
	b"Scanning processes...",
	b"Scanning candidates...",
	b"Scanning linux images...",
	b"Extracting templates from packages",
	b"Reading changelogs...",
	b"Retrieving bug reports...",
	b"Parsing Found/Fixed information...",
	b"[Working]",
	b"[Connecting",
	b"[Waiting for headers]",
	b"[Connected to",
)
DPKG_ERRORS = (
	b"dpkg:",
	b"failed to allocate memory for new entry",
	b"error processing package",
	b"error processing archive",
	b"Errors were encountered while processing",
	b"Processing was halted because there were too many errors",
)
CAT = r"""
   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  sk
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
"""
