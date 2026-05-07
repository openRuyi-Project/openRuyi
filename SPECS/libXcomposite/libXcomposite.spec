# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXcomposite
Version:        0.4.7
Release:        %autorelease
Summary:        X Composite Extension library
License:        MIT AND HPND-sell-variant
URL:            http://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libXcomposite
#!RemoteAsset:  sha256:8bdf310967f484503fa51714cf97bff0723d9b673e0eecbf92b3f97c060c8ccb
Source0:        https://www.x.org/archive/individual/lib/libXcomposite-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  util-macros
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xext)

%description
The X Composite Extension library allows clients to redirect rendering of
windows to off-screen storage.

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
%{_libdir}/libXcomposite.so.1*

%files devel
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
%{_mandir}/man3/X?omposite*.3*

%changelog
%autochangelog
