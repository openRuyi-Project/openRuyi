# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond asciidoc 0

Name:           libXi
Version:        1.8.2
Release:        %autorelease
Summary:        X.Org X11 libXi runtime library
License:        MIT
URL:            https://www.x.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxi.git
#!RemoteAsset
Source0:        https://www.x.org/releases/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-specs
%if %{with asciidoc}
BuildOption(conf):  --with-asciidoc=yes
%else
BuildOption(conf):  --with-asciidoc=no
%endif

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  xmlto
%if %{with asciidoc}
BuildRequires:  asciidoc
%endif

Requires:       libX11

%description
X.Org X11 libXi runtime library

%package        devel
Summary:        X.Org X11 libXi development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
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
%autochangelog
