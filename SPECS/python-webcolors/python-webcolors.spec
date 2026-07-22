# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname webcolors

Name:           python-%{srcname}
Version:        25.10.0
Release:        %autorelease
Summary:        Library for HTML and CSS color formats
License:        BSD-3-Clause
URL:            https://github.com/ubernostrum/webcolors
#!RemoteAsset:  sha256:62abae86504f66d0f6364c2a8520de4a0c47b80c03fc3a5f1815fedbef7c19bf
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  webcolors

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pdm-backend)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
webcolors converts and normalizes color formats defined by HTML and CSS.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
