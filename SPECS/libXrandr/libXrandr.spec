# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXrandr
Version:        1.5.4
Release:        %autorelease
Summary:        X.Org X11 libXrandr runtime library
License:        MIT
URL:            https://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxrandr.git
#!RemoteAsset
Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)

Requires:       libX11

%description
X.Org X11 libXrandr runtime library

%package        devel
Summary:        X.Org X11 libXrandr development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
X.Org X11 libXrandr development package

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libXrandr.so.2*

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
