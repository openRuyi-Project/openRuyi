# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXau
Version:        1.0.12
Release:        %autorelease
Summary:        Sample Authorization Protocol for X
License:        MIT-open-group
URL:            http://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxau
#!RemoteAsset
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  util-macros
BuildRequires:  pkgconfig
BuildRequires:  xorgproto

%description
This is a very simple mechanism for providing individual access to an X Window
System display. It uses existing core protocol and library hooks for specifying
authorization data in the connection setup block to restrict use of the display
to only those clients that show that they know a server-specific key
called a "magic cookie".

%package        devel
Summary:        Development files for %{name}
BuildRequires:  xorgproto
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xorgproto
Requires:       pkgconfig

%description    devel
X.Org X11 libXau development package

%files
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXau.so.*

%files devel
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_libdir}/pkgconfig/xau.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
