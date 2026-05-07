# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXinerama
Version:        1.1.6
Release:        %autorelease
Summary:        X.Org X11 libXinerama runtime library
License:        MIT AND MIT-open-group AND X11
URL:            https://gitlab.freedesktop.org/xorg/lib/libxinerama
#!RemoteAsset:  sha256:d00fc1599c303dc5cbc122b8068bdc7405d6fcb19060f4597fc51bd3a8be51d7
Source0:        http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  util-macros
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
The Xinerama Library is an X11 extension that provides multi-head support.
It allows applications to query the X server for information about the
physical screens attached to the system.

%package        devel
Summary:        X.Org X11 libXinerama development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
X.Org X11 libXinerama development package.

%conf -p
autoreconf -fiv

%files
%doc COPYING
%{_libdir}/libXinerama.so.1*

%files devel
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/Xinerama.h
%{_includedir}/X11/extensions/panoramiXext.h

%changelog
%autochangelog
