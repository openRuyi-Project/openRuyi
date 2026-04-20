# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname uritemplate

Name:           python-%{srcname}
Version:        4.2.0
Release:        %autorelease
Summary:        URI template parsing per RFC6570
License:        BSD-3-Clause OR Apache-2.0
URL:            https://github.com/python-hyper/uritemplate
#!RemoteAsset:  sha256:480c2ed180878955863323eea31b0ede668795de182617fef9c6ca09e6ec9d0e
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Simple python library to deal with URI Templates.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
