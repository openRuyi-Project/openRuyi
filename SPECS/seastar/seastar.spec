# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond dpdk 1

Name:           seastar
Version:        25.05.0
Release:        %autorelease
Summary:        Advanced C++ framework for high-performance server applications
License:        Apache-2.0
URL:            https://seastar.io/
VCS:            git:https://github.com/scylladb/seastar
#!RemoteAsset:  sha256:6e0405706a539af5a0ee307278bbd1fd965a2d97f7c8b970b7daa64d4ddfae11
Source0:        https://github.com/scylladb/seastar/archive/refs/tags/seastar-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DSeastar_DEPRECATED_OSTREAM_FORMATTERS:BOOL=OFF
BuildOption(conf):  -DSeastar_DOCS:BOOL=OFF
%if %{with dpdk}
BuildOption(conf):  -DSeastar_DPDK:BOOL=ON
%ifarch riscv64
# Seastar forces -march=${Seastar_DPDK_MACHINE} PUBLIC when DPDK is on; the
# default "native" is non-portable for a distro build
BuildOption(conf):  -DSeastar_DPDK_MACHINE=rv64gcv
%endif
%else
BuildOption(conf):  -DSeastar_DPDK:BOOL=OFF
%endif
BuildOption(conf):  -DSeastar_INSTALL:BOOL=ON
BuildOption(conf):  -DSeastar_TESTING:BOOL=ON

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libpciaccess-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  pkgconfig(libcares)
%if %{with dpdk}
BuildRequires:  pkgconfig(libdpdk)
%endif
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(liburing) >= 2.0
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  ragel
BuildRequires:  systemtap-sdt-devel
BuildRequires:  xfsprogs-devel

Provides:       %{name}-libs = %{version}-%{release}

%patchlist
# https://github.com/scylladb/seastar/commit/e5b109702df4b20d0dd45f397f0e94b08db85095
1000-util-adapt-to-fmt-12.0.0-API-changes.patch
# https://github.com/scylladb/seastar/commit/4b1542d93d5f85de724ad318962efef73ba1cd4f
1001-tests-avoid-printing-std-vector-in-BOOST_CHECK_EQUAL.patch
# https://github.com/scylladb/seastar/commit/2cbe79c66228
1002-http-declare-unsigned-char-alphabet-in-ragel-parsers.patch
# https://github.com/scylladb/seastar/commit/59225b1c6d2225b67dd2f2cebd3aa22be84b55d3
1003-core-util-add-initial-RISC-V-port.patch
# https://github.com/scylladb/seastar/commit/9bb7e48fccfde3b715a9e5ef2027233e8065f354
1004-cmake-don-t-require-i40e-sfc-DPDK-PMDs-on-RISC-V.patch
# https://github.com/scylladb/seastar/commit/c52e20fdeebb1fe84581b058cfd7fbc1578b3fa1
1005-build-also-detect-GCC-s-Wno-error-cpp-for-warning.patch
# https://github.com/scylladb/seastar/pull/3441
1006-cmake-guard-DPDK-dpdk-against-redefinition-in-Finddp.patch

%description
Seastar is an advanced, open-source C++ framework for high-performance
server applications on modern hardware. Seastar uses a shared-nothing
model that shards all requests onto individual cores, communicating via
explicit message passing instead of locks and atomic instructions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       lksctp-tools-devel
Requires:       pkgconfig(fmt)
Requires:       pkgconfig(gnutls)
Requires:       pkgconfig(hwloc)
Requires:       pkgconfig(libcares)
Requires:       pkgconfig(liblz4)
Requires:       pkgconfig(liburing)
Requires:       pkgconfig(protobuf)
Requires:       pkgconfig(yaml-cpp)

%description    devel
This package contains the header files, libraries, pkg-config and CMake
configuration files for developing applications that use Seastar.

%prep
# GitHub archive expands to seastar-seastar-<ver>/, override the autosetup name.
%autosetup -n %{name}-%{name}-%{version} -p1

%check
# Tests require host sysctl tuning (fs.aio-max-nr, kernel.perf_event_paranoid),
# /dev/shm 1777 bind, and public-network access (dns/tls tests), none of which
# the OBS chroot can provide.

%files
%doc README.md HACKING.md
%license LICENSE NOTICE
# Upstream CMake ships unversioned .so without SONAME.
%{_libdir}/libseastar.so
%{_libdir}/libseastar_testing.so
%{_libdir}/libseastar_perf_testing.so
%{_bindir}/seastar-json2code.py

%files devel
%{_includedir}/seastar/
%{_libdir}/cmake/Seastar/
%{_libdir}/pkgconfig/seastar.pc
%{_libdir}/pkgconfig/seastar-testing.pc

%changelog
%autochangelog
