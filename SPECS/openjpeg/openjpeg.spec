# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openjpeg
Version:        2.5.4
Release:        %autorelease
Summary:        C-Library for JPEG 2000
License:        BSD-2-Clause AND MIT
URL:            https://github.com/uclouvain/openjpeg
#!RemoteAsset
Source0:        https://github.com/uclouvain/openjpeg/archive/v%{version}/openjpeg-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DOPENJPEG_INSTALL_LIB_DIR=%{_lib}
BuildOption(conf):  -DBUILD_DOC=ON
BuildOption(conf):  -DBUILD_STATIC_LIBS=OFF
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  jbigkit-devel
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

%description
The OpenJPEG library is an open-source JPEG 2000 library.
This package contains the shared libraries.

%package        devel
Summary:        Development files for OpenJPEG 2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for OpenJPEG 2.

%files
%license LICENSE
%doc AUTHORS.md NEWS.md README.md THANKS.md
%{_libdir}/libopenjp2.so.*
%{_mandir}/man3/libopenjp2.3*
%{_bindir}/opj_compress
%{_bindir}/opj_decompress
%{_bindir}/opj_dump
%{_mandir}/man1/opj_compress.1*
%{_mandir}/man1/opj_decompress.1*
%{_mandir}/man1/opj_dump.1*

%files devel
%dir %{_includedir}/openjpeg-2.5/
%{_includedir}/openjpeg-2.5/openjpeg.h
%{_includedir}/openjpeg-2.5/opj_config.h
%{_libdir}/libopenjp2.so
%{_libdir}/cmake/openjpeg-2.5/
%{_libdir}/pkgconfig/libopenjp2.pc
%{_datadir}/doc/

%changelog
%autochangelog
