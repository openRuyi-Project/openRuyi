# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXt
Version:        1.3.1
Release:        %autorelease
Summary:        X.Org X11 libXt runtime library
License:        MIT
URL:            https://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxt.git
#!RemoteAsset
Source0:        https://www.x.org/releases/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc

Requires:       libX11

%description
X.Org X11 libXt runtime library.

%package        devel
Summary:        X.Org X11 libXt development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
X.Org X11 libXt development package

%conf -p
autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"

%install -a
mkdir -p -m 0755 %{buildroot}%{_datadir}/X11/app-defaults

%files
%license COPYING
%{_libdir}/*.so.*
%dir %{_datadir}/X11/app-defaults

%files devel
%{_includedir}/X11/*.h
%{_libdir}/*.so
%if %{with static}
%{_libdir}/*.a
%endif
%{_libdir}/pkgconfig/xt.pc
%{_mandir}/man3/*.3*
%doc %{_datadir}/doc/*

%changelog
%{?autochangelog}
