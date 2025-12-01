# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lcms2
Version:        2.17
Release:        %autorelease
Summary:        Color Management Engine
License:        MIT AND GPL-3.0-or-later
URL:            https://github.com/mm2/Little-CMS
#!RemoteAsset
Source:         https://github.com/mm2/Little-CMS/archive/refs/tags/lcms%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf): -Dutils=true

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  zlib-devel

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form. LCMS2 is the current version of LCMS.
This package contains the shared library.

%package        devel
Summary:        Development files for LittleCMS
Requires:       %{name}%{?_isa} = %{version}
Provides:       littlecms-devel = %{version}

%description    devel
Development files for LittleCMS. This package contains headers and libraries
needed to build applications that use LittleCMS.

%files
%doc AUTHORS ChangeLog README.md
%license LICENSE
%{_libdir}/liblcms2.so.2*
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/lcms2*.h
%{_libdir}/liblcms2.so
%{_libdir}/pkgconfig/lcms2.pc

%changelog
%{?autochangelog}
