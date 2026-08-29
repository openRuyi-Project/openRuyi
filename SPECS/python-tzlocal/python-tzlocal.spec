# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tzlocal

Name:           python-%{srcname}
Version:        5.3.1
Release:        %autorelease
Summary:        tzinfo object for the local timezone
License:        MIT
URL:            https://github.com/regebro/tzlocal
#!RemoteAsset:  sha256:cceffc7edecefea1f595541dbd6e990cb1ea3d19bf01b2809f362a03dd7921fd
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# No windows stuff
BuildOption(check):  -e tzlocal.win32
BuildOption(check):  -e tzlocal.windows_tz

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This Python module returns a tzinfo object with the local timezone information
under Unix and Win-32. It requires pytz, and returns pytz tzinfo objects.

This module attempts to fix a glaring hole in pytz, that there is no way to get
the local timezone information, unless you know the zoneinfo name, and under
several Linux distros that’s hard or impossible to figure out.

Also, with Windows different timezone system using pytz isn’t of much use unless
you separately configure the zoneinfo timezone name.

With tzlocal you only need to call get_localzone() and you will get a tzinfo
object with the local time zone info. On some Unices you will still not get to
know what the timezone name is, but you don’t need that when you have the tzinfo
file. However, if the timezone name is readily available it will be used.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
