# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nest-asyncio
%global pypi_name nest_asyncio

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        Patch asyncio to allow nested event loops
License:        BSD-2-Clause
URL:            https://github.com/erdewit/nest_asyncio
#!RemoteAsset:  sha256:6f172d5449aca15afd6c646851f4e31e02c598d553a667e38cafa997cfec55fe
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Patch asyncio to allow nested event loops.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
