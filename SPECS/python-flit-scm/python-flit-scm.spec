# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flit_scm

Name:           python-flit-scm
Version:        1.7.0
Release:        %autorelease
Summary:        PEP 518 build backend that uses setuptools_scm and flit
License:        MIT
URL:            https://gitlab.com/WillDaSilva/flit_scm
#!RemoteAsset:  sha256:961bd6fb24f31bba75333c234145fff88e6de0a90fc0f7e5e7c79deca69f6bb2
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-flit-scm = %{version}-%{release}
%python_provide python3-flit-scm

%description
A PEP 518 build backend that uses setuptools_scm to generate a version file
from your version control system, then flit_core to build the package.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
