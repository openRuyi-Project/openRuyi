# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# ROCclr loads comgr at run time by soversion, so this needs to be checked when
# updating this package as it's used for the comgr requires for opencl and hip:
%global comgr_maj_api_ver 3
# See the file "rocclr/device/comgrctx.cpp" for reference:
# https://github.com/ROCm-Developer-Tools/ROCclr/blob/develop/device/comgrctx.cpp#L62

%global rocm_major 7
%global rocm_minor 1
%global rocm_patch 1
%global rocm_release %{rocm_major}.%{rocm_minor}
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname clr

Name:           rocclr
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm Compute Language Runtime
License:        MIT
URL:            https://github.com/ROCm/rocm-systems
#!RemoteAsset:  sha256:18ac260d0e750fb2d576b857823f68725d47d6357ce82e6d2f0130303b59a638
Source0:        %{url}/releases/download/rocm-%{version}/%{upstreamname}.tar.gz
#!RemoteAsset:  sha256:145457cead91d2f426a6926bbde1c0b9137fcd5f5dd35249b3b4836d4020980b
Source1:        %{url}/releases/download/rocm-%{version}/hip.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_AR=%{rocmllvm_bindir}/llvm-ar
BuildOption(conf):  -DCMAKE_RANLIB=%{rocmllvm_bindir}/llvm-ranlib
BuildOption(conf):  -DCMAKE_LINKER=%{rocmllvm_bindir}/ld.lld
BuildOption(conf):  -DHIP_COMMON_DIR=%{_builddir}/%{buildsubdir}/hip
BuildOption(conf):  -DHIPCC_BIN_DIR=%{_bindir}
BuildOption(conf):  -DHIP_COMPILER=hipcc
BuildOption(conf):  -DHIP_PLATFORM=amd
BuildOption(conf):  -DROCM_PATH=%{_prefix}
BuildOption(conf):  -DBUILD_ICD=OFF
BuildOption(conf):  -DCLR_BUILD_HIP=ON
BuildOption(conf):  -DCLR_BUILD_OCL=OFF
BuildOption(conf):  -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF
BuildOption(conf):  -DHIP_ENABLE_ROCPROFILER_REGISTER=OFF
BuildOption(conf):  -DUSE_PROF_API=ON
BuildOption(conf):  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/..

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(LLVM)
BuildRequires:  cmake(rocprofiler-register)
BuildRequires:  hipcc
BuildRequires:  lld
BuildRequires:  perl
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(cppheaderparser)
BuildRequires:  rocm-llvm-macros

%patchlist
# https://github.com/ROCm/rocm-systems/commit/655fbae6a1a54e7267fff90a246f0b54cdfcc94a
1001-fix-potential-data-race.patch
# Add riscv64 support
2001-fix-riscv64-abi.patch
2002-Replace-sfence-and-mfence.patch
2003-add-lp64d-target-to-llvm-mc.patch

%description
ROCm Compute Language Runtime

%package     -n rocm-hip
Summary:        ROCm HIP platform and device tool
Requires:       comgr(major) = %{comgr_maj_api_ver}
Requires:       hipcc

%description -n rocm-hip
HIP is a C++ Runtime API and Kernel Language that allows developers to create
portable applications for AMD and NVIDIA GPUs from the same source code.

%package     -n rocm-hip-devel
Summary:        ROCm HIP development package
Requires:       rocm-hip = %{version}-%{release}
Requires:       rocm-comgr-devel
Requires:       rocr-runtime-devel >= %{rocm_release}
# For roc-obj-ls
Requires:       binutils
Requires:       gawk

%description -n rocm-hip-devel
ROCm HIP development package.

%prep
%autosetup -N -a 1 -n %{upstreamname}

# ROCclr patches
%autopatch -p1

# Disable RPATH
# https://github.com/ROCm-Developer-Tools/hipamd/issues/22
sed -i '/INSTALL_RPATH/d' \
    opencl/tools/clinfo/CMakeLists.txt hipamd/CMakeLists.txt

# Upstream doesn't want OpenCL sonames because they don't guarantee API/ABI.
# For distributions, SOVERSION can be major.minor (i.e. rocm_release) as rocm patch
# releases are very unlikely to break anything:
echo "set_target_properties(amdocl PROPERTIES VERSION %{version} SOVERSION %rocm_release)" \
    >> opencl/amdocl/CMakeLists.txt
echo "libamdocl64.so.%{rocm_release}" > opencl/config/amdocl64.icd
echo "set_target_properties(cltrace PROPERTIES VERSION %{version} SOVERSION %rocm_release)" \
    >> opencl/tools/cltrace/CMakeLists.txt

# Clean up unused bundled code
# Only keep opencl2.2 headers as are they needed for now:
ls -d opencl/khronos/* | grep -v headers | xargs rm -r
ls -d opencl/khronos/headers/* | grep -v opencl2.2 | xargs rm -r
# Unused opencl 2.2 test code:
rm -r opencl/khronos/headers/opencl2.2/tests/

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' hipamd/src/CMakeLists.txt

# Stop cmake from trying to install HIPCC again:
sed -i "/install(PROGRAMS.*{[Hh][Ii][Pp][Cc]/d" hipamd/CMakeLists.txt

# Use cpack is not needed when we are doing the packaging here
# Gets confused on TW
sed -i -e 's@add_subdirectory(packaging)@#add_subdirectory(packaging)@' hipamd/CMakeLists.txt
sed -i -e 's@add_subdirectory(packaging)@#add_subdirectory(packaging)@' opencl/CMakeLists.txt

# cmake version
sed -i -e 's@cmake_minimum_required(VERSION 3.3)@cmake_minimum_required(VERSION 3.5)@' hipamd/src/hiprtc/cmake/hiprtc-config.cmake.in

%install -a
# TODO send upstream a patch, libhip should be installed with cmake's 'TARGETS'
chmod 755 %{buildroot}%{_libdir}/lib*.so*

# Unnecessary file and is not FHS compliant:
rm %{buildroot}%{_libdir}/.hipInfo

# Windows files:
rm %{buildroot}%{_bindir}/*.bat

rm -f %{buildroot}%{_prefix}/share/doc/packages/rocclr*/LICENSE.md
rm -f %{buildroot}%{_prefix}/share/doc/opencl*/LICENSE.md
rm -f %{buildroot}%{_prefix}/share/doc/hip-asan/LICENSE.md
rm -f %{buildroot}%{_prefix}/share/doc/hip/LICENSE.md

%files -n rocm-hip
%license hipamd/LICENSE.md
%{_libdir}/libamdhip64.so.%{rocm_major}{,.*}
%{_libdir}/libhiprtc.so.%{rocm_major}{,.*}
%{_libdir}/libhiprtc-builtins.so.%{rocm_major}{,.*}
%{_datadir}/hip

%files -n rocm-hip-devel
%{_bindir}/roc-*
%{_libdir}/libamdhip64.so
%{_libdir}/libhiprtc.so
%{_libdir}/libhiprtc-builtins.so
%{_libdir}/cmake/hip*
%{_bindir}/hipdemangleatp
%{_bindir}/hipcc_cmake_linker_helper
%{_includedir}/hip
%{_includedir}/hip_prof_str.h

%changelog
%autochangelog
