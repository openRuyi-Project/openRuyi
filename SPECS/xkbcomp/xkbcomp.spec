# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xkbcomp
Version:        1.5.0
Release:        %autorelease
Summary:        XKB keymap compiler
License:        MIT-open-group AND HPND-DEC
URL:            https://gitlab.freedesktop.org/xorg/app/xkbcomp
#!RemoteAsset
Source0:        https://www.x.org/pub/individual/app/xkbcomp-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
The X Keyboard Extension (XKB) keymap compiler.

%package        devel
Summary:        XKB keymap compiler development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the pkg-config file for xkbcomp.

%files
%license COPYING
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1*

%files devel
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog
%autochangelog
