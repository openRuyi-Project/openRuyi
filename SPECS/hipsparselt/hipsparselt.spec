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

%global tensile_version 4.33.0

%bcond test 0

Name:           hipsparselt
Version:        %{rocm_version}
Release:        %autorelease
Summary:        A SPARSE marshaling library
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries
#!RemoteAsset:  sha256:9ebd347b9b0fab350ce48c27aa848fe8f99c8b743ecf5213965618fa4f9a25ba
Source0:        %{url}/releases/download/rocm-%{version}/%{name}.tar.gz
#!RemoteAsset:  sha256:72ad0a8db025c6d47397791a9fce5c80cde1b89fc830523d0b34e5138329de63
Source1:        %{url}/releases/download/rocm-%{version}/hipblaslt.tar.gz
# Patches for hipBLASLt's tensilelite (applied during prep inside hipBLASLt/)
Source2:        0001-hipblaslt-tensilelite-remove-yappi-dependency.patch
Source3:        0001-hipblaslt-tensilelite-use-system-paths.patch
Source4:        0001-hipblaslt-find-origami-package.patch
# Heartbeat during tensilelite ParallelMap2 kernel generation: without periodic
# output the silent phase trips OBS's logidlelimit and times out on slow workers
# (riscv64 emulation). Same fix as rocm-specs hipblaslt.
Source5:        2000-tensilelite-add-heartbeat-during-parallel-map.patch
# -mf16c is an x86-only clang flag (F16C intrinsics); guard it on x86 so the
# hipSPARSELt library builds on non-x86 hosts like riscv64. cf. ollama PR #8129
Patch2000:      2000-hipsparselt-guard-mf16c-to-x86.patch
BuildSystem:    cmake

BuildOption(conf):  -DBLAS_INCLUDE_DIR=%{_includedir}/flexiblas
BuildOption(conf):  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF
%if %{with test}
BuildOption(conf):  -DBUILD_CLIENTS_TESTS=ON
BuildOption(conf):  -DHIPSPARSELT_ENABLE_CLIENT=ON
%else
BuildOption(conf):  -DBUILD_CLIENTS_TESTS=OFF
BuildOption(conf):  -DHIPSPARSELT_ENABLE_CLIENT=OFF
%endif
BuildOption(conf):  -DBUILD_VERBOSE=ON
BuildOption(conf):  -DCMAKE_Fortran_COMPILER=gcc-fortran
BuildOption(conf):  -DCMAKE_VERBOSE_MAKEFILE=ON
BuildOption(conf):  -DGPU_TARGETS="gfx942;gfx950"
BuildOption(conf):  -DTensile_COMPILER=clang++
BuildOption(conf):  -DTensile_LIBRARY_FORMAT=msgpack
BuildOption(conf):  -DTensile_VERBOSE=1
BuildOption(conf):  -DVIRTUALENV_BIN_DIR=%{_bindir}
BuildOption(conf):  -Dnanobind_ROOT=%(python3 -m nanobind --cmake_dir)
BuildOption(conf):  -G Ninja
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++

BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipsparse)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(origami)
BuildRequires:  cmake(rocm_smi)
BuildRequires:  cmake(rocsparse)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  gcc-fortran
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  libomp-devel(major) = %{llvm_maj_ver}
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(msgpack)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(msgpack)
# nanobind is used to build the rocisa native module (build-time only)
BuildRequires:  python3dist(nanobind)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocminfo
BuildRequires:  rocm-llvm-macros
BuildRequires:  roctracer-devel

%if %{with test}
BuildRequires:  chrpath
BuildRequires:  pkgconfig(openblas)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gmock)
%endif

%global _description %{expand:
hipSPARSELt is a SPARSE marshaling library that provides general sparse
matrix-matrix multiplication using structured sparsity. It offers a flexible
API and supports multiple backends.
}

%description
%{_description}

%package        devel
Summary:        The hipSPARSELt development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The hipSPARSELt development package.

%if %{with test}
%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    test
%{_description}
%endif

%prep
%autosetup -p1 -n %{name}

tar xf %{SOURCE1}
cd hipblaslt

patch -p1 < %{SOURCE2}
patch -p1 < %{SOURCE3}
patch -p1 < %{SOURCE4}
patch -p1 < %{SOURCE5}

# Use PATH to find where TensileGetPath and other tensile bins are
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g' \
    tensilelite/Tensile/cmake/TensileConfig.cmake

# Make sure hip/hip_runtime.h is found
sed -i -e 's@-x hip @-I%{_includedir} -x hip @' device-library/matrix-transform/CMakeLists.txt
sed -i -e 's@"-D__HIP_HCC_COMPAT_MODE__=1"@"-D__HIP_HCC_COMPAT_MODE__=1","-I%{_includedir}"@' \
    tensilelite/Tensile/Toolchain/Component.py

# Use the distribution-provided nanobind instead of fetching/bundling it
sed -i -e 's@FetchContent_MakeAvailable(nanobind)@find_package(nanobind CONFIG REQUIRED)@' \
    tensilelite/rocisa/CMakeLists.txt

# disable openmp in hipBLASLt
sed -i -e 's@option(HIPBLASLT_ENABLE_OPENMP "Use OpenMP to improve performance." ON)@option(HIPBLASLT_ENABLE_OPENMP "Use OpenMP to improve performance." OFF)@' CMakeLists.txt

cd ..

# Point hipBLASLt path at the bundled in-source copy (default looks in ../hipblaslt)
sed -i -e 's@${CMAKE_CURRENT_SOURCE_DIR}/../hipblaslt@${CMAKE_CURRENT_SOURCE_DIR}/hipblaslt@' CMakeLists.txt

# Prevent the virtualenv install from cmake
sed -i -e 's@virtualenv_install@#virtualenv_install@' CMakeLists.txt

# Unforce the setting of libdir
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt

# We are building from a tarball, not a git repo
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' hipblaslt/cmake/dependencies.cmake

# Replace all mentions of 'amdclang' with 'clang' in Tensile Python files
find hipblaslt/tensilelite -type f -name "*.py" -exec sed -i 's/amdclang++/clang++/g; s/amdclang/clang/g' {} +

%conf -p
export PATH=%{rocmllvm_bindir}:$PATH

%build -p
# Do a manual install of tensilelite instead of cmake's virtualenv, then point
# Tensile at it for build-time kernel generation (same approach as hipblaslt)
cd hipblaslt/tensilelite
TL=$PWD
%__python3 setup.py install --root $TL
cd ../..

export PATH=%{_prefix}/bin:%{rocmllvm_bindir}:$PATH
CLANG_PATH=`hipconfig --hipclangpath`
ROCM_CLANG=${CLANG_PATH}/clang
RESOURCE_DIR=`${ROCM_CLANG} -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler
export PATH=${TL}/%{_bindir}:$PATH
export PYTHONPATH=${TL}%{python3_sitelib}:$PYTHONPATH
export Tensile_DIR=${TL}%{python3_sitelib}/Tensile

%install -a
rm -f %{buildroot}%{_datadir}/doc/hipsparselt/LICENSE.md

# Strip and fix permissions on hsaco kernel files
%{rocmllvm_bindir}/llvm-strip %{buildroot}%{_libdir}/hipsparselt/library/Kernels*.hsaco
chmod a+x %{buildroot}%{_libdir}/hipsparselt/library/Kernels*.hsaco

%files
%doc README.md
%license LICENSE.md
%{_libdir}/libhipsparselt.so.*
%{_libdir}/hipsparselt/

%files devel
%{_includedir}/hipsparselt/
%{_libdir}/cmake/hipsparselt/
%{_libdir}/libhipsparselt.so

%if %{with test}
%files test
%{_bindir}/hipsparselt*
%endif

%changelog
%autochangelog
