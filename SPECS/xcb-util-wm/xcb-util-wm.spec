# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcb-util-wm
Version:        0.4.2
Release:        %autorelease
Summary:        XCB utility module for client- and WM-side ICCCM helpers
License:        MIT
URL:            http://xcb.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxcb-wm.git
#!RemoteAsset
Source:         http://xorg.freedesktop.org/releases/individual/xcb/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(install):  DESTDIR="%{buildroot}"

BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xorg-macros) >= 1.6.0

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- icccm: Both client and window-manager helpers for ICCCM.

%package        devel
Summary:        Development files for the XCB EWMH/ICCCM utility modules
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in libxcb-icccm4/ewmh2.

%files
%license COPYING
%doc NEWS ChangeLog
%{_libdir}/libxcb-ewmh.so.2*
%{_libdir}/libxcb-icccm.so.4*

%files devel
%{_includedir}/xcb/*.h
%{_libdir}/libxcb-ewmh.so
%{_libdir}/libxcb-icccm.so
%{_libdir}/pkgconfig/xcb-ewmh.pc
%{_libdir}/pkgconfig/xcb-icccm.pc

%changelog
%autochangelog
