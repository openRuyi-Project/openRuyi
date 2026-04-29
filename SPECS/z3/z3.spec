# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Specifically for python-claripy
# https://github.com/angr/claripy/blob/master/pyproject.toml#L19
# If we don't provide the version directly (4.13 but not 4.13.0 or anyother),
# The pyproject will output "nothing provide python3dist(z3-solver) == 4.13"
# TODO: Is this a pyproject bug?
%global z3_major_ver 4.13

%global srcname z3

Name:           %{srcname}
Version:        %{z3_major_ver}.0
Release:        %autorelease
Summary:        The Z3 Theorem Prover
License:        MIT
URL:            https://github.com/Z3Prover/z3
#!RemoteAsset:  sha256:01bcc61c8362e37bb89fd2430f7e3385e86df7915019bd2ce45de9d9bd934502
Source0:        https://github.com/Z3Prover/z3/archive/%{srcname}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_CXX_FLAGS="%{optflags} -Wno-overloaded-virtual -Wno-template-body"
BuildOption(conf):  -DZ3_BUILD_LIBZ3_SHARED=true
BuildOption(conf):  -DZ3_USE_LIB_GMP=true
BuildOption(conf):  -DZ3_BUILD_PYTHON_BINDINGS=true
BuildOption(conf):  -DZ3_INSTALL_PYTHON_BINDINGS=true
BuildOption(conf):  -DZ3_ENABLE_EXAMPLE_TARGETS=false
BuildOption(conf):  -DZ3_LINK_TIME_OPTIMIZATION=true
BuildOption(conf):  -DCMAKE_INSTALL_PREFIX=%{_prefix}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python-rpm-macros

%description
Z3 is a Satisfiability Modulo Theories (SMT) solver and integrates
several decision procedures: Linear real and integer arithmetic,
fixed-size bit vectors, uninterpreted functions, extensional arrays,
quantifiers and model generation.

%package        libs
Summary:        Library for the Z3 SMT theorem prover

%description    libs
Z3 is a Satisfiability Modulo Theories (SMT) solver and integrates
several decision procedures.

This subpackage contains the Z3 runtime library needed for Z3 and
other projects.

%package        devel
Summary:        Development files for Z3
Requires:       z3-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for the Z3 library.

# The Python API for z3 is named z3-solver.
# https://github.com/Z3Prover/z3/blob/dcb888d4c87ddc4effc395f8095805560b94fb05/src/api/python/setup.py#L335
%package     -n python-%{srcname}-solver
Summary:        Python bindings for Z3
BuildArch:      noarch
# Specifically for python-claripy
# TODO: remove after this issue is resolved, see above.
Provides:       python3dist(z3-solver) == %{z3_major_ver}
Provides:       python3-%{srcname}-solver
%python_provide python3-%{srcname}-solver

%description -n python-%{srcname}-solver
Python bindings for the Z3 library.

%prep -a
# fix some bugs
# https://github.com/Z3Prover/z3/blob/3049f578a8f98a0b0992eca193afe57a73b30ca3/src/math/lp/column_info.h#L50
sed -i 's/m_low_bound/m_lower_bound/g' src/math/lp/column_info.h
# https://github.com/Z3Prover/z3/blob/3049f578a8f98a0b0992eca193afe57a73b30ca3/src/math/lp/static_matrix.h#L82
sed -i 's/v\.m_matrix\.get(/v.m_matrix.get_elem(/g' src/math/lp/static_matrix.h

%files
%license LICENSE.txt
%doc README.md RELEASE_NOTES.md
%{_bindir}/z3

%files libs
%license LICENSE.txt
%{_libdir}/libz3.so.*

%files devel
%license LICENSE.txt
%{_includedir}/z3*.h
%{_libdir}/libz3.so
%{_libdir}/pkgconfig/z3.pc
%dir %{_libdir}/cmake/z3/
%{_libdir}/cmake/z3/Z3Config.cmake
%{_libdir}/cmake/z3/Z3ConfigVersion.cmake
%{_libdir}/cmake/z3/Z3Targets*

%files -n python-%{srcname}-solver
%license LICENSE.txt
%dir %{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}/*py

%changelog
%autochangelog
