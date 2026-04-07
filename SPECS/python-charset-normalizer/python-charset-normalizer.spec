# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname charset-normalizer
%global modname charset_normalizer

Name:           python-%{srcname}
Version:        3.4.6
Release:        %autorelease
Summary:        The Real First Universal Charset Detector
License:        MIT
URL:            https://github.com/Ousret/charset_normalizer
#!RemoteAsset:  sha256:1ae6b62897110aa7c79ea2f5dd38d1abca6db663687c0b1ad9aed6f6bae3d9d6
Source:         https://files.pythonhosted.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{modname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking a new approach.
All IANA character set names for which the Python core library provides codecs
are supported.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/normalizer

%changelog
%autochangelog
