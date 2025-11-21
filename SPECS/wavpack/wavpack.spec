# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wavpack
Version:        5.8.1
Release:        %autorelease
Summary:        Hybrid Lossless Audio Compression Format
License:        BSD-3-Clause
URL:            https://www.wavpack.com/
#!RemoteAsset
Source:         https://github.com/dbry/WavPack/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DBUILD_SHARED_LIBS=ON

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  gcc

%description
WavPack is an open audio compression format providing lossless, high-quality
lossy, and unique hybrid compression modes. This package contains the
command-line tools.

%package        devel
Summary:        Development files for wavpack, an audio compression format
Requires:       %{name}%{?_isa} = %{version}
Requires:       glibc-devel

%description    devel
This package contains the header files, libraries, and documentation
needed to develop applications that use the WavPack library.

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/wavpack
%{_bindir}/wvgain
%{_bindir}/wvunpack
%{_bindir}/wvtag
%{_mandir}/man1/*
%{_libdir}/libwavpack.so.1*

%files devel
%doc doc/*
%{_libdir}/cmake/WavPack
%{_includedir}/wavpack
%{_libdir}/libwavpack.so
%{_libdir}/pkgconfig/wavpack.pc

%changelog
%{?autochangelog}
