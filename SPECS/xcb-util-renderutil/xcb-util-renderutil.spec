# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcb-util-renderutil
Version:        0.3.10
Release:        %autorelease
Summary:        XCB utility module for the Render extension
License:        MIT
URL:            http://xcb.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxcb-render-util.git
#!RemoteAsset
Source0:        http://xcb.freedesktop.org/dist/xcb-util-renderutil-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-proto) >= 1.6
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xorg-macros) >= 1.6.0

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- renderutil: Convenience functions for the Render extension.

%package        devel
Summary:        Development files for the XCB Render utility module
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in %lname.

%files
%{_libdir}/libxcb-render-util.so.*

%files devel
%_includedir/xcb
%{_libdir}/libxcb-render-util.so
%{_libdir}/pkgconfig/xcb-renderutil.pc

%changelog
%autochangelog
