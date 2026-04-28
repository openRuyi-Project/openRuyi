# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <uwu@icenowy.me>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xcb-util-keysyms
Version:        0.4.1
Release:        %autorelease
Summary:        X Fixes library
License:        MIT
URL:            https://www.x.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxcb-keysyms.git
#!RemoteAsset:  sha256:7c260a5294412aed429df1da2f8afd3bd07b7cba3fec772fba15a613a6d5c638
Source0:        https://www.x.org/archive/individual/lib/xcb-util-keysyms-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xproto) >= 7.0.8

%description
XCB utility library for translating keysyms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
%{name} development package

%files
%license COPYING
%doc NEWS
%{_libdir}/libxcb-keysyms.so.*

%files devel
%{_includedir}/xcb/xcb_keysyms.h
%{_libdir}/pkgconfig/xcb-keysyms.pc
%{_libdir}/libxcb-keysyms.so

%changelog
%autochangelog
