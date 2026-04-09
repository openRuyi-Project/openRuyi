# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# last updated: 2021.
%global libargparse_commit  ee74d1b53bd680748af14e737378de57e2a0a954

Name:           libavif
Version:        1.4.0
Release:        %autorelease
Summary:        Library for encoding and decoding .avif files
License:        BSD-2-Clause AND IJG AND Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/AOMediaCodec/libavif
#!RemoteAsset:  sha256:713e2b998ca0bf5473fe4624afdbc7fa9f6e4799dd414020fe67d56f6997bf4e
Source0:        https://github.com/AOMediaCodec/libavif/archive/refs/tags/v%{version}.tar.gz
#!RemoteAsset:  sha256:7727b0498851e5b6a6fcd734eb667a8a231897e2c86a357aec51cc0664813060
Source1:        https://github.com/maryla-uc/libargparse/archive/%{libargparse_commit}/libargparse-%{libargparse_commit}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DAVIF_BUILD_APPS=ON
BuildOption(conf):  -DAVIF_CODEC_DAV1D=SYSTEM
BuildOption(conf):  -DAVIF_LIBXML2=SYSTEM
BuildOption(conf):  -DAVIF_LIBYUV=OFF
BuildOption(conf):  -DAVIF_BUILD_TESTS=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)

%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format.

%package        devel
Summary:        Development files for libavif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package holds the development files for libavif.

%prep -a
mkdir -p ext/libargparse
tar --strip-components=1 -xvf %{SOURCE1} -C ext/libargparse

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/avifdec
%{_bindir}/avifenc
%{_bindir}/avifgainmaputil
%{_libdir}/libavif.so.*

%files devel
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/
%{_libdir}/pkgconfig/libavif.pc

%changelog
%autochangelog
