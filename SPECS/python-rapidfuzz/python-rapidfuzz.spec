# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rapidfuzz

Name:           python-%{srcname}
Version:        3.14.5
Release:        %autorelease
Summary:        Rapid fuzzy string matching library
License:        MIT
URL:            https://github.com/rapidfuzz/RapidFuzz
#!RemoteAsset:  sha256:ba10ac57884ce82112f7ed910b67e7fb6072d8ef2c06e30dc63c0f604a112e0e
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python3dist(scikit-build-core)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
RapidFuzz is a library for fast fuzzy string matching in Python and C++.

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%doc README.md CHANGELOG.rst api_differences.md
%license LICENSE extern/rapidfuzz-cpp/LICENSE extern/taskflow/LICENSE

%changelog
%autochangelog
