# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# The package follows LLVM's major version, but API version is still important:
%global comgr_maj_api_ver 3
%global comgr_full_api_ver %{comgr_maj_api_ver}.0

# What LLVM is upstream using (use LLVM_VERSION_MAJOR from cmake/Modules/LLVMVersion.cmake):
%global llvm_maj_ver 21
# Sakura286: ROCm 7.1.1 uses LLVM 20, but only LLVM 21 is on openRuyi.
#            Backport is needed.
%global rocm_llvm_maj_ver 20

%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global bundle_prefix %{_libdir}/llvm%{llvm_maj_ver}
%global llvm_triple %{_target_platform}
%global amd_device_libs_prefix lib/clang/%{llvm_maj_ver}

%global toolchain clang

%ifarch x86_64
%global targets_to_build "X86;AMDGPU"
%endif
%ifarch riscv64
%global targets_to_build "RISCV;AMDGPU"
%endif

# All the tests are not enabled both on fedora and debian
# https://salsa.debian.org/rocm-team/rocm-llvm/-/blob/debian/unstable/debian/rules
# https://src.fedoraproject.org/rpms/rocm-compilersupport/blob/rawhide/f/rocm-compilersupport.spec
# Disabled by default.
%bcond device_libs_test 0
%bcond comgr_test 0

Name:           rocm-llvm
Version:        %{rocm_version}
Release:        %autorelease
Summary:        Various AMD ROCm LLVM related services
# llvm is Apache-2.0 WITH LLVM-exception OR NCSA
# hipcc is MIT, comgr and device-libs are NCSA:
License:        (Apache-2.0 WITH LLVM-exception OR NCSA) AND NCSA AND MIT
URL:            https://github.com/ROCm/llvm-project
#!RemoteAsset
Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz
Source1:        rocm-llvm.prep.in

# RISC-V support patches
# https://salsa.debian.org/rocm-team/rocm-llvm/-/merge_requests/2
Patch0:         0002-Use-signed-char-in-comgr-building.patch
# Backport mainline comgr patches since 7.1.1 is build on llvm-20
Patch1:         0003-adapt-comgr-api-to-llvm-21.patch

BuildRequires:  clang >= %{llvm_maj_ver}
BuildRequires:  clang-devel >= %{llvm_maj_ver}
BuildRequires:  clang-tools-extra
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  lld >= %{llvm_maj_ver}
BuildRequires:  lld-devel >= %{llvm_maj_ver}
BuildRequires:  llvm-devel >= %{llvm_maj_ver}
BuildRequires:  llvm-test >= %{llvm_maj_ver}
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
# comgr requires python
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rocm-cmake >= %{rocm_release}

%description
%{summary}

%package        macros
Summary:        ROCm Compiler RPM macros for RPM Build
BuildArch:      noarch

%description    macros
This package contains ROCm compiler related RPM macros.

%package     -n rocm-device-libs
Summary:        AMD ROCm LLVM bit code libraries

%description -n rocm-device-libs
This package contains a set of AMD specific device-side language runtime
libraries in the form of bit code. Specifically:
 - Open Compute library controls
 - Open Compute Math library
 - Open Compute Kernel library
 - OpenCL built-in library
 - HIP built-in library
 - Heterogeneous Compute built-in library

%package     -n rocm-comgr
Summary:        AMD ROCm LLVM Code Object Manager
Provides:       comgr(major) = %{comgr_maj_api_ver}
Provides:       rocm-comgr = %{comgr_full_api_ver}-%{release}

%description -n rocm-comgr
The AMD Code Object Manager (Comgr) is a shared library which provides
operations for creating and inspecting code objects.

%package     -n rocm-comgr-devel
Summary:        AMD ROCm LLVM Code Object Manager
Requires:       rocm-comgr%{?_isa} = %{version}-%{release}
Requires:       rocm-device-libs

%description -n rocm-comgr-devel
The AMD Code Object Manager (Comgr) development package.

%package     -n hipcc
Summary:        HIP compiler driver
Requires:       rocm-device-libs = %{version}-%{release}
Suggests:       rocminfo

%description -n hipcc
hipcc is a compiler driver utility that will call clang or nvcc, depending on
target, and pass the appropriate include and library options for the target
compiler and HIP infrastructure.

hipcc will pass-through options to the target compiler. The tools calling hipcc
must ensure the compiler options are appropriate for the target compiler.

%prep
%autosetup -p1 -n llvm-project-rocm-%{rocm_version}

# llvm_maj_ver sanity check (we should be matching the bundled llvm major ver):
if ! grep -q "set(LLVM_VERSION_MAJOR %{llvm_maj_ver})" cmake/Modules/LLVMVersion.cmake; then
    echo "ERROR llvm_maj_ver macro is not correctly set"
    # Sakura286: ROCm 7.1.1 uses LLVM 20, but only 21 is on openRuyi. Sad.
    # TODO: Need to re-enable this 'if' when rocm upstream bump to llvm-21
    # exit 1
fi

# Make sure we only build the AMD bits by discarding the bundled llvm code:
ls | grep -xv "amd" | xargs rm -r

install -pm 755 %{SOURCE1} prep.sh
sed -i -e 's@%%{_prefix}@%{_prefix}@' prep.sh
sed -i -e 's@%%{_lib}@%{_lib}@' prep.sh
sed -i -e 's@%%{amd_device_libs_prefix}@%{amd_device_libs_prefix}@' prep.sh
sed -i -e 's@%%{bundle_prefix}@%{bundle_prefix}@' prep.sh
sed -i -e 's@%%{llvm_maj_ver}@%{llvm_maj_ver}@' prep.sh
grep -v '%%{' prep.sh

. ./prep.sh

%build
CLANG_VERSION=%llvm_maj_ver

# Maybe use llvm-config-%{llvm_maj_ver} in the future
LLVM_BINDIR=`%{_libdir}/llvm%{llvm_maj_ver}/bin/llvm-config --bindir`
LLVM_CMAKEDIR=`%{_libdir}/llvm%{llvm_maj_ver}/bin/llvm-config --cmakedir`
# Only enable one target to accelerate build
GPU_TARGET="gfx1100;gfx1101;gfx1200;gfx1201"

echo "%%rocmllvm_version $CLANG_VERSION"    >  macros.rocmcompiler
echo "%%rocmllvm_bindir $LLVM_BINDIR"       >> macros.rocmcompiler
echo "%%rocmllvm_cmakedir $LLVM_CMAKEDIR"   >> macros.rocmcompiler
echo "%%rocm_gpu_list_default $GPU_TARGET"  >> macros.rocmcompiler

export PATH=%{_libdir}/llvm%{llvm_maj_ver}/bin:$PATH
export INCLUDE_PATH=%{_libdir}/llvm%{llvm_maj_ver}/include

# Build device-libs first, hipcc and comgr need it
%define _vpath_srcdir amd/device-libs
%define _vpath_builddir build-devicelibs
# Workaround for bug in cmake tests not finding amdgcn:
ln -s %{amd_device_libs_prefix}/amdgcn amdgcn
#TODO ROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_* should be removed in ROCm 7.0:
%cmake -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_NEW="%{amd_device_libs_prefix}/amdgcn" \
    -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_OLD="" \
    -DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld" \
    %{?__cmake_build_type:-DCMAKE_BUILD_TYPE="%{__cmake_build_type}"}
%cmake_build -- %{?_smp_mflags}
# Used by comgr to find device libs when building:
export ROCM_PATH=$(realpath %__cmake_builddir)

# Build comgr
%define _vpath_srcdir amd/comgr
%define _vpath_builddir build-comgr
%cmake -DCMAKE_PREFIX_PATH=$ROCM_PATH \
    -DCMAKE_MODULE_PATH=%{_libdir}/llvm%{llvm_maj_ver}/lib \
    -DCMAKE_BUILD_TYPE="RELEASE" \
    -DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld" \
    -DBUILD_TESTING=%{?with_comgr_test:ON}%{!?with_comgr_test:OFF}
%cmake_build -- %{?_smp_mflags}

# Build hipcc
%define _vpath_srcdir amd/hipcc
%define _vpath_builddir build-hipcc
%cmake -DHIPCC_BACKWARD_COMPATIBILITY=OFF \
    -DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld"
%cmake_build -- %{?_smp_mflags}

%check
# Test device-libs
%define _vpath_srcdir amd/device-libs
%define _vpath_builddir build-devicelibs
# Workaround for bug in cmake tests not finding amdgcn:
ln -s %{amd_device_libs_prefix}/amdgcn build-devicelibs/amdgcn
# Below tests are failed:
#    6 - compile_native_rcp__gfx600 (Failed)
#    7 - compile_native_rsqrt__gfx600 (Failed)
#   10 - compile_native_rcp__gfx700 (Failed)
#   11 - compile_native_rsqrt__gfx700 (Failed)
#   14 - compile_native_rcp__gfx803 (Failed)
#   15 - compile_native_rsqrt__gfx803 (Failed)
#   18 - compile_atomic_work_item_fence__gfx803 (Failed)
#   19 - compile_atomic_work_item_fence__gfx900 (Failed)
#   20 - compile_atomic_work_item_fence__gfx90a (Failed)
#   21 - compile_atomic_work_item_fence__gfx1030 (Failed)
#   22 - compile_atomic_work_item_fence__gfx1100 (Failed)
#   23 - compile_atomic_work_item_fence__gfx1200 (Failed)
%{?with_device_libs_test:%ctest}

# Test comgr
%define _vpath_srcdir amd/comgr
%define _vpath_builddir build-comgr
# Below tests are failed:
#    2 - comgr_disasm_llvm_reloc_test (SEGFAULT)
#    3 - comgr_disasm_llvm_so_test (SEGFAULT)
#    5 - comgr_disasm_options_test (SEGFAULT)
#   13 - comgr_compile_test (Failed)
#   14 - comgr_compile_minimal_test (Failed)
#   16 - comgr_compile_log_remarks_test (Failed)
#   17 - comgr_compile_source_with_device_libs_to_bc_with_vfs_test (Failed)
#   21 - comgr_get_data_isa_name_test (Failed)
#   29 - comgr_mangled_names_test (Failed)
#   30 - comgr_multithread_test (SEGFAULT)
#   32 - comgr_compile_hip_test (Failed)
#   33 - comgr_compile_hip_to_relocatable (Failed)
#   34 - comgr_mangled_names_hip_test (Failed)
#   35 - comgr_unbundle_hip_test (Failed)
%{?with_comgr_test:%ctest}

%install
# Install macros
install -Dpm 644 macros.rocmcompiler \
    %{buildroot}%{_rpmmacrodir}/macros.rocmcompiler

# Install device-libs
%define _vpath_builddir build-devicelibs
%cmake_install

# Install comgr
%define _vpath_builddir build-comgr
%cmake_install

# Install hipcc
%define _vpath_builddir build-hipcc
%cmake_install

rm -f %{buildroot}%{_datadir}/doc/ROCm-Device-Libs/LICENSE.TXT
rm -rf %{buildroot}%{_datadir}/doc/amd_comgr
rm -f %{buildroot}%{_datadir}/doc/hipcc/LICENSE.txt
rm -f %{buildroot}%{_datadir}/doc/hipcc/README.md

%files macros
%{_rpmmacrodir}/macros.rocmcompiler

%files -n rocm-device-libs
%doc        amd/device-libs/README.md amd/device-libs/doc/*.md
%license    amd/device-libs/LICENSE.TXT
%dir        %{_libdir}/cmake/AMDDeviceLibs
%{_libdir}/cmake/AMDDeviceLibs/*.cmake
%{_prefix}/%{amd_device_libs_prefix}/amdgcn

%files -n rocm-comgr
%doc        amd/comgr/README.md
%license    amd/comgr/LICENSE.txt
%license    amd/comgr/NOTICES.txt
%{_libdir}/libamd_comgr.so.*

%files -n rocm-comgr-devel
%dir        %{_includedir}/amd_comgr
%dir        %{_libdir}/cmake/amd_comgr
%{_includedir}/amd_comgr/amd_comgr.h
%{_libdir}/libamd_comgr.so
%{_libdir}/cmake/amd_comgr/*.cmake

%files -n hipcc
%doc        amd/hipcc/README.md
%license    amd/hipcc/LICENSE.txt
%license    amd/hipcc/README.md
%{_bindir}/hipcc
%{_bindir}/hipconfig
%{_bindir}/hipvars.pm

%changelog
%{?autochangelog}
