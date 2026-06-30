# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           menu-cache
Version:        1.1.1
Release:        %autorelease
Summary:        Caching mechanism for freedesktop.org compliant menus
License:        LGPL-2.1-or-later
URL:            https://github.com/lxde/menu-cache
VCS:            git:https://github.com/lxde/menu-cache.git
#!RemoteAsset:  sha256:e8af90467df271c3c8700c840ca470ca2915699c6f213c502a87d74608748f08
Source0:        https://github.com/lxde/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libfm-extra)

%description
Menu-cache is a caching mechanism for freedesktop.org compliant menus that
speeds up parsing of menu entries. It is used by LXDE components such as
LXPanel and LXLauncher.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(glib-2.0)

%description    devel
The %{name}-devel package contains headers, pkgconfig metadata, and linker
files for developing applications that use %{name}.

%conf -p
# GitHub tag archives do not include gtk-doc helper files needed by autoreconf.
mkdir -p m4
gtkdocize --copy
autoreconf -fiv

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libexecdir}/menu-cache/menu-cache-gen
%{_libexecdir}/menu-cache/menu-cached
%{_libdir}/libmenu-cache.so.*

%files devel
%{_includedir}/menu-cache/
%{_libdir}/libmenu-cache.so
%{_libdir}/pkgconfig/libmenu-cache.pc

%changelog
%autochangelog
