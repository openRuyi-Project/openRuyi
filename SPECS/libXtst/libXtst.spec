# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXtst
Version:        1.2.5
Release:        %autorelease
Summary:        X.Org X11 libXtst runtime library
License:        MIT
URL:            https://www.x.org
#!RemoteAsset
Source0:         https://www.x.org/releases/individual/lib/%{name}-%{version}.tar.xz

BuildSystem:    autotools

BuildOption(conf): --disable-static

Requires:       libX11 >= 1.6
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xext) >= 1.0.99.4
BuildRequires:  pkgconfig(xextproto) >= 7.0.99.3
BuildRequires:  pkgconfig(recordproto) >= 1.13.99.1
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(xi)

%description
X.Org X11 libXtst runtime library

%package devel
Summary:        X.Org X11 libXtst development package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
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
%{?autochangelog}
