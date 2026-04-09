# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXScrnSaver
Version:        1.2.5
Release:        %autorelease
Summary:        X.Org X11 libXss runtime library
License:        MIT
URL:            https://gitlab.freedesktop.org/xorg/lib/libxscrnsaver
#!RemoteAsset:  sha256:5057365f847253e0e275871441e10ff7846c8322a5d88e1e187d326de1cd8d00
Source0:        https://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  CFLAGS="%{build_cflags} -fno-strict-aliasing"

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  util-macros
BuildRequires:  pkgconfig
BuildRequires:  xorgproto
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
The X Screen Saver Extension library allows clients to query the screen
saver status and register for screen saver events.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%files
%doc COPYING README.md ChangeLog
%{_libdir}/libXss.so.*

%files devel
%{_libdir}/libXss.so
%{_libdir}/pkgconfig/xscrnsaver.pc
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/scrnsaver.h

%changelog
%autochangelog
