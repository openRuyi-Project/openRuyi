# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond test 1

Name:           wayland-protocols
Version:        1.46
Release:        %autorelease
Summary:        Wayland protocols that add functionality not available in the core protocol
License:        MIT
URL:            ttps://gitlab.freedesktop.org/wayland/wayland-protocols
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/%{version}/wayland-protocols-%{version}.tar.bz2
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig

%if %{with test}
BuildOption(conf): -Dtests=true
BuildRequires:  python3
BuildRequires:  gcc
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
%else
BuildOption(conf): -Dtests=false
%endif

%description
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol.

%files
%license COPYING
%doc README.md
%{_datadir}/pkgconfig/wayland-protocols.pc
%{_datadir}/wayland-protocols/
%{_includedir}/wayland-protocols/

%changelog
%{?autochangelog}
