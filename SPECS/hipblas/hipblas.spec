# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_version 7.1.1

Name:           hipblas
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm BLAS marshalling library
License:        MIT
Url:            https://github.com/ROCm/hipBLAS
#!RemoteAsset
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz
BuildSystem:    cmake

BuildRequires:  clang
BuildRequires:  clang-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipblas-common)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(rocblas)
BuildRequires:  cmake(rocsolver)
BuildRequires:  compiler-rt
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hipcc
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  rocm-cmake
BuildRequires:  rocm-llvm-macros

Provides:       hipblas = %{version}-%{release}

%description
hipBLAS is a Basic Linear Algebra Subprograms (BLAS) marshalling
library, with multiple supported backends. It sits between the
application and a 'worker' BLAS library, marshalling inputs into
the backend library and marshalling results back to the
application. hipBLAS exports an interface that does not require
the client to change, regardless of the chosen backend. Currently,
hipBLAS supports rocBLAS and cuBLAS as backends.

%package        devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(hipblas-common)

%description    devel
%{summary}

%prep -a
# This is a tarball, no .git to query
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' library/CMakeLists.txt

%install -a
rm -f %{buildroot}%{_prefix}/share/doc/hipblas/LICENSE.md

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libhipblas.so.3{,.*}

%files devel
%{_includedir}/hipblas/
%{_libdir}/libhipblas.so
%{_libdir}/cmake/hipblas/

%changelog
%autochangelog
