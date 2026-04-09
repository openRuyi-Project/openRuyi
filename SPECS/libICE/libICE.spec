# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libICE
Version:        1.1.2
Release:        %autorelease
Summary:        X.Org X11 ICE runtime library
License:        MIT-open-group
URL:            http://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libice.git
#!RemoteAsset
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-fop
BuildOption(conf):  --without-xmlto

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)

%description
The X.Org X11 ICE (Inter-Client Exchange) runtime library.

%package        devel
Summary:        X.Org X11 ICE development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The X.Org X11 ICE (Inter-Client Exchange) development package.

%files
%{_libdir}/libICE.so.*
%doc AUTHORS ChangeLog COPYING

%files devel
%{_includedir}/X11/ICE
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc
%{_docdir}/%{name}/*.xml

%changelog
%autochangelog
