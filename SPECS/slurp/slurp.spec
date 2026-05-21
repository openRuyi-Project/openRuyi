# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           slurp
Version:        1.5.0
Release:        %autorelease
Summary:        Select a region in a Wayland compositor
License:        MIT
URL:            https://github.com/emersion/slurp
#!RemoteAsset:  sha256:eeb282b2adc8db5614b852596340b69da6f3954cf6cfbdc4392da509c934208a
Source0:        https://github.com/emersion/slurp/releases/download/v%{version}/slurp-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc

%description
Select a region in a Wayland compositor and
print it to the standard output. Works well with grim.

%files
%doc README.md
%license LICENSE
%{_bindir}/slurp
%{_mandir}/man1/slurp.1*

%changelog
%autochangelog
