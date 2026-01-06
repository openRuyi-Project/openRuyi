# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcursor-themes
Version:        1.0.7
Release:        %autorelease
Summary:        Default set of cursor themes for X
License:        X11
URL:            http://xorg.freedesktop.org/
# Seems to no git repo.
#!RemoteAsset:  sha256:95bae8f48823d894a05bf42dfbf453674ab7dbdeb11e2bc079e8525ad47378c8
Source0:        http://xorg.freedesktop.org/releases/individual/data/xcursor-themes-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xcursorgen
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xorg-macros)

%description
This is a default set of cursor themes for use with libXcursor, originally
created for the XFree86 Project, and now shipped as part of the X.Org software
distribution.

%files
%license COPYING
%doc ChangeLog README.md
%{_datadir}/icons/handhelds/
%{_datadir}/icons/redglass/
%{_datadir}/icons/whiteglass/

%changelog
%{?autochangelog}
