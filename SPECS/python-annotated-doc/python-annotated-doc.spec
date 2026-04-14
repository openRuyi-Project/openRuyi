# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname annotated-doc
%global pypi_srcname annotated_doc

Name:           python-%{srcname}
Version:        0.0.4
Release:        %autorelease
Summary:        Inline documentation helper based on Annotated
License:        MIT
URL:            https://github.com/fastapi/annotated-doc
VCS:            git:https://github.com/fastapi/annotated-doc.git
#!RemoteAsset:  sha256:fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_srcname}/%{pypi_srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Switch from pdm-backend to setuptools for the openRuyi buildroot.
Patch0:         2000-python-annotated-doc-switch-to-setuptools-build-back.patch

BuildOption(install):  -l annotated_doc

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Document parameters, class attributes, return types, and variables inline
with Annotated.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
