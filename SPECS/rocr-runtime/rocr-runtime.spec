# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstreamname ROCR-Runtime

%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

#Image support is x86 only
%ifarch x86_64
%global enableimage 1
%endif

%global kfdtest 1

Name:           rocr-runtime
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm Runtime Library
License:        NCSA
URL:            https://github.com/ROCm/ROCR-Runtime
#!RemoteAsset
Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz
BuildSystem:    cmake

Patch0:         0001-Add-riscv64-support.patch
Patch1:         0002-Replace-fence-instrutions-for-riscv64.patch

BuildOption(conf):  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/..
BuildOption(conf):  -DCMAKE_SHARED_LINKER_FLAGS=-ldrm_amdgpu
BuildOption(conf):  -DINCLUDE_PATH_COMPATIBILITY=OFF
BuildOption(conf):  -DCMAKE_PROGRAM_PATH=%{rocmllvm_bindir}

BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  lld
BuildRequires:  lld-devel
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-macros
BuildRequires:  xxd

%description
The ROCm Runtime Library is a thin, user-mode API that exposes the necessary
interfaces to access and interact with graphics hardware driven by the AMDGPU
driver set and the AMDKFD kernel driver. Together they enable programmers to
directly harness the power of AMD discrete graphics devices by allowing host
applications to launch compute kernels directly to the graphics hardware.

%package        devel
Summary:        ROCm Runtime development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
ROCm Runtime development files

%if 0%{?kfdtest}
%package     -n kfdtest
Summary:        Test suite for ROCm's KFD kernel module
Requires:       rocm-smi

%description -n kfdtest
This package includes ROCm's KFD kernel module test suite (kfdtest), the list of
excluded tests for each ASIC, and a convenience script to run the test suite.
%endif

%prep -a
# Use llvm's static libs kfdtest
sed -i -e 's@LLVM_LINK_LLVM_DYLIB@0@' libhsakmt/tests/kfdtest/CMakeLists.txt

sed -i '/#include <memory>.*/a#include <cstdint>' runtime/hsa-runtime/core/inc/amd_elf_image.hpp

%build -a
%if 0%{kfdtest}
export PATH=%{rocmllvm_bindir}:$PATH
export LIBHSAKMT_PATH=$(pwd)/%__cmake_builddir/libhsakmt/archive
cd libhsakmt/tests/kfdtest
%cmake -DCMAKE_SKIP_RPATH=ON -DLLVM_DIR=%{rocmllvm_cmakedir}
%cmake_build
%endif

%install -a
%if 0%{kfdtest}
cd libhsakmt/tests/kfdtest
%cmake_install
%endif

rm -f %{buildroot}%{_prefix}/share/doc/hsa-runtime64/LICENSE.md
rm -f %{buildroot}%{_prefix}/share/doc/packages/%{name}/LICENSE.md
rm -f %{buildroot}%{_libdir}/libhsakmt.*
rm -rf %{buildroot}%{_libdir}/cmake/hsakmt
rm -f %{buildroot}%{_libdir}/pkgconfig/libhsakmt.pc

%files
%doc        README.md
%license    LICENSE.txt
%{_libdir}/libhsa-runtime64.so.1{,.*}

%files      devel
%{_includedir}/hsa/
%{_includedir}/hsakmt
%{_libdir}/libhsa-runtime64.so
%{_libdir}/cmake/hsa-runtime64/

%if 0%{kfdtest}
%files   -n kfdtest
%doc        libhsakmt/tests/kfdtest/README.txt
%license    libhsakmt/tests/kfdtest/LICENSE.kfdtest
%{_bindir}/kfdtest
%{_bindir}/run_kfdtest.sh
%{_datadir}/kfdtest
%endif

%changelog
%{?autochangelog}
