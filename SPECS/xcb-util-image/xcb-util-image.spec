# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcb-util-image
Version:        0.4.1
Release:        %autorelease
Summary:        XCB utility module for XImage/XShmImage-like functions
License:        MIT
URL:            http://xcb.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxcb-image.git
#!RemoteAsset
Source0:        http://xcb.freedesktop.org/dist/xcb-util-image-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xorg-macros) >= 1.6.0
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.
Included in this package is:
- image: Port of Xlib's XImage and XShmImage functions.

%package        devel
Summary:        Development files for the XCB image utility module
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in %lname.

%conf -p
./autogen.sh

%files
%{_libdir}/libxcb-image.so.*

%files devel
%_includedir/xcb
%{_libdir}/libxcb-image.so
%{_libdir}/pkgconfig/xcb-image.pc

%changelog
%{?autochangelog}
