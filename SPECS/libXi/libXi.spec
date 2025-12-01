# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond asciidoc 0

Name:           libXi
Version:        1.8.2
Release:        %autorelease
Summary:        X.Org X11 libXi runtime library
License:        MIT
URL:            https://www.x.org/
#!RemoteAsset
Source0:         https://www.x.org/releases/individual/lib/%{name}-%{version}.tar.xz

BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --disable-specs
%if %{with asciidoc}
BuildOption(conf):  --with-asciidoc=yes
%else
BuildOption(conf):  --with-asciidoc=no
%endif

Requires:       libX11 >= 1.6
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xext) >= 1.0.99.1
BuildRequires:  pkgconfig(xextproto) >= 7.0.3
BuildRequires:  pkgconfig(xfixes) >= 5
BuildRequires:  pkgconfig(inputproto) >= 2.3.99.1
BuildRequires:  pkgconfig(xproto) >= 7.0.13
BuildRequires:  xmlto
%if %{with asciidoc}
BuildRequires:  asciidoc
%endif

%description
X.Org X11 libXi runtime library

%package devel
Summary:        X.Org X11 libXi development package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
X.Org X11 libXi development package

%files
%license COPYING
%{_libdir}/libXi.so.*

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_mandir}/man3/*

%changelog
%{?autochangelog}
