# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python_discovery
%global pypi_name python-discovery

Name:           python-python-discovery
Version:        1.6.1
Release:        %autorelease
Summary:        Python interpreter discovery
License:        MIT
URL:            https://github.com/tox-dev/python-discovery
#!RemoteAsset:  sha256:cf87d3627dfb4412437fdd5b13eae402607722998d21567993aedbc59b23c15e
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
BuildOption(check):  -e 'python_discovery._windows.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{pypi_name} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
python-discovery is a library for discovering Python interpreters installed on a system.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
