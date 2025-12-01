# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXfont2
Version:        2.0.7
Release:        %autorelease
Summary:        X font handling library for server and utilities
License:        MIT
URL:            https://www.x.org/wiki/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxfont
#!RemoteAsset
Source0:        http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(zlib)

%description
libXfont provides the core of the legacy X11 font system, handling
the index files (fonts.dir, fonts.alias, fonts.scale), the various
font file formats, and rasterizing them. It is used by the X servers,
the X Font Server (xfs), and some font utilities (bdftopcf for
instance), but should not be used by normal X11 clients. X11 clients
access fonts via either the new APIs in libXft, or the legacy APIs in
libX11.

%package        devel
Summary:        Development files for the X font handling library
Requires:       %{name} = %{version}-%{release}

%description devel
libXfont provides the core of the legacy X11 font system, handling
the index files (fonts.dir, fonts.alias, fonts.scale), the various
font file formats, and rasterizing them. It is used by the X servers,
the X Font Server (xfs), and some font utilities (bdftopcf for
instance), but should not be used by normal X11 clients. X11 clients
access fonts via either the new APIs in libXft, or the legacy APIs in
libX11.

%conf -p
autoreconf -fiv

%files
%license COPYING
%{_libdir}/libXfont2.so.2*

%files devel
%{_includedir}/X11/*
%{_libdir}/libXfont2.so
%{_libdir}/pkgconfig/xfont2.pc

%changelog
%{?autochangelog}
