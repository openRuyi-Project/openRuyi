# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flexparser

Name:           python-%{srcname}
Version:        0.4
Release:        %autorelease
Summary:        Parsing made fun using typing
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexparser
#!RemoteAsset:  sha256:266d98905595be2ccc5da964fe0a2c3526fbbffdc45b65b3146d75db992ef6b2
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
flexparser is a Python parsing helper library with a typed data model.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGES
%doc README.rst
%license LICENSE

%changelog
%autochangelog
