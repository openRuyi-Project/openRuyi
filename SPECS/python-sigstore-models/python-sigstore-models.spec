# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sigstore-models
%global pypi_name sigstore_models

Name:           python-%{srcname}
Version:        0.0.6
Release:        %autorelease
Summary:        Pydantic models for Sigstore protobuf specifications
License:        MIT
URL:            https://github.com/astral-sh/sigstore-models
VCS:            git:https://github.com/astral-sh/sigstore-models.git
#!RemoteAsset:  sha256:c766c09470c2a7e8a4a333c893f07e2001c56a3ff1757b1a246119f53169a849
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pydantic) >= 2.12
BuildRequires:  python3dist(typing-extensions) >= 4.14.1

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python models for Sigstore's protobuf specifications, implemented with
Pydantic.

%prep -a
# Use the packaged pure-Python backend because uv_build is not packaged.
sed -i 's/uv_build>=0.9.0,<0.10/hatchling/' pyproject.toml
sed -i 's/uv_build/hatchling.build/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
