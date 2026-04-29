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
#!RemoteAsset:  sha256:5982ccd839735be99cfd3b92a8847c6c196692f476c215da84b79d2ad12f9f1b
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
# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pybind11)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A next generation Python CMake adapter and Python API for plugins.

%prep -a
cp -p src/scikit_build_core/_vendor/pyproject_metadata/LICENSE LICENSE-pyproject-metadata

%generate_buildrequires
%pyproject_buildrequires

%if %{with test}
%check -a
%pytest -m "not network"
%endif

%files -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE-pyproject-metadata

%changelog
%autochangelog
