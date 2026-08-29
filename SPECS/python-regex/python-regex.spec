# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname regex

Name:           python-%{srcname}
Version:        2026.1.15
Release:        %autorelease
Summary:        Alternative regular expression module for Python
License:        Apache-2.0
URL:            https://github.com/mrabarnett/mrab-regex
#!RemoteAsset:  sha256:164759aa25575cbc0651bef59a0b18353e54300d79ace8084c818ad8ac72b7d5
Source:         https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An alternate regex implementation. It differs from "re" in that

* Zero-width matches are handled like in Perl and PCRE:
  * ``.split`` will split a string at a zero-width match.
  * ``.sub`` will handle zero-width matches correctly.
* Inline flags apply to the end of the group or pattern, and they can
  be turned off.
* Nested sets and set operations are supported.
* Case-insensitive matches in Unicode use full case-folding by
  default.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
