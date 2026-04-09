# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hdf5
Version:        2.0.0
Release:        %autorelease
Summary:        A general purpose library and file format for storing scientific data
License:        BSD-3-Clause
URL:            https://github.com/HDFGroup/hdf5/
#!RemoteAsset
Source0:        https://github.com/HDFGroup/hdf5/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DBUILD_STATIC_LIBS=OFF
BuildOption(conf):  -DHDF5_BUILD_HL_LIB=ON
BuildOption(conf):  -DHDF5_BUILD_FORTRAN=OFF
BuildOption(conf):  -DHDF5_BUILD_CPP_LIB=ON
BuildOption(conf):  -DHDF5_INSTALL_BIN_DIR=%{_bindir}
BuildOption(conf):  -DHDF5_INSTALL_LIB_DIR=%{_libdir}
BuildOption(conf):  -DHDF5_INSTALL_INCLUDE_DIR=%{_includedir}
BuildOption(conf):  -DHDF5_INSTALL_DATA_DIR=%{_datadir}
BuildOption(conf):  -DHDF5_INSTALL_CMAKE_DIR=%{_libdir}/cmake/hdf5
BuildOption(conf):  -DHDF5_ENABLE_Z_LIB_SUPPORT=ON
BuildOption(conf):  -DHDF5_BUILD_EXAMPLES=OFF
BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DCMAKE_SKIP_RPATH=ON
BuildOption(conf):  -DHDF5_ENABLE_SZIP_SUPPORT=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libaec-devel

%description
HDF5 is a general purpose library and file format for storing scientific data.

%package        devel
Summary:        HDF5 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libaec-devel
Requires:       pkgconfig(zlib)

%description    devel
HDF5 development headers and libraries.

%files
%doc ACKNOWLEDGMENTS README.md
%{_datadir}/CHANGELOG.md
%{_datadir}/LICENSE
%{_bindir}/h5clear
%{_bindir}/h5copy
%{_bindir}/h5debug
%{_bindir}/h5diff
%{_bindir}/h5delete
%{_bindir}/h5dump
%{_bindir}/h5format_convert
%{_bindir}/h5import
%{_bindir}/h5jam
%{_bindir}/h5ls
%{_bindir}/h5mkgrp
%{_bindir}/h5perf_serial
%{_bindir}/h5repack
%{_bindir}/h5repart
%{_bindir}/h5stat
%{_bindir}/h5unjam
%{_bindir}/h5watch
%{_libdir}/*.so.*

%files devel
%{_datadir}/USING_HDF5_CMake.txt
%{_bindir}/h5c++*
%{_bindir}/h5cc*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.settings
%{_libdir}/cmake/hdf5
%{_libdir}/pkgconfig/hdf5.pc
%{_libdir}/pkgconfig/hdf5_cpp.pc
%{_libdir}/pkgconfig/hdf5_hl.pc
%{_libdir}/pkgconfig/hdf5_hl_cpp.pc

%changelog
%autochangelog
