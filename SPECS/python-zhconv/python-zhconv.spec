# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zhconv

Name:           python-%{srcname}
Version:        1.4.3
Release:        %autorelease
Summary:        A Python library for Simplified-Traditional Chinese conversion
License:        MIT
URL:            https://github.com/gumblex/zhconv
#!RemoteAsset:  sha256:ad42d9057ca0605f8e41d62b67ca797f879f58193ee6840562c51459b2698c45
Source:         https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A Python library for conversion between Simplified and Traditional Chinese
based on MediaWiki and OpenCC conversion tables.

It supports maximum forward matching and regional vocabulary conversion
for multiple variants, including zh-cn, zh-tw, zh-hk, zh-sg, zh-hans,
and zh-hant. It also fully supports MediaWiki's manual conversion syntax.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
