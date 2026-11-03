# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydantic-extra-types
%global pypi_name pydantic_extra_types

Name:           python-%{srcname}
Version:        2.11.2
Release:        %autorelease
Summary:        Extra Pydantic types
License:        MIT
URL:            https://github.com/pydantic/pydantic-extra-types
#!RemoteAsset:  sha256:3a2b83b61fe920925688e7838b59caa90a45637d1dbba2b1364b8d1f7ff72a0a
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
# No module named 'pendulum'
BuildOption(check):  -e pydantic_extra_types.pendulum_dt

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pycountry)
BuildRequires:  python3dist(cron-converter)
BuildRequires:  python3dist(pymongo)
BuildRequires:  python3dist(phonenumbers)
BuildRequires:  python3dist(semver)
BuildRequires:  python3dist(python-ulid)
BuildRequires:  python3dist(jsonschema)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A place for pydantic types that probably shouldn't exist in the main pydantic lib.

%pyproject_extras_subpkg -n python-%{srcname} phonenumbers pycountry semver python_ulid cron

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
