# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcb-util
Version:        0.4.1
Release:        %autorelease
Summary:        XCB utility modules
License:        MIT
URL:            https://xcb.freedesktop.org/
VCS:	        git:https://gitlab.freedesktop.org/xorg/lib/libxcb-util.git
#!RemoteAsset:  sha256:5abe3bbbd8e54f0fa3ec945291b7e8fa8cfd3cccc43718f8758430f94126e512
Source:         https://xcb.freedesktop.org/dist/xcb-util-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xproto) >= 7.0.8

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

Included in this package are:

- atom: Standard core X atom constants and atom caching.
- aux: Convenient access to connection setup and some core requests.
- event: Callback X event handling.

%package        devel
Summary:        Development files for the XCB utility modules
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

This package contains the development headers for the library found
in %{name}.

%files
%{_libdir}/libxcb-util.so.1*

%files devel
%license COPYING
%doc README.md
%{_includedir}/xcb
%{_libdir}/libxcb-util.so
%{_libdir}/pkgconfig/xcb-atom.pc
%{_libdir}/pkgconfig/xcb-aux.pc
%{_libdir}/pkgconfig/xcb-event.pc
%{_libdir}/pkgconfig/xcb-util.pc

%changelog
%autochangelog
