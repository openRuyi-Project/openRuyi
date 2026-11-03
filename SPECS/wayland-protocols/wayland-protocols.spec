# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond test 1

Name:           wayland-protocols
Version:        1.50
Release:        %autorelease
Summary:        Wayland protocols that add functionality not available in the core protocol
License:        MIT
URL:            https://gitlab.freedesktop.org/wayland/wayland-protocols
#!RemoteAsset:  sha256:dc5899a21274fd03d06472a753d1954ab30ecc6af372105d72d472ba17a65705
Source0:        https://gitlab.freedesktop.org/wayland/wayland-protocols/-/archive/%{version}/wayland-protocols-%{version}.tar.bz2
BuildSystem:    meson

%if %{with test}
BuildOption(conf):  -Dtests=true
%else
BuildOption(conf):  -Dtests=false
%endif

BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig
%if %{with test}
BuildRequires:  python3
BuildRequires:  gcc
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
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
%autochangelog
