# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <uwu@icenowy.me>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libxshmfence
Version:        1.3.3
Release:        %autorelease
Summary:        X Fixes library
License:        MIT
URL:            https://www.x.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxshmfence.git
#!RemoteAsset
Source:         https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --enable-futex
BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(xproto)

%description
X library for implementing synchornization with shared memory.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
%{name} development package

%files
%license COPYING
%{_libdir}/libxshmfence.so.*

%files devel
%{_includedir}/X11/xshmfence.h
%{_libdir}/pkgconfig/xshmfence.pc
%{_libdir}/libxshmfence.so

%changelog
%{?autochangelog}
