# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond autoreconf 1

Name:           bdftopcf
Version:        1.1.2
Release:        %autorelease
Summary:        Font compiler for the X server and font server
License:        MIT
URL:            https://www.x.org/wiki/
VCS:            git:https://gitlab.freedesktop.org/xorg/util/bdftopcf
#!RemoteAsset:  sha256:bc60be5904330faaa3ddd2aed7874bee2f29e4387c245d6787552f067eb0523a
Source0:        http://xorg.freedesktop.org/releases/individual/util/bdftopcf-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  make
%if %{with autoreconf}
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(xorg-macros)
%endif
BuildRequires:  pkgconfig(xfont2)

%description
bdftopcf is a font compiler for the X server and font server. Fonts
in Portable Compiled Format can be read by any architecture, although
the file is structured to allow one particular architecture to read
them directly without reformatting. This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%conf -p
%if %{with autoreconf}
autoreconf -fiv
%endif

%files
%license COPYING
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*

%changelog
%autochangelog
