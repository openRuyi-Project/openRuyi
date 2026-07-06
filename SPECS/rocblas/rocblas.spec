# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Tests consumes too much time and space
%bcond test 0

%global rocm_version 7.2.4

%global llvm_maj_ver 22

Name:           rocblas
Summary:        BLAS implementation for ROCm
Version:        %{rocm_version}
Release:        %autorelease
License:        MIT AND BSD-3-Clause
URL:            https://github.com/ROCm/rocBLAS
#!RemoteAsset:  sha256:39ccaf6a0009a131b7daf3b21e14517f864f7642f109fa2da6dec1127b4a85e0
Source0:        %{url}/archive/rocm-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DBLAS_INCLUDE_DIR=%{_includedir}/cblas
BuildOption(conf):  -DBLAS_LIBRARY=cblas
BuildOption(conf):  -DCMAKE_CXX_COMPILER=hipcc
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld
BuildOption(conf):  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar
BuildOption(conf):  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib
BuildOption(conf):  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/..
BuildOption(conf):  -DCMAKE_SKIP_RPATH=ON
BuildOption(conf):  -DCMAKE_VERBOSE_MAKEFILE=ON
BuildOption(conf):  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF
# Avoid using external tensile
BuildOption(conf):  -DBUILD_WITH_PIP=OFF
BuildOption(conf):  -DROCM_SYMLINK_LIBS=OFF
BuildOption(conf):  -DHIP_PLATFORM=amd
# These will be enabled in a long future
BuildOption(conf):  -DBUILD_CLIENTS_BENCHMARKS=%{?with_test:ON}%{!?with_test:OFF}
BuildOption(conf):  -DBUILD_CLIENTS_TESTS=%{?with_test:ON}%{!?with_test:OFF}
BuildOption(conf):  -DBUILD_CLIENTS_TESTS_OPENMP=OFF
BuildOption(conf):  -DBUILD_FORTRAN_CLIENTS=OFF
BuildOption(conf):  -DBUILD_OFFLOAD_COMPRESS=ON
BuildOption(conf):  -DBUILD_WITH_HIPBLASLT=OFF
BuildOption(conf):  -DBUILD_WITH_TENSILE=ON
BuildOption(conf):  -DGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -DTensile_LIBRARY_FORMAT=msgpack
BuildOption(conf):  -DTensile_VERBOSE=1
BuildOption(conf):  -DTensile_DIR=$(%{_bindir}/TensileGetPath)/cmake
BuildOption(conf):  -DTensile_LOGIC=asm_full
BuildOption(conf):  -DTensile_CODE_OBJECT_VERSION=default
BuildOption(conf):  -DTensile_SEPARATE_ARCHITECTURES=ON
BuildOption(conf):  -DTensile_LAZY_LIBRARY_LOADING=ON
BuildOption(conf):  -DTensile_ASSEMBLER=%{rocmllvm_bindir}/clang++
BuildOption(conf):  -DCMAKE_PROGRAM_PATH=%{rocmllvm_bindir}

Patch0:         0001-fixup-install-of-tensile-output.patch
# https://github.com/ROCm/rocm-libraries/commit/6221075881f3ea8e9dfa0d985f22005c74ae1f52
Patch1:         0002-fix-nodiscard-return-value-ignored.patch

BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(msgpack)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  gcc-c++
BuildRequires:  hipcc
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3dist(tensile)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-macros

%if %{with test}
BuildRequires:  gcc-fortran
BuildRequires:  cmake(openmp)
BuildRequires:  cmake(rocm_smi)
BuildRequires:  pkgconfig(blas)
BuildRequires:  pkgconfig(GTest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  rocminfo
%endif

%description
rocBLAS is the AMD library for Basic Linear Algebra Subprograms
(BLAS) on the ROCm platform. It is implemented in the HIP
programming language and optimized for AMD GPUs.

%package        devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rocm-hip-devel

%description    devel
%{summary}

%if %{with test}
%package        test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       diffutils

%description    test
%{summary}
%endif

%conf -p
export PATH=%{rocmllvm_bindir}:$PATH

%prep -a
sed -i -e 's@target_link_libraries( rocblas-test PRIVATE ${BLAS_LIBRARY} ${GTEST_BOTH_LIBRARIES} roc::rocblas )@target_link_libraries( rocblas-test PRIVATE cblas ${GTEST_BOTH_LIBRARIES} roc::rocblas )@' clients/gtest/CMakeLists.txt

# no git in this build
sed -i -e 's@find_package(Git REQUIRED)@find_package(Git)@' library/CMakeLists.txt

# /usr/include/gtest/internal/gtest-port.h:279:2: error: C++ versions less than C++14 are not supported.
#   279 | #error C++ versions less than C++14 are not supported.
sed -i -e 's@CXX_STANDARD 11@CXX_STANDARD 17@' clients/samples/CMakeLists.txt
sed -i "s@/opt/rocm@%{_prefix}@g" \
    clients/cmake/FindROCmSMI.cmake \
    clients/CMakeLists.txt \
    rmake.py \
    rmake.py \
    rmake.py \
    toolchain-linux.cmake \
    header_compilation_tests.sh \
    library/src/tensile_host.cpp \
    library/src/include/handle.hpp \
    scripts/utilities/check_for_pretuned_sizes_c/Makefile \
    scripts/performance/blas/getspecs.py \
    scripts/performance/blas/commandrunner.py \
    CMakeLists.txt \
    library/CMakeLists.txt
sed -i "s@llvm/bin@bin@g" CMakeLists.txt library/CMakeLists.txt

%install -a
rm -f %{buildroot}%{_prefix}/share/doc/rocblas/LICENSE.md

%check
%if %{with test}
export LD_LIBRARY_PATH=%{_vpath_builddir}/library/src:$LD_LIBRARY_PATH
%{_vpath_builddir}/clients/staging/rocblas-test --gtest_brief=1
%endif

%files
%license LICENSE.md
%{_libdir}/librocblas.so.5{,.*}
%{_libdir}/rocblas/

%files devel
%doc README.md
%{_includedir}/rocblas/
%{_libdir}/cmake/rocblas/
%{_libdir}/librocblas.so

%if %{with test}
%files test
%{_bindir}/rocblas*
%endif

%changelog
%autochangelog
