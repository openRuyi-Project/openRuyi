# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fdk-aac
Version:        2.0.3
Release:        %autorelease
Summary:        Fraunhofer FDK AAC Codec Library (Free Version)
License:        FDK-AAC
URL:            https://github.com/mstorsjo/fdk-aac
#!RemoteAsset
Source:         https://github.com/mstorsjo/fdk-aac/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-silent-rules
BuildOption(conf): --disable-static

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
This is a modified version of the Fraunhofer FDK AAC Codec Library for Android.
It implements MPEG Advanced Audio Coding ("AAC") encoding and decoding.
This version has been stripped of patented code to be redistributable.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%files
%doc ChangeLog
%license NOTICE
%{_libdir}/*.so.2*

%files devel
%doc documentation/*.pdf
%{_includedir}/fdk-aac/
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc

%changelog
%{?autochangelog}
