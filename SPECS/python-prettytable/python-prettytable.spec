# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname prettytable

Name:           python-%{srcname}
Version:        3.17.0
Release:        %autorelease
Summary:        Python library to display tabular data in tables
License:        BSD-3-Clause
URL:            https://github.com/jazzband/prettytable
#!RemoteAsset:  sha256:59f2590776527f3c9e8cf9fe7b66dd215837cca96a9c39567414cbc632e8ddb0
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.

%generate_buildrequires
%pyproject_buildrequires -r

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
