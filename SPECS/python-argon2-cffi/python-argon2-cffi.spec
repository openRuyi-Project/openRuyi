# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname argon2-cffi
%global pypi_name argon2_cffi

Name:           python-%{srcname}
Version:        25.1.0
Release:        %autorelease
Summary:        Secure Argon2 password hashing library for Python
License:        MIT
URL:            https://github.com/hynek/argon2-cffi
#!RemoteAsset:  sha256:694ae5cc8a42f4c4e2bf2ca0e64e51e23a040c6a517a85074683d3959e1346c1
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l argon2

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(argon2-cffi-bindings)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
argon2-cffi provides secure Argon2 password hashing and verification for
Python, backed by low-level CFFI bindings.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
