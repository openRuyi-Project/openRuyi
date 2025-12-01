# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXft
Version:        2.3.8
Release:        %autorelease
Summary:        X.Org X11 libXft runtime library
License:        HPND-sell-variant
URL:            https://xorg.freedesktop.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxft
#!RemoteAsset
Source0:        %{url}/releases/individual/lib/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        %{url}/releases/individual/lib/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)

%description
X.Org X11 libXft runtime library

%package        devel
Summary:        X.Org X11 libXft development package
Requires:       %{name} = %{version}-%{release}

%description    devel
X.Org X11 libXft development package

%conf -p
autoconf -fiv

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc AUTHORS COPYING README.md ChangeLog
%{_libdir}/libXft.so.2*

%files devel
%dir %{_includedir}/X11/Xft
%{_includedir}/X11/Xft/Xft.h
%{_includedir}/X11/Xft/XftCompat.h
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%{_mandir}/man3/Xft*.3*

%changelog
%{?autochangelog}
