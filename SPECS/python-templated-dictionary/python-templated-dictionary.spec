# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# This package can't use pyproject BuildSystem.

%global srcname templated-dictionary

Name:           python-%{srcname}
Version:        1.6
Release:        %autorelease
Summary:        Dictionary with Jinja2 expansion
License:        GPL-2.0-or-later
URL:            https://github.com/xsuchy/templated-dictionary
#!RemoteAsset
Source0:        %{url}/archive/refs/tags/python-%{srcname}-%{version}-1.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

Requires:       python3-jinja2

%description
Dictionary where __getitem__() is run through Jinja2 template.

%prep
%autosetup -p1 -n %{srcname}-%{name}-%{version}-1

%generate_buildrequires
%pyproject_buildrequires

%build
version="%{version}" %pyproject_wheel

%install
version="%{version}" %pyproject_install

%files
%license LICENSE
%{python3_sitelib}/templated_dictionary/
%{python3_sitelib}/*.dist-info

%changelog
%autochangelog
