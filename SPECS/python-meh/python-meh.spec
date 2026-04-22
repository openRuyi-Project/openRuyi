# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-meh
Version:        0.52
Release:        %autorelease
Summary:        A python library for handling exceptions
License:        GPL-2.0-or-later
URL:            https://github.com/rhinstaller/python-meh
#!RemoteAsset:  sha256:7b66046b4693e7631aad299e5a55d0255962608cd03372f559745c575aa8c920
Source0:        https://github.com/rhinstaller/python-meh/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(dbus-python)

Provides:       python3-meh = %{version}-%{release}
%python_provide python3-meh

Requires:       python3dist(dbus-python)
Requires:       python3dist(rpm)
Requires:       python3dist(pygobject)

%description
The python-meh package is a python library for handling, saving,
and reporting exceptions.

# No configure
%conf

%check
make test

%files
%doc COPYING
%{python3_sitelib}/*
%{_datadir}/python-meh

%changelog
%autochangelog
