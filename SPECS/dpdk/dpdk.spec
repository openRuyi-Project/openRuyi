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
Version:        25.07
Release:        %autorelease
Summary:        Set of libraries and drivers for fast packet processing
License:        BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-only
URL:            http://dpdk.org
VCS:            git:https://github.com/DPDK/dpdk
#!RemoteAsset
Source:         https://fast.dpdk.org/rel/dpdk-%{version}.tar.xz
BuildSystem:    meson

BuildOption(prep):  -p1 -n dpdk%{version_suffix}-%{version}
BuildOption(conf):  -Dmachine=generic

BuildRequires:  meson
BuildRequires:  python3-pyelftools
BuildRequires:  gcc
BuildRequires:  linux-headers
BuildRequires:  libpcap-devel
BuildRequires:  zlib-devel
BuildRequires:  numactl-devel
BuildRequires:  openssl-devel
BuildRequires:  rdma-core-devel

%patchlist
# 25.11
0001-config-riscv-detect-V-extension.patch
0002-lpm-lookup-with-RISC-V-vector-extension.patch
0003-fib-lookup-with-RISC-V-vector-extension.patch
0004-config-riscv-consider-specified-CPU.patch
0005-test-raise-fast-test-timeout-to-60s-on-RISC-V.patch
0006-config-riscv-add-rv64gcv-cross-compilation-target.patch
# https://patches.dpdk.org/project/dpdk/patch/20251116155001.2809998-1-sunyuechi@iscas.ac.cn/
0007-node-lookup-with-RISC-V-vector-extension.patch
# https://patches.dpdk.org/project/dpdk/patch/20251130200810.879556-1-sunyuechi@iscas.ac.cn/
0008-acl-add-RISC-V-vector-extension-implementation.patch

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
Requires:       python3-pyelftools

%description    tools
%{summary}

# Only run fast-tests; other tests require environments with hugepages, etc.
%check
tests=$(meson test -C %{_vpath_builddir} --suite fast-tests --list \
  | awk '{print $3}' \
  | grep -Ev 'argparse_autotest|rwlock_test1_autotest|pflock_autotest|ticketlock_autotest')
meson test -C %{_vpath_builddir} --num-processes %{_smp_build_ncpus} --print-errorlogs $tests

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
%exclude %{_bindir}/dpdk-*.py
%{_bindir}/dpdk-dumpcap
%{_bindir}/dpdk-pdump
%{_bindir}/dpdk-graph
%{_bindir}/dpdk-test
%{_bindir}/dpdk-test-*
%{_bindir}/dpdk-*.py

%changelog
%autochangelog
