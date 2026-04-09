# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXv
Version:        1.0.13
Release:        %autorelease
Summary:        X.Org X11 libXv runtime library
License:        SMLNJ AND HPND-sell-variant
URL:            https://gitlab.freedesktop.org/xorg/lib/libXv
#!RemoteAsset:  sha256:7d34910958e1c1f8d193d828fea1b7da192297280a35437af0692f003ba03755
Source0:        http://xorg.freedesktop.org/archive/individual/lib/libXv-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  util-macros
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(x11)

%description
X.Org X11 libXv runtime library.

%package        devel
Summary:        X.Org X11 libXv development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
X.Org X11 libXv development package.

%conf -p
autoreconf -fiv

%files
%doc AUTHORS COPYING
%{_libdir}/libXv.so.1*

%files devel
%doc man/xv-library-v2.2.txt
%{_includedir}/X11/extensions/Xvlib.h
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
