# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pluggy

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        The plugin manager stripped of pytest specific details
License:        MIT
URL:            https://github.com/pytest-dev/pluggy
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pluggy

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm[toml])

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The plugin manager stripped of pytest specific details.

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
