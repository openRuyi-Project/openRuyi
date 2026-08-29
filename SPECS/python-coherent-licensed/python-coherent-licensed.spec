# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname coherent-licensed
%global pypi_name coherent_licensed

Name:           python-%{srcname}
Version:        0.5.2
Release:        %autorelease
Summary:        License management tooling for Coherent System and skeleton projects
License:        MIT
URL:            https://github.com/coherent-oss/coherent.licensed
#!RemoteAsset:  sha256:d8071403ce742d3ac3592ddc4fb7057a46caffb415b928b4d52802e5f208416d
Source:         https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l coherent

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This library was built for coherent.build and skeleton projects to inject a
license file at build time to reflect the license declared in the License
Expression.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
