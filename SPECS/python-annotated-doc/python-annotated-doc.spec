# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname annotated-doc
%global pypi_name annotated_doc

Name:           python-%{srcname}
Version:        0.0.4
Release:        %autorelease
Summary:        Document parameters and attributes inline with Annotated
License:        MIT
URL:            https://github.com/fastapi/annotated-doc
VCS:            git:https://github.com/fastapi/annotated-doc.git
#!RemoteAsset:  sha256:fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4
Source:         https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pdm-backend)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
annotated-doc provides a way to document parameters, class attributes, return
types, and variables inline using typing.Annotated.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
