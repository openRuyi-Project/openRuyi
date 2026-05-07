# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXext
Version:        1.3.7
Release:        %autorelease
Summary:        X.Org X11 libXext runtime library
License:        MIT
URL:            https://xorg.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxext.git
#!RemoteAsset:  sha256:6564608dc3b816b0cfddf0c7ddc62bc579055dd70b2f28113a618df2acb64189
Source0:        https://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto) >= 7.0.13
BuildRequires:  xmlto
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Requires:       libX11

%description
X.Org X11 libXext runtime library

%package        devel
Summary:        X.Org X11 libXext development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
X.Org X11 libXext development package

%package        doc
Summary:        Documentation for %{name}

%description    doc
The %{name}-doc package contains documentation for the %{name} library.

%conf -p
autoreconf -fiv

%files
%doc AUTHORS
%license COPYING
%{_libdir}/libXext.so.*

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXext.so
%{_libdir}/pkgconfig/xext.pc

%files doc
%{_docdir}/libXext/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
