# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           swaybg
Version:        1.2.1
Release:        %autorelease
Summary:        Wallpaper tool for Wayland compositors
License:        MIT
URL:            https://github.com/swaywm/swaybg
#!RemoteAsset:  sha256:6af1fdf0e57b1cc5345febed786b761fea0e170943a82639f94cfaed7df84f8f
Source0:        https://github.com/swaywm/swaybg/releases/download/v%{version}/swaybg-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  scdoc

%description
swaybg is a wallpaper utility for Wayland compositors. It supports PNG, JPEG,
and other image formats supported by gdk-pixbuf, as well as solid colors.

%files
%doc README.md
%license LICENSE
%{_bindir}/swaybg
%{_mandir}/man1/swaybg.1*

%changelog
%autochangelog
