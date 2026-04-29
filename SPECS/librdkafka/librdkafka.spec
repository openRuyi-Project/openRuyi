# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           librdkafka
Version:        2.14.1
Release:        %autorelease
Summary:        Apache Kafka C/C++ client library
License:        BSD-2-Clause AND BSD-3-Clause AND MIT AND Zlib AND Apache-2.0
URL:            https://github.com/confluentinc/librdkafka
#!RemoteAsset:  sha256:bb246e754dee3560e9b42bf4e844dc05de4b146a3cae937e36301ffacdc456e7
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/librdkafka-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DRDKAFKA_BUILD_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DRDKAFKA_BUILD_TESTS:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
librdkafka is a C library implementation of the Apache Kafka protocol,
providing Producer, Consumer and Admin clients. It was designed with message
delivery reliability and high performance in mind.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, shared library symlinks, pkg-config
files and CMake config files needed to develop applications that link against
%{name}.

%files
%doc CHANGELOG.md CONFIGURATION.md INTRODUCTION.md README.md
%license LICENSE LICENSES.txt
%license LICENSE.cjson LICENSE.crc32c LICENSE.fnv1a LICENSE.hdrhistogram
%license LICENSE.lz4 LICENSE.murmur2 LICENSE.nanopb LICENSE.opentelemetry
%license LICENSE.pycrc LICENSE.queue LICENSE.regexp LICENSE.snappy
%license LICENSE.tinycthread LICENSE.wingetopt
%{_libdir}/librdkafka.so.*
%{_libdir}/librdkafka++.so.*

%files devel
%{_includedir}/librdkafka/
%{_libdir}/librdkafka.so
%{_libdir}/librdkafka++.so
%{_libdir}/pkgconfig/rdkafka.pc
%{_libdir}/pkgconfig/rdkafka++.pc
%{_libdir}/cmake/RdKafka/

%changelog
%autochangelog
