# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXtst
Version:        1.2.5
Release:        %autorelease
Summary:        X.Org X11 libXtst runtime library
License:        MIT
URL:            https://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxtst.git
#!RemoteAsset
Source0:        https://www.x.org/releases/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(xi)

Requires:       libX11

%description
X.Org X11 libXtst runtime library

%package        devel
Summary:        X.Org X11 libXtst development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
X.Org X11 libXtst development package

%files
%license COPYING
%{_libdir}/libXtst.so.*

%files devel
%doc %{_docdir}/libXtst/*
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
%{_mandir}/man3/XTest*.3*

%changelog
%autochangelog
