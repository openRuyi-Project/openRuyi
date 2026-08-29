# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pycountry

Name:           python-%{srcname}
Version:        26.2.16
Release:        %autorelease
Summary:        ISO country, subdivision, language and currency definitions
License:        LGPL-2.1-only
URL:            https://github.com/pycountry/pycountry
#!RemoteAsset:  sha256:5b6027d453fcd6060112b951dd010f01f168b51b4bf8a1f1fc8c95c8d94a0801
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L
# upstream ships test modules that require pytest
BuildOption(check):  -e 'pycountry.tests.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pycountry provides ISO country, subdivision, language, currency and script
definitions together with their translations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst src/%{srcname}/COPYRIGHT.txt
%license LICENSE.txt

%changelog
%autochangelog
