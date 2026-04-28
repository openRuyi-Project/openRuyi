# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXpresent
Version:        1.0.2
Release:        %autorelease
Summary:        A Xlib-compatible API for the Present extension
License:        MIT
URL:            https://www.x.org/wiki/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxpresent
#!RemoteAsset:  sha256:4e5b21b4812206a4b223013606ae31170502c1043038777a1ef8f70c09d37602
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXpresent-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  util-macros
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(presentproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)

%description
This package contains header files and documentation for the Present
extension.  Library and server implementations are separate.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/libXpresent.so.1
%{_libdir}/libXpresent.so.1.0.0

%files devel
%{_includedir}/X11/extensions/Xpresent.h
%{_libdir}/libXpresent.so
%{_libdir}/pkgconfig/xpresent.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
