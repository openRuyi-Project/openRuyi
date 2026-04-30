# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           grpc
Version:        1.80.0
Release:        %autorelease
Summary:        An HTTP/2-based Remote Procedure Call framework
License:        Apache-2.0
URL:            https://grpc.io/
VCS:            git:https://github.com/grpc/grpc
#!RemoteAsset:  sha256:38f58596277fa632064cc0719b9ece4381c8c77461cb51e9b66ca149574b7865
Source:         https://github.com/grpc/grpc/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

Patch2000:      2000-force-system-libraries-in-isolated-environments.patch

BuildOption(conf):  -DgRPC_INSTALL:BOOL=ON
BuildOption(conf):  -DgRPC_INSTALL_LIBDIR:PATH="%_lib"
BuildOption(conf):  -DgRPC_INSTALL_CMAKEDIR:PATH="%_libdir/cmake/grpc"
BuildOption(conf):  -DgRPC_ABSL_PROVIDER=package
BuildOption(conf):  -DgRPC_CARES_PROVIDER=package
BuildOption(conf):  -DgRPC_PROTOBUF_PROVIDER=package
BuildOption(conf):  -DgRPC_RE2_PROVIDER=package
BuildOption(conf):  -DgRPC_SSL_PROVIDER=package
BuildOption(conf):  -DgRPC_ZLIB_PROVIDER=package
BuildOption(conf):  -DCMAKE_CXX_STANDARD=17
BuildOption(conf):  -DgRPC_BENCHMARK_PROVIDER=none
BuildOption(conf):  -DgRPC_BENCHMARK_PROVIDER=OFF
BuildOption(conf):  -DgRPC_BUILD_TESTS=OFF
BuildOption(conf):  -DgRPC_DOWNLOAD_ARCHIVES:BOOL=OFF
BuildOption(conf):  -DgRPC_BUILD_GRPC_PYTHON_PLUGIN=ON

BuildRequires:  abseil-cpp-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)

%description
gRPC is a modern, open source, high-performance Remote Procedure Call (RPC)
framework that can run in any environment.

%package     -n python-grpcio
Summary:        Python bindings for gRPC
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-grpcio%{?_isa} = %{version}-%{release}
Provides:       python3-grpcio = %{version}-%{release}
%python_provide python3-grpcio

%description -n python-grpcio
Python language bindings for gRPC (HTTP/2-based RPC framework).

%package        devel
Summary:        Development files for gRPC
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libcares)
Requires:       pkgconfig(re2)

%description    devel
This package contains the libraries, header files, and tools needed to
develop applications that use the gRPC framework.

%prep -a
find . -type f -regex ".*\.py\|.*\.sh" -exec sed -i -e 's|/usr/bin/env python.*|/usr/bin/python3|' -e 's|/usr/bin/python.*|/usr/bin/python3|' {} +
rm -Rf third_party/abseil-cpp/

# Fixing a bug in gRPC 1.78+ where upstream source files are hard-coded (Issue #41696)
mkdir -p third_party/abseil-cpp/absl/log/
touch third_party/abseil-cpp/absl/log/initialize.cc

%build -a
%pyproject_wheel

%install -a
rm -Rf %{buildroot}%{_datadir}/grpc/*.pem
%fdupes %{buildroot}%{_prefix}
%pyproject_install
%pyproject_save_files grpc

%files
%license LICENSE
%{_libdir}/libaddress_sorting.so.*
%{_libdir}/libgpr*.so.*
%{_libdir}/libgrpc*.so.*
%{_libdir}/libutf8_range_lib.so.*
%{_libdir}/libupb*.so.*

%files -n python-grpcio -f %{pyproject_files}
%license LICENSE

%files devel
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gpr.pc
%{_libdir}/pkgconfig/grpc++.pc
%{_libdir}/pkgconfig/grpc++_unsecure.pc
%{_libdir}/pkgconfig/grpc.pc
%{_libdir}/pkgconfig/grpc_unsecure.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/grpc/

%changelog
%autochangelog
