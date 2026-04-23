# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname orderly-set
%global pypi_name orderly_set

Name:           python-%{srcname}
Version:        5.5.0
Release:        %autorelease
Summary:        Orderly Set previously known as Ordered Set
License:        MIT
URL:            https://github.com/seperman/orderly-set
#!RemoteAsset:  sha256:e87185c8e4d8afa64e7f8160ee2c542a475b738bc891dc3f58102e654125e6ce
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Orderly Set is a package containing multiple implementations of Ordered Set.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license MIT-LICENSE

%changelog
%autochangelog
