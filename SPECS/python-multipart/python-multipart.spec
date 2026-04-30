# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-multipart
%global pypi_name python_multipart

Name:           python-%{srcname}
Version:        0.0.22
Release:        %autorelease
Summary:        Streaming multipart parser for Python
License:        Apache-2.0
URL:            https://github.com/Kludex/python-multipart
#!RemoteAsset:  sha256:7340bef99a7e0032613f56dc36027b959fd3b30a787ed62d310e951f7c3a3a58
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} +auto
BuildOption(check):  %{pypi_name} multipart

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
python-multipart is a streaming parser for multipart/form-data content, useful
for web upload handling.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{python3_sitelib}/multipart/

%changelog
%autochangelog
