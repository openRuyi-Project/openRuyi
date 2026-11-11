# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# RISC-V unit-test template compilation was killed with 32 concurrent jobs.
%ifarch riscv64
%global _smp_ncpus_max 8
%endif

Name:           libcds
Version:        2.3.3
Release:        %autorelease
Summary:        Concurrent data structures library
License:        BSL-1.0
URL:            https://github.com/khizmax/libcds
VCS:            git:https://github.com/khizmax/libcds.git
#!RemoteAsset:  sha256:f090380ecd6b63a3c2b2f0bdb27260de2ccb22486ef7f47cc1175b70c6e4e388
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Firebird page-cache insertion needs the key/value update overload.
# https://github.com/FirebirdSQL/firebird/commit/6f93d275d0d2506ab774e17b16c748bf201069f6
Patch1000:      1000-support-preconstructed-michael-kvlist-values.patch
# Detect 64-bit pointers in the generic C++ atomics path on riscv64.
# https://sources.debian.org/src/libcds/2.3.3-7/debian/patches/ftbfs.patch/
Patch2000:      2000-detect-pointer-width-on-generic-architectures.patch
# Install the shared library and export its public compiler options.
Patch2001:      2001-install-shared-library-with-system-layout.patch

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
# The upstream flag detector otherwise exports -std=c++11 to GTest targets.
BuildOption(conf):  -DCMAKE_CXX_FLAGS="%{build_cxxflags} -std=c++17"
BuildOption(conf):  -DCMAKE_TARGET_ARCHITECTURE=%{_arch}
BuildOption(conf):  -DBUILD_STATIC=OFF
BuildOption(conf):  -DWITH_TESTS=ON
# Run the unit suite; stress targets default to large benchmark workloads.
BuildOption(conf):  -DENABLE_STRESS_TEST=OFF

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtest)

%description
libcds provides concurrent containers, memory reclamation schemes, and
synchronization primitives. Firebird uses its lock-free lists in the
database page cache.

%package        devel
Summary:        Development files for libcds
Provides:       libcds-devel(firebird-michael-kv-update)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, CMake targets, and pkg-config metadata for libcds, including the
preconstructed-value update interface used by Firebird.

%files
%doc readme.md change.log
%license LICENSE
%{_libdir}/libcds.so.*

%files devel
%{_includedir}/cds/
%{_libdir}/libcds.so
%{_libdir}/cmake/LibCDS/
%{_libdir}/pkgconfig/libcds.pc

%changelog
%autochangelog
