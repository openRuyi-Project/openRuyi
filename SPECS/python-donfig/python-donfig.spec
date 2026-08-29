# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname donfig

Name:           python-%{srcname}
Version:        0.8.1.post1
Release:        %autorelease
Summary:        Python package for configuring a Python package
License:        MIT
URL:            https://github.com/pytroll/donfig
#!RemoteAsset:  sha256:3bef3413a4c1c601b585e8d297256d0c1470ea012afa6e8461dc28bfb7c23f52
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l donfig

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cloudpickle)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(versioneer[toml])

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Donfig is a Python package that provides configuration management for
Python applications.

%prep -a
# Remove the pinned versioneer version
sed -i 's/versioneer\[toml\]==0.28/versioneer[toml]/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
