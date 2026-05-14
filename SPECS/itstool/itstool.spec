# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           itstool
Version:        2.0.7
Release:        %autorelease
Summary:        ITS-based XML translation tool
License:        GPL-3.0-or-later
URL:            http://itstool.org/
VCS:            git:https://github.com/itstool/itstool
#!RemoteAsset:  sha256:6b9a7cd29a12bb95598f5750e8763cee78836a1a207f85b74d8b3275b27e87ca
Source0:        http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildSystem:    autotools

Patch0001:      0001-Fix-insufficiently-quoted-regular-expressions.patch
Patch0002:      0002-Switch-from-libxml2-to-lxml.patch

BuildOption(prep):  -n %{name}-%{version} -p1

BuildRequires:  python3dist(lxml)
BuildRequires:  pkgconfig(python3)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Requires:       python3dist(lxml)

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages

%conf -p
autoreconf -fi
export PYTHON=%{__python3}

%files
%license COPYING COPYING.GPL3
%doc ChangeLog NEWS
%{_bindir}/itstool
%{_datadir}/itstool
%{_mandir}/man1/*

%changelog
%autochangelog
