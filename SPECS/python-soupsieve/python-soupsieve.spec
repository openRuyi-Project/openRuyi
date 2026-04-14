# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname soupsieve

Name:           python-soupsieve
Version:        2.8.3
Release:        %autorelease
Summary:        A modern CSS selector implementation for Beautiful Soup
License:        MIT
URL:            https://github.com/facelessuser/soupsieve
#!RemoteAsset:  sha256:3267f1eeea4251fb42728b6dfb746edc9acaffc4a45b27e19450b676586e8349
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l soupsieve

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

Provides:       python3-soupsieve = %{version}-%{release}
%python_provide python3-soupsieve

%description
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS
selectors. Soup Sieve currently provides selectors from the CSS level 1
specifications up through the latest CSS level 4 drafts and beyond (though some
are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin
select feature, and as of Beautiful Soup version 4.7.0, it now is. Soup Sieve
can also be imported in order to use its API directly for more controlled,
specialized parsing.

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%check -a
%if %{with tests}
%pytest
%endif

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
