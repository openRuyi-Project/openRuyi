# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest_asyncio

Name:           python-pytest-asyncio
Version:        1.3.0
Release:        %autorelease
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Summary:        Pytest support for asyncio
#!RemoteAsset:  sha256:d7f52f36d231b80ee124cd216ffb19369aa168fc10095013c6b014a34d3ee9e5
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-pytest-asyncio = %{version}-%{release}
%python_provide python3-pytest-asyncio

%description
Python asyncio code is usually written in the form of
coroutines, which makes it slightly more difficult to test using normal
testing tools.  pytest-asyncio provides useful fixtures and markers
to make testing async code easier.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE

%changelog
%autochangelog
