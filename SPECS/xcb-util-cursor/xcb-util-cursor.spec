# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcb-util-cursor
Version:        0.1.6
Release:        %autorelease
Summary:        XCB cursor library (libxcursor port)
License:        MIT
URL:            http://xcb.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxcb-cursor.git
#!RemoteAsset
Source0:        http://xcb.freedesktop.org/dist/xcb-util-cursor-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-proto) >= 1.6
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xorg-macros) >= 1.6.0

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.
Included in this package is:
- cursor: port of libxcursor

%package        devel
Summary:        Development files for the XCB cursor library (libxcursor port)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in %{name}.

%conf -p
autoreconf -fiv

%files
%{_libdir}/libxcb-cursor.so.*

%files devel
%{_includedir}/xcb
%{_libdir}/libxcb-cursor.so
%{_libdir}/pkgconfig/xcb-cursor.pc

%changelog
%autochangelog
