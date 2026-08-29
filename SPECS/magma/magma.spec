# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond test 0

%global llvm_maj_ver 22

Name:           magma
Version:        2.10.0
Release:        %autorelease
Summary:        Matrix Algebra on GPU and Multi-core Architectures
License:        BSD-3-Clause
URL:            https://icl.utk.edu/magma/
VCS:            git:https://github.com/icl-utk-edu/magma.git
#!RemoteAsset:  sha256:26347adbccbe7a6693d6b3f3c0ab5620037eb3a62b5ef69d05e40289472a82a4
Source0:        https://github.com/icl-utk-edu/%{name}/archive/v%{version}.tar.gz
# Template for magma's own make.inc build config
Source1:        make.inc
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DBLA_VENDOR=OpenBLAS
BuildOption(conf):  -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
BuildOption(conf):  -DMAGMA_ENABLE_HIP=ON
BuildOption(conf):  -DUSE_FORTRAN=OFF
BuildOption(conf):  -DMAGMA_SO_VERSION=%{version}
BuildOption(conf):  -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf):  -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++

BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipblas)
BuildRequires:  cmake(hipsparse)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  gcc-c++
BuildRequires:  hipcc
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  ninja
BuildRequires:  pkgconfig(openblas)
BuildRequires:  pkgconfig(python3)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-llvm-macros

%patchlist
# Upstream installs the shared libraries unversioned; version them so the
# runtime library and the -devel .so symlink can live in separate packages.
# https://bitbucket.org/icl/magma/issues/77/versioning-so
2000-version-shared-libraries.patch
# Add newer gfx targets to Makefile's valid arch whitelist
# https://bitbucket.org/icl/magma/issues/76/a-few-new-rocm-gpus
2001-add-newer-gfx-targets.patch
# Change the bin,lib install locations
2002-fix-install-destination-dirs.patch
# python to python3, need env to find local bits like magmasubs.py
2003-python3-shebangs.patch
# ICS, Copy of strlcpy - just use strlcpy
2004-drop-bundled-strlcpy.patch
%if %{with test}
# Remove a test that fails to link (undefined magma_generate_matrix)
2005-remove-broken-test.patch
%else
# Disable building tests
2006-disable-tests-cmake.patch
%endif

%global _description %{expand:
Matrix Algebra on GPU and Multi-core Architectures (MAGMA) is a collection
of next-generation linear algebra libraries for heterogeneous computing.
The MAGMA package supports interfaces for current linear algebra packages
and standards (e.g., LAPACK and BLAS) to enable computational scientists
to easily port any linear algebra–reliant software component to
heterogeneous computing systems. MAGMA enables applications to fully
exploit the power of current hybrid systems of many-core CPUs and
multi-GPUs/coprocessors to deliver the fastest possible time to accurate
solutions within given energy constraints.

MAGMA features LAPACK-compliant routines for multi-core CPUs enhanced with
NVIDIA or AMD GPUs. MAGMA 2.7.2 now includes more than 400 routines that
cover one-sided dense matrix factorizations and solvers, two-sided
factorizations, and eigen/singular-value problem solvers, as well as a
subset of highly optimized BLAS for GPUs. A MagmaDNN package has been
added and further enhanced to provide high-performance data analytics,
including functionalities for machine learning applications that use MAGMA
as their computational back end. The MAGMA Sparse and MAGMA Batched
packages have been included since MAGMA 1.6.
}

%description
%{_description}

%package        devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{_description}

%prep -a
# Remove some files we do not need to simplify licenses
# GPL, results for cuda
rm -rf results/*

%conf -p
export PATH=%{rocmllvm_bindir}:$PATH
export MAGMA_GPU_TARGET=%{rocm_gpu_list_default}

cp %{SOURCE1} make.inc
sed -i "s/@GPU_TARGET@/$MAGMA_GPU_TARGET/" make.inc

make generate

%if %{with test}
%check
%{_vpath_builddir}/testing/testing_sgemm
%endif

%files
%license COPYRIGHT
%{_libdir}/libmagma.so.*
%{_libdir}/libmagma_sparse.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libmagma.so
%{_libdir}/libmagma_sparse.so

%changelog
%autochangelog
