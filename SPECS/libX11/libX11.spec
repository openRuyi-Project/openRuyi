# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libX11
Version:        1.8.13
Release:        %autorelease
Summary:        Core X11 protocol client library
License:        MIT
URL:            https://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libx11.git
#!RemoteAsset:  sha256:69606f485c2c07c14ef64f75b7bb326d48587af33795d9ab3e607c0b5f94f11c
Source0:        https://www.x.org/releases/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules

BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(xcb) >= 1.11.1
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto) >= 1.2.0
BuildRequires:  pkgconfig(xorg-macros) >= 1.15
BuildRequires:  pkgconfig(xproto) >= 7.0.25
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  xmlto >= 0.0.22
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Core X11 protocol client library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
X.Org X11 libX11 development package

%package        doc
Summary:        Documentation for %{name}

%description    doc
The %{name}-doc package contains documentation for the %{name} library.

%conf -p
autoreconf -fiv

%install -a
mkdir -p %{buildroot}/var/cache/libX11/compose

# Don't install Xcms.txt
find %{buildroot} -name 'Xcms.txt' -delete
rm -rf %{buildroot}%{_docdir}

%files
%doc AUTHORS
%license COPYING
%{_libdir}/*.so.*
%{_datadir}/X11/locale/*
%{_datadir}/X11/XErrorDB
%dir /var/cache/libX11
%dir /var/cache/libX11/compose

%files devel
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/X11/*.h
%{_libdir}/pkgconfig/x11-xcb.pc
%{_libdir}/pkgconfig/x11.pc
%{_includedir}/X11/extensions/XKBgeom.h

%files doc
%{_mandir}/man3/*.3*
%{_mandir}/man5/*.5*

%changelog
%autochangelog
