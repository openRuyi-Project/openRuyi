# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libaec
Version:        1.1.4
Release:        %autorelease
Summary:        Adaptive Entropy Coding library
License:        BSD-2-Clause
URL:            https://gitlab.dkrz.de/k202009/libaec
#!RemoteAsset
Source0:        https://gitlab.dkrz.de/k202009/libaec/-/archive/v%{version}/libaec-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=ON
BuildOption(conf):  -DBUILD_STATIC_LIBS=ON

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  make

%description
Libaec provides fast loss-less compression of 1 up to 32 bit wide
signed or unsigned integers. It includes a free drop-in replacement
for the SZIP library.

%package        devel
Summary:        Development files for libaec
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libaec.

%files
%doc README.md README.SZIP CHANGELOG.md
%license LICENSE.txt doc/patent.txt
%{_libdir}/libaec.so.0*
%{_libdir}/libsz.so.2*

%files devel
%{_includedir}/*.h
%{_libdir}/libaec.so
%{_libdir}/libsz.so
# keep the static library as hdf5 needs it.
%{_libdir}/libaec.a
%{_libdir}/libsz.a
%{_libdir}/cmake/libaec/

%changelog
%autochangelog
