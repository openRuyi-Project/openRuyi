# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXfixes
Version:        6.0.2
Release:        %autorelease
Summary:        X Fixes library
License:        MIT
URL:            https://www.x.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxfixes.git
#!RemoteAsset
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(fixesproto) >= 6.0
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.22

%description
X Fixes library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
libXfixes development package

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libXfixes.so.*

%files devel
%{_includedir}/X11/extensions/Xfixes.h
%{_libdir}/pkgconfig/xfixes.pc
%{_libdir}/libXfixes.so
%if %{with static}
%{_libdir}/*.a
%endif
%{_mandir}/man3/*

%changelog
%{?autochangelog}
