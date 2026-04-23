# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mock

Name:           python-%{srcname}
Version:        4.0.3
Release:        %autorelease
Summary:        The Python mock library
License:        BSD-2-Clause
URL:            https://mock.readthedocs.io/en/latest/
VCS:            git:https://github.com/testing-cabal/mock.git
#!RemoteAsset:  sha256:7d3fbbde18228f4ff2f1f119a45cdffa458b4c0dee32eb4d2bb2f82554bac7bc
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
mock is a library for testing in Python.
It allows you to replace parts of your system under test
with mock objects and make assertions about how they have been used.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
