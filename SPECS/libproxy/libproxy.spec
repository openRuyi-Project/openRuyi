# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libproxy
Version:        0.5.11
Release:        %autorelease
Summary:        A library for proxy configuration management
License:        LGPL-2.1-or-later
URL:            https://libproxy.github.io/libproxy/
VCS:            git:https://github.com/libproxy/libproxy
#!RemoteAsset
Source:         https://github.com/libproxy/libproxy/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dconfig-gnome=false
BuildOption(conf):  -Dconfig-kde=false
BuildOption(conf):  -Dconfig-osx=false
BuildOption(conf):  -Dconfig-windows=false
BuildOption(conf):  -Dintrospection=true
BuildOption(conf):  -Dtests=true
BuildOption(conf):  -Dvapi=true

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  vala
BuildRequires:  pkgconfig(duktape)
BuildRequires:  pkgconfig(gio-2.0) >= 2.71.3
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(python3)

%description
libproxy provides a library for transparently handling proxy settings,
dynamically adjusting to changing network topologies.

%package        devel
Summary:        Development files for libproxy
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and documentation for
developing applications that use libproxy.

%files
%license COPYING
%doc README.md
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Libproxy-1.0.typelib
%{_libdir}/libproxy.so.*
%dir %{_libdir}/libproxy
%{_libdir}/libproxy/libpxbackend-1.0.so
%{_bindir}/proxy
%{_mandir}/man8/proxy.8*

%files devel
%{_docdir}/libproxy-1.0/
%{_includedir}/libproxy/
%{_libdir}/libproxy.so
%{_libdir}/pkgconfig/libproxy-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Libproxy-1.0.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/libproxy-1.0.deps
%{_datadir}/vala/vapi/libproxy-1.0.vapi

%changelog
%autochangelog
