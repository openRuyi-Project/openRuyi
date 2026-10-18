# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global version_suffix %{lua: \
  local v = rpm.expand("%{version}") \
  local _, count = v:gsub("%.", "") \
  print(count > 1 and "-stable" or "") \
}

# Avoid OOM on RISC-V builders
%define _lto_cflags %{nil}
%global _smp_build_ncpus 16

Name:           dpdk
Version:        26.07
Release:        %autorelease
Summary:        Set of libraries and drivers for fast packet processing
License:        BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-only
URL:            http://dpdk.org
VCS:            git:https://github.com/DPDK/dpdk
#!RemoteAsset:  sha256:7141a8b5bad9d7d965483ac0d75317ac0c21dcee1d13d373693c655f9e3fabe6
Source:         https://fast.dpdk.org/rel/dpdk-%{version}.tar.xz
BuildSystem:    meson

%global dpdk_isa generic
%ifarch riscv64
%if "%{openruyi_riscv_arch}" == "-march=rva23u64"
%global dpdk_isa rva23u64
%endif
%endif

BuildOption(prep):  -p1 -n dpdk%{version_suffix}-%{version}
BuildOption(conf):  -Dcpu_instruction_set=%{dpdk_isa}

BuildRequires:  meson
BuildRequires:  python3dist(pyelftools)
BuildRequires:  gcc
BuildRequires:  linux-headers
BuildRequires:  libpcap-devel
BuildRequires:  zlib-devel
BuildRequires:  numactl-devel
BuildRequires:  openssl-devel
BuildRequires:  rdma-core-devel
BuildRequires:  pkgconfig(libarchive)

%patchlist
# https://git.dpdk.org/dpdk/commit/?id=d86c606fe341507071701c16fd56f92db8feca70
1000-fib-use-scalar-lookup-for-network-byte-order-on-RISC.patch

%description
The Data Plane Development Kit is a set of libraries and drivers for
fast packet processing in the user space.

%package        devel
Summary:        Data Plane Development Kit development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rdma-core-devel

%description    devel
This package contains the headers and other files needed for developing
applications with the Data Plane Development Kit.

%package        tools
Summary:        Tools for setting up Data Plane Development Kit environment
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kmod
Requires:       pciutils
Requires:       iproute2
Requires:       which
Requires:       python3dist(pyelftools)

%description    tools
%{summary}

# Skip. Require environments with hugepages, etc.
%check

%files
%{_bindir}/dpdk-testpmd
%{_bindir}/dpdk-proc-info
%{_libdir}/*.so.*
%{_libdir}/dpdk/pmds-*/*.so.*

%files devel
%{_includedir}/
%{_datadir}/%{name}
%{_libdir}/*.so
%{_libdir}/dpdk/pmds-*/*.so
%exclude %{_libdir}/*.a
%{_libdir}/pkgconfig/libdpdk.pc
%{_libdir}/pkgconfig/libdpdk-libs.pc

%files tools
%{_bindir}/dpdk-dumpcap
%{_bindir}/dpdk-pdump
%{_bindir}/dpdk-graph
%{_bindir}/dpdk-test
%{_bindir}/dpdk-test-*
%{_bindir}/dpdk-*.py

%changelog
%autochangelog
