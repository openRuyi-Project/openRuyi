# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           grpc
Version:        1.75.1
Release:        %autorelease
Summary:        An HTTP/2-based Remote Procedure Call framework
License:        Apache-2.0
URL:            https://grpc.io/
#!RemoteAsset
Source:         https://github.com/grpc/grpc/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DgRPC_INSTALL:BOOL=ON
BuildOption(conf): -DgRPC_INSTALL_LIBDIR:PATH="%_lib"
BuildOption(conf): -DgRPC_INSTALL_CMAKEDIR:PATH="%_libdir/cmake/grpc"

BuildOption(conf): -DgRPC_ABSL_PROVIDER=package
BuildOption(conf): -DgRPC_CARES_PROVIDER=package
BuildOption(conf): -DgRPC_PROTOBUF_PROVIDER=package
BuildOption(conf): -DgRPC_RE2_PROVIDER=package
BuildOption(conf): -DgRPC_SSL_PROVIDER=package
BuildOption(conf): -DgRPC_ZLIB_PROVIDER=package
BuildOption(conf): -DCMAKE_CXX_STANDARD=17
BuildOption(conf): -DgRPC_BENCHMARK_PROVIDER=none
BuildOption(conf): -DgRPC_BENCHMARK_PROVIDER=OFF
BuildOption(conf): -DgRPC_BUILD_TESTS=OFF
BuildOption(conf): -DgRPC_DOWNLOAD_ARCHIVES:BOOL=OFF

BuildRequires:  abseil-cpp-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcares) >= 1.19.1
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(protobuf) >= 22
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)

%description
gRPC is a modern, open source, high-performance Remote Procedure Call (RPC)
framework that can run in any environment.

%package        devel
Summary:        Development files for gRPC
Requires:       %{name} = %{version}
Requires:       pkgconfig(libcares)
Requires:       pkgconfig(re2)

%description    devel
This package contains the libraries, header files, and tools needed to
develop applications that use the gRPC framework.

%prep -a
find . -type f -regex ".*\.py\|.*\.sh" -exec sed -i -e 's|/usr/bin/env python.*|/usr/bin/python3|' -e 's|/usr/bin/python.*|/usr/bin/python3|' {} +
rm -Rf third_party/abseil-cpp/

%install -a
rm -Rf %{buildroot}%{_datadir}/grpc/*.pem
%fdupes %{buildroot}%{_prefix}

%files
%license LICENSE
%{_libdir}/libaddress_sorting.so.*
%{_libdir}/libgpr*.so.*
%{_libdir}/libgrpc*.so.*
%{_libdir}/libutf8_range_lib.so.*
%{_libdir}/libupb*.so.*

%files devel
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/grpc/

%changelog
%{?autochangelog}
