# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXdamage
Version:        1.1.7
Release:        %autorelease
Summary:        X Damage extension library
License:        MIT
URL:            https://gitlab.freedesktop.org/xorg/lib/libXdamage
#!RemoteAsset:  sha256:127067f521d3ee467b97bcb145aeba1078e2454d448e8748eb984d5b397bde24
Source0:        https://www.x.org/pub/individual/lib/libXdamage-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  util-macros
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(damageproto) >= 1.1.0

%description
The X Damage Extension allows applications to track modified regions
of drawables.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%files
%doc AUTHORS COPYING README.md ChangeLog
%{_libdir}/libXdamage.so.1*

%files devel
%{_includedir}/X11/extensions/Xdamage.h
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc

%changelog
%autochangelog
