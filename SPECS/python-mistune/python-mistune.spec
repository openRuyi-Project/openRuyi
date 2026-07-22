# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mistune

Name:           python-%{srcname}
Version:        3.3.3
Release:        %autorelease
Summary:        Fast and extensible Markdown parser in Python
License:        BSD-3-Clause
URL:            https://github.com/lepture/mistune
#!RemoteAsset:  sha256:c4c6c0c840b8637a2e9b8b6d607eb7c8f00888bf14c754409bcd339e848c2477
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l mistune

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Mistune is a fast and extensible Markdown parser with useful plugins and
renderers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/mistune

%changelog
%autochangelog
