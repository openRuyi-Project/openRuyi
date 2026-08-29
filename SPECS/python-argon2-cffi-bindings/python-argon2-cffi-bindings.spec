# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname argon2-cffi-bindings
%global pypi_name argon2_cffi_bindings

Name:           python-%{srcname}
Version:        25.1.0
Release:        %autorelease
Summary:        Low-level CFFI bindings for Argon2
License:        MIT
URL:            https://github.com/hynek/argon2-cffi-bindings
#!RemoteAsset:  sha256:b957f3e6ea4d55d820e40ff76f450952807013d361a65d7f28acc0acbf29229d
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l _argon2_cffi_bindings
BuildOption(check):  _argon2_cffi_bindings

BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
argon2-cffi-bindings provides low-level Python CFFI bindings for the Argon2
password hashing library.

%build -p
export ARGON2_CFFI_USE_SYSTEM=1

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -v

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
