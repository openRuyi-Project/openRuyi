# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname typogrify

Name:           python-%{srcname}
Version:        2.1.0
Release:        %autorelease
Summary:        Filters to transform text into typographically-improved HTML
License:        BSD-3-Clause
URL:            https://github.com/justinmayer/typogrify
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# For check
BuildRequires:  pytest
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(django)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
@code{typogrify} provides a set of custom filters that automatically
apply various transformations to plain text in order to yield
typographically-improved HTML.  While often used in conjunction with Jinja and
Django template systems, the filters can be used in any environment.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%{?autochangelog}
