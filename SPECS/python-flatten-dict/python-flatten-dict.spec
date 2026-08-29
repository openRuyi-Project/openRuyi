# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flatten-dict
%global pypi_name flatten_dict

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        A flexible utility for flattening and unflattening dict-like objects in Python
License:        MIT
URL:            https://github.com/ianlini/flatten-dict
#!RemoteAsset:  sha256:ca89664d0bc9552d525ee756726b5a755c17f65b5bf23d0a1f07841f181428b7
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A flexible utility for flattening and unflattening dict-like objects in Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
