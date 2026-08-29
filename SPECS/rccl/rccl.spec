# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_release 7.2
%global rocm_patch   4
%global rocm_version %{rocm_release}.%{rocm_patch}

%global llvm_maj_ver 22

# Linking AMD device libs code takes too much time
# Set --lto-partitions can accelerate, but even --lto-partitions=4 is killed for OOM on riscv64
%ifarch riscv64
%global lto_partitions 2
%else
%global lto_partitions %(nproc)
%endif

Name:           rccl
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm Communication Collectives Library
# From License.txt the main license is BSD 3
# Modifications from Microsoft is MIT
# The NVIDIA based header files below are Apache-2.0
#  src/include/nvtx3/nv*.h and similar
# The URL for NVIDIA in the License.txt https://github.com/NVIDIA/NVTX is Apache-2.0
License:        BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://github.com/ROCm/rccl
#!RemoteAsset:  sha256:e8927c61f76e70801e660a3482d383b30159d6f2a9e0580e5cdf168f2503e8c7
Source0:        %{url}/archive/rocm-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -DEXPLICIT_ROCM_VERSION=%{version}
BuildOption(conf):  -DROCM_PATH=%{_prefix}
BuildOption(conf):  -DCMAKE_VERBOSE_MAKEFILE=ON
BuildOption(conf):  -DBUILD_TESTS=ON
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++

BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(rocm_smi)
BuildRequires:  cmake(rocm-core)
BuildRequires:  cmake(rocprofiler-register)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  hipify
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-llvm-macros

Requires:       %{name}-data = %{version}-%{release}

%global _description %{expand:
RCCL (pronounced "Rickle") is a stand-alone library of standard
collective communication routines for GPUs, implementing all-reduce,
all-gather, reduce, broadcast, reduce-scatter, gather, scatter, and
all-to-all. There is also initial support for direct GPU-to-GPU
send and receive operations. It has been optimized to achieve high
bandwidth on platforms using PCIe, xGMI as well as networking using
InfiniBand Verbs or TCP/IP sockets. RCCL supports an arbitrary
number of GPUs installed in a single node or multiple nodes, and
can be used in either single- or multi-process (e.g., MPI)
applications.

The collective operations are implemented using ring and tree
algorithms and have been optimized for throughput and latency. For
best performance, small operations can be either batched into
larger operations or aggregated through the API.
}

%description
%{_description}

%package        devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rccl-devel = %{version}-%{release}

%description    devel
Headers and libraries for %{name}

%package        data
Summary:        Data for %{name}
BuildArch:      noarch

%description    data
Data for %{name}

%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
%{_description}

%prep -a
# Do not force install
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' cmake/Dependencies.cmake
# -amdgpu-s-branch-bits and -amdgpu-long-branch-factor=2 are needed to avoid 'branch size exceed simm16' error
# --lto-partitions parallelizes the GPU LTO codegen (capped on riscv64, see lto_partitions above)
sed -i -e 's@target_link_options(rccl PRIVATE "SHELL:-Xoffload-linker -mllvm=-amdgpu-kernarg-preload-count=16")@target_link_options(rccl PRIVATE "SHELL:-Xoffload-linker -mllvm=-amdgpu-s-branch-bits=15" "SHELL:-Xoffload-linker -mllvm=-amdgpu-long-branch-factor=2" "SHELL:-Xoffload-linker -mllvm=-amdgpu-kernarg-preload-count=16" "SHELL:-Xoffload-linker --lto-partitions=%{lto_partitions}" "SHELL:-Xoffload-linker --verbose")@' CMakeLists.txt

%conf -p
export PATH=%{rocmllvm_bindir}:$PATH

%build
%ifarch riscv64
# Prevent from being killed by build machine
timeout 20h bash -c 'while sleep 300; do echo "[heartbeat] $(date)"; done' & TIME_OUT=$!
%endif

%cmake_build

%ifarch riscv64
kill $TIME_OUT 2>/dev/null || true
%endif

%install -a
rm -f %{buildroot}%{_datadir}/doc/rccl/LICENSE.txt

%files
%license LICENSE.txt
%{_libdir}/librccl.so.*
%{_bindir}/rcclras

%files data
%{_datadir}/rccl/msccl-algorithms/
%{_datadir}/rccl/msccl-unit-test-algorithms/

%files devel
%doc README.md
%{_includedir}/rccl/
%{_libdir}/cmake/rccl/
%{_libdir}/librccl.so

%files test
%{_bindir}/rccl-UnitTests

%changelog
%autochangelog
