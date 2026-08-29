# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname soupsieve

Name:           python-%{srcname}
Version:        2.8.4
Release:        %autorelease
Summary:        CSS selector library for Beautiful Soup
License:        MIT
URL:            https://github.com/facelessuser/soupsieve
#!RemoteAsset:  sha256:e121fd02e975c695e4e9e8774a5ee35d74714b59307868dcc5319ad2d9e3328e
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup.

%generate_buildrequires
%pyproject_buildrequires

# soupsieve and beautifulsoup4 have a circular build dependency.
# Skip %%check to break the cycle.
%check

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
%autochangelog
