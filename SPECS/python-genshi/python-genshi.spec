# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname genshi

Name:           python-%{srcname}
Version:        0.7.10
Release:        %autorelease
Summary:        Toolkit for stream-based generation of output for the web
License:        BSD-3-Clause
URL:            https://genshi.edgewall.org/
#!RemoteAsset:  sha256:85b0db113625314f0f44f3fe6ef0eb2564d6c34dd2ee5677b495d15142bb4973
Source:         https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or other
textual content for output generation on the web.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest

%files -f %{pyproject_files}
%doc ChangeLog doc examples README.md
%license COPYING

%changelog
%autochangelog
