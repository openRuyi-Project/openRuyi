# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scikit-build-core
%global pypi_name scikit_build_core
# skip the tests as some deps we don't have yet.
%bcond test 0

Name:           python-%{srcname}
Version:        0.11.6
Release:        %autorelease
Summary:        Build backend for CMake based projects
License:        Apache-2.0 AND MIT
URL:            https://github.com/scikit-build/scikit-build-core
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
%if %{with test}
# for tests.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pybind11)
%endif

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A next generation Python CMake adapter and Python API for plugins.

%prep -a
cp -p src/scikit_build_core/_vendor/pyproject_metadata/LICENSE LICENSE-pyproject-metadata

%generate_buildrequires
%pyproject_buildrequires

%check
%if %{with test}
%pyproject_check_import
%pytest -m "not network"
%endif

%files -f %{pyproject_files}
%license LICENSE LICENSE-pyproject-metadata
%doc README.md

%changelog
%{?autochangelog}
