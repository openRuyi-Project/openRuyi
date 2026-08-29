# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname awscrt

Name:           python-%{srcname}
Version:        0.32.0
Release:        %autorelease
Summary:        Python bindings for the AWS Common Runtime
License:        Apache-2.0
URL:            https://github.com/awslabs/aws-crt-python
#!RemoteAsset:  sha256:92e749fce6c61da8db1af0baa6b7e96f7acf8a5574760b3d7880d190cedee8a0
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  cmake

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python 3 bindings for the AWS Common Runtime.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{python_sitearch}/_awscrt*.so

%changelog
%autochangelog
