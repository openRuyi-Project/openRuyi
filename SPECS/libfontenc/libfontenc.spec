# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfontenc
Version:        1.1.8
Release:        %autorelease
Summary:        X11 font encoding library
License:        MIT
URL:            https://www.x.org/wiki/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libfontenc
#!RemoteAsset
Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-fontrootdir=%{_datadir}/fonts

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zlib)

%description
The libfontenc library is used by the Xorg server and other X font
tools for handling fonts with different character set encodings.

%package        devel
Summary:        Development files for the X11 font encoding library
Requires:       %{name} = %{version}-%{release}

%description    devel
The libfontenc library is used by the Xorg server and other X font
tools for handling fonts with different character set encodings.

%conf -p
autoreconf -fiv

%files
%{_libdir}/libfontenc.so.1*

%files devel
%{_includedir}/X11/*
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc

%changelog
%{?autochangelog}
