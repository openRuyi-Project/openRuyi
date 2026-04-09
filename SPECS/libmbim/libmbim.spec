# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmbim
Version:        1.32.0
Release:        %autorelease
Summary:        Mobile Broadband Interface Model protocol
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/mobile-broadband/libmbim/
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/mobile-broadband/libmbim/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  libxml2
BuildRequires:  python3
BuildRequires:  help2man

%description
libmbim is a library for talking to WWAN modems and devices which speak
the Mobile Broadband Interface Model protocol.

%package        devel
Summary:        Header files for adding MBIM support to applications that use glib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libmbim is a library for talking to WWAN modems and devices which speak
the Mobile Broadband Interface Model protocol.

This package contains the header and pkg-config files for developing
applications using MBIM functionality.

%files
%doc NEWS AUTHORS README.md
%license LICENSES/LGPL-2.1-or-later.txt
%{_bindir}/mbim-network
%{_bindir}/mbimcli
%{_libdir}/libmbim-glib.so.4*
%{_libdir}/girepository-1.0/Mbim-1.0.typelib
%{_libexecdir}/mbim-proxy
%{_mandir}/man1/mbim-network.1*
%{_mandir}/man1/mbimcli.1*
%{_datadir}/bash-completion/completions/mbimcli

%files devel
%{_includedir}/libmbim-glib/
%{_libdir}/pkgconfig/mbim-glib.pc
%{_libdir}/libmbim-glib.so
%{_datadir}/gir-1.0/Mbim-1.0.gir

%changelog
%autochangelog
