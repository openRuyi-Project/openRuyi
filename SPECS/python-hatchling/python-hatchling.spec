# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hatchling

Name:           python-%{srcname}
Version:        1.29.0
Release:        %autorelease
Summary:        The build backend used by Hatch
License:        MIT
URL:            https://pypi.org/project/hatchling
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:793c31816d952cee405b83488ce001c719f325d9cda69f1fc4cd750527640ea6
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l hatchling

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pathspec)
BuildRequires:  python3dist(pluggy)
BuildRequires:  python3dist(trove-classifiers)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is the extensible, standards compliant build backend used by Hatch.

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/hatchling

%changelog
%autochangelog
