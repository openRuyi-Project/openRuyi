# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname discord.py
%global pypi_name discord_py

Name:           python-%{srcname}
Version:        2.7.1
Release:        %autorelease
Summary:        An API wrapper for Discord written in Python
License:        MIT
URL:            https://github.com/Rapptz/discord.py
#!RemoteAsset:  sha256:24d5e6a45535152e4b98148a9dd6b550d25dc2c9fb41b6d670319411641249da
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l discord
# Skip discord.types import checks: These modules contain circular dependencies for type hinting
# that fail under isolated import tests in Python 3.13, despite being functional in standard usage.
BuildOption(check):  -e discord.types.*

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An API wrapper for Discord written in Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
