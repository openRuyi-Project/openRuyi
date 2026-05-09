# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname language-tags
%global pypi_name language_tags

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        Dealing with IANA language tags in Python
License:        MIT
URL:            https://github.com/OnroerendErfgoed/language-tags
#!RemoteAsset:  sha256:b15f05505dad3ad296a1782d5a6083fd141309186094d1ab08095348f4203f37
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This Python API offers a way to validate and lookup languages tags.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
