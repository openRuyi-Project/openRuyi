# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pybind11

Name:           pybind11
Version:        3.0.1
Release:        %autorelease
Summary:        Seamless operability between C++11 and Python
License:        BSD-3-Clause
URL:            https://github.com/pybind/pybind11
#!RemoteAsset:  sha256:9c0f40056a016da59bab516efb523089139fcc6f2ba7e4930854c61efb932051
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE:STRING=Release
BuildOption(conf):  -DUSE_PYTHON_INCLUDE_DIR=FALSE

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(scikit-build-core)
BuildRequires:  python3dist(tomlkit)
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(pytest)
BuildRequires:  ninja

%description
pybind11 is a lightweight header-only library that exposes C++ types
in Python and vice versa, mainly to create Python bindings of existing
C++ code.

%package        devel
Summary:        Development headers for pybind11

%description    devel
This package contains the development headers for pybind11.

%package     -n python-%{srcname}
Summary:        Python 3 bindings for pybind11
Requires:       %{name}-devel = %{version}-%{release}
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description -n python-%{srcname}
This package contains the Python 3 files for pybind11.

%generate_buildrequires
%pyproject_buildrequires -g test

%build -a
%{pyproject_wheel %{shrink:
  -C cmake.build-type=Release
  -C cmake.define.PYBIND11_INSTALL=OFF
  -C cmake.define.PYBIND11_TEST=OFF
}}

%install -a
%pyproject_install
%pyproject_save_files -l pybind11

%check
%cmake_build --target check

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/pybind11/
%{_datadir}/cmake/pybind11/
%{_bindir}/pybind11-config
%{_datadir}/pkgconfig/pybind11.pc

%files -n python-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
