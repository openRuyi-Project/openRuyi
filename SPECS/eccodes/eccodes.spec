# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           eccodes
Version:        2.48.0
Release:        %autorelease
Summary:        Library for decoding and encoding GRIB and BUFR messages
License:        Apache-2.0
URL:            https://github.com/ecmwf/eccodes
#!RemoteAsset:  sha256:c7552ce91ebd868f65e43f1f4dacfd9d3a642e257b5132eb304679d1f168b960
Source0:        %{url}/archive/refs/tags/%{version}/%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  ecbuild
BuildRequires:  gcc-fortran
BuildRequires:  libaec-devel

%description
ecCodes provides an application programming interface and tools for decoding
and encoding weather data in GRIB and BUFR formats.

%package        devel
Summary:        Development files for ecCodes
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and build-system metadata for developing applications with ecCodes.

%conf -p
# https://github.com/ecmwf/eccodes/issues/514
export FFLAGS=`echo %{build_fflags} | sed -e "s/-Wformat//g"`

%files
%doc README.md
%license LICENSE
%{_bindir}/bufr_compare
%{_bindir}/bufr_compare_dir
%{_bindir}/bufr_copy
%{_bindir}/bufr_count
%{_bindir}/bufr_dump
%{_bindir}/bufr_filter
%{_bindir}/bufr_get
%{_bindir}/bufr_index_build
%{_bindir}/bufr_ls
%{_bindir}/bufr_set
%{_bindir}/codes_bufr_filter
%{_bindir}/codes_config
%{_bindir}/codes_count
%{_bindir}/codes_export_resource
%{_bindir}/codes_info
%{_bindir}/codes_parser
%{_bindir}/codes_split_file
%{_bindir}/grib2ppm
%{_bindir}/grib_compare
%{_bindir}/grib_copy
%{_bindir}/grib_count
%{_bindir}/grib_dump
%{_bindir}/grib_filter
%{_bindir}/grib_get
%{_bindir}/grib_get_data
%{_bindir}/grib_histogram
%{_bindir}/grib_index_build
%{_bindir}/grib_ls
%{_bindir}/grib_set
%{_bindir}/gts_compare
%{_bindir}/gts_copy
%{_bindir}/gts_count
%{_bindir}/gts_dump
%{_bindir}/gts_filter
%{_bindir}/gts_get
%{_bindir}/gts_ls
%{_datadir}/eccodes/
%{_libdir}/libeccodes.so
%{_libdir}/libeccodes_f90.so

%files devel
%{_includedir}/eccodes.h
%{_includedir}/eccodes.mod
%{_includedir}/eccodes_config.h
%{_includedir}/eccodes_ecbuild_config.h
%{_includedir}/eccodes_version.h
%{_includedir}/eccodes_windef.h
%{_includedir}/grib_api.h
%{_includedir}/grib_api.mod
%{_libdir}/cmake/eccodes/
%{_libdir}/pkgconfig/eccodes.pc
%{_libdir}/pkgconfig/eccodes_f90.pc

%changelog
%autochangelog
