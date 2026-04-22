# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname build

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        Simple Python PEP 517 package builder
License:        MIT
URL:            https://pypa-build.readthedocs.io/en/latest/
#!RemoteAsset:  sha256:698edd0ea270bde950f53aed21f3a0135672206f3911e0176261a31e0e07b397
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  build +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The build command invokes the PEP 517 hooks to
build a distribution package.  It is a simple build tool and does not perform
any dependency management.  It aims to keep dependencies to a minimum, in
order to make bootstrapping easier.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*
%license LICENSE

%changelog
%autochangelog
