# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname phonenumbers

Name:           python-%{srcname}
Version:        9.0.32
Release:        %autorelease
Summary:        Python port of Google's libphonenumber
License:        Apache-2.0
URL:            https://github.com/daviddrysdale/python-phonenumbers
#!RemoteAsset:  sha256:108ad0237202d2f6cf4b342fac411f22808d85187c3a366152a2af7ed3202a8e
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python version of Google's common library for parsing,
formatting, storing and validating international phone numbers.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
