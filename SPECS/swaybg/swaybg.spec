# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           swaybg
Version:        1.2.2
Release:        %autorelease
Summary:        Wallpaper tool for Wayland compositors
License:        MIT
URL:            https://github.com/swaywm/swaybg
#!RemoteAsset:  sha256:a6652a0060a0bea3c3318d9d03b6dddac34f6aeca01b883eef9e58281f5202a1
Source0:        https://github.com/swaywm/swaybg/releases/download/v%{version}/swaybg-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dwerror=false

BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.31
BuildRequires:  pkgconfig(wayland-scanner) >= 1.14.91
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
