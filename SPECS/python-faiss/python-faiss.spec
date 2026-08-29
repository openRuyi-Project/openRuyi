# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <KimmyXYC@users.noreply.github.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname faiss
%global pypi_name faiss-cpu
# libfaiss is bundled privately beside the extension and is not a system ABI.
%global __provides_exclude ^libfaiss\\.so.*$
%global __requires_exclude ^libfaiss\\.so.*$

Name:           python-%{srcname}
Version:        1.15.0
Release:        %autorelease
Summary:        Efficient similarity search and clustering of dense vectors
License:        MIT
URL:            https://github.com/facebookresearch/faiss
VCS:            git:https://github.com/facebookresearch/faiss.git
#!RemoteAsset:  sha256:0b94bf4b17229b28a8a6686d7637ce93de4ef25f6308040184675befad9d9332
Source0:        https://github.com/facebookresearch/faiss/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    pyproject

# Preserve debuginfo and openRuyi compiler flags instead of upstream wheel flags.
Patch2000:      2000-honor-distribution-build-flags.patch
# Keep RVA20 binaries usable because V and Zvfhmin are only guaranteed by RVA23.
Patch2001:      2001-allow-disabling-rvv.patch

%if "%{openruyi_riscv_arch}" == "-march=rva23u64"
BuildOption(build):  -Ccmake.define.FAISS_ENABLE_RVV=ON
%else
BuildOption(build):  -Ccmake.define.FAISS_ENABLE_RVV=OFF
%endif
BuildOption(install):  -l %{srcname} -L
# Skip private native library: dynamic module does not define module export function (PyInit_libfaiss).
BuildOption(check):  -e '%{srcname}.libfaiss'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libomp-devel
BuildRequires:  ninja
BuildRequires:  openblas-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(scikit-build-core)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(swig)
BuildRequires:  python3dist(torch)
BuildRequires:  swig

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{pypi_name} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
Provides:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}
%python_provide python3-%{pypi_name}

%description
Faiss is a library for efficient similarity search and clustering of dense
vectors. This package provides the CPU implementation and its Python and NumPy
bindings.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md THIRD_PARTY_NOTICES
%license LICENSE

%changelog
%autochangelog
