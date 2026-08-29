# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mistral_common

Name:           python-%{srcname}
Version:        1.11.3
Release:        %autorelease
Summary:        Mistral-common is a library of common utilities for Mistral AI
License:        Apache-2.0
URL:            https://github.com/mistralai/mistral-common
#!RemoteAsset:  sha256:6437e128fc8a307318440839ca14ddf2e8060056b062233ec0db10352651374c
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:5ed6f79e77734b5a60740dd821af5ecac9a6f33709c860eea4e20fcb6cca7fcc
Source1:        https://raw.githubusercontent.com/mistralai/mistral-common/refs/tags/v1.11.3/LICENCE
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(fastapi)
BuildRequires:  python3dist(pydantic-settings)
BuildRequires:  python3dist(uvicorn)

Requires:       python3dist(click)
Requires:       python3dist(fastapi)
Requires:       python3dist(pydantic-settings)
Requires:       python3dist(uvicorn)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
mistral-common is a set of tools to help you work with Mistral AI models.

%prep -a
cp %{SOURCE1} LICENSE

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/mistral_common

%changelog
%autochangelog
