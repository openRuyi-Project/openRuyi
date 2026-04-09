# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bdftopcf
Version:        1.1.2
Release:        %autorelease
Summary:        Font compiler for the X server and font server
License:        MIT
URL:            https://www.x.org/wiki/
VCS:            git:https://gitlab.freedesktop.org/xorg/util/bdftopcf
#!RemoteAsset
Source0:        http://xorg.freedesktop.org/releases/individual/util/bdftopcf-%{version}.tar.xz
#!RemoteAsset
Source1:        http://xorg.freedesktop.org/releases/individual/util/bdftopcf-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xorg-macros)

%description
bdftopcf is a font compiler for the X server and font server. Fonts
in Portable Compiled Format can be read by any architecture, although
the file is structured to allow one particular architecture to read
them directly without reformatting. This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%conf -p
autoreconf -fiv

%files
%license COPYING
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*

%changelog
%autochangelog
