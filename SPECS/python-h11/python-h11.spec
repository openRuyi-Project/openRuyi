# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname h11

Name:           python-%{srcname}
Version:        0.16.0
Release:        %autorelease
Summary:        A pure-Python, bring-your-own-I/O implementation of HTTP/11
License:        MIT
URL:            https://github.com/encode/h11
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This is a little HTTP/1.1 library written from scratch in Python, heavily
inspired by hyper-h2.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
