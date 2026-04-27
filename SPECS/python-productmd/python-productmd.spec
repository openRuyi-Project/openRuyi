# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname productmd

Name:           python-%{srcname}
Version:        1.50
Release:        %autorelease
Summary:        Product, compose and installation media metadata library
License:        LGPL-2.1-only
URL:            https://github.com/release-engineering/productmd
#!RemoteAsset:  sha256:a27df6835de352b6ad06e0781c83105037069b99350c0ed294e8a5c7fd379aba
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python library providing parsers for metadata related to composes
and installation media.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS
%license LICENSE

%changelog
%autochangelog
