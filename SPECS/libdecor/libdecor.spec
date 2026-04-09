# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdecor
Version:        0.2.5
Release:        %autorelease
Summary:        Wayland client side decoration library
License:        MIT
URL:            https://gitlab.freedesktop.org/libdecor/libdecor
#!RemoteAsset
Source:         https://gitlab.freedesktop.org/libdecor/libdecor/-/releases/%{version}/downloads/libdecor-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgtk=disabled

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)

%description
Libdecor provides a small helper library for providing client side decoration
to Wayland clients.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSE
%doc README.md
%{_libdir}/libdecor-0.so.0*
%dir %{_libdir}/libdecor/
%dir %{_libdir}/libdecor/plugins-1
%{_libdir}/libdecor/plugins-1/libdecor-cairo.so
# without gtk.
# %{_libdir}/libdecor/plugins-1/libdecor-gtk.so

%files devel
%{_includedir}/libdecor-0/
%{_libdir}/libdecor-0.so
%{_libdir}/pkgconfig/libdecor-0.pc

%changelog
%autochangelog
