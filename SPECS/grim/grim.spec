# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           grim
Version:        1.5.0
Release:        %autorelease
Summary:        Grab images from a Wayland compositor
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/grim
#!RemoteAsset:  sha256:99708950205d5bfd2e769519fcb6423a9f545175a29c46c7c1cf7965afc4b8eb
Source0:        https://gitlab.freedesktop.org/emersion/grim/-/releases/v%{version}/downloads/grim-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dbash-completions=true

BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  scdoc

%description
Grab images from a Wayland compositor. Works great with slurp.

%files
%doc README.md
%license LICENSE
%{_bindir}/grim
%{_mandir}/man1/grim.1*
%{bash_completions_dir}/grim*

%changelog
%autochangelog
