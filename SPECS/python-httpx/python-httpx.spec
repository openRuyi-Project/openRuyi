# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httpx

Name:           python-%{srcname}
Version:        0.28.1
Release:        %autorelease
Summary:        HTTP client for Python
License:        BSD-3-Clause
URL:            https://github.com/encode/httpx
#!RemoteAsset:  sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python HTTP client with async support.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_bindir}/httpx

%changelog
%autochangelog
