# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname editdistance

Name:           python-%{srcname}
Version:        0.8.1
Release:        %autorelease
Summary:        Fast implementation of the edit distance (Levenshtein distance)
License:        MIT
URL:            https://github.com/roy-ht/editdistance
#!RemoteAsset:  sha256:d1cdf80a5d5014b0c9126a69a42ce55a457b457f6986ff69ca98e4fe4d2d8fed
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pdm-backend)
BuildRequires:  python3dist(wheel)
BuildRequires:  gcc-c++
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Fast implementation of the edit distance (Levenshtein distance).
This library simply implements Levenshtein distance with C++ and Cython.

%generate_buildrequires
%pyproject_buildrequires

%install -a
find %{buildroot}%{python3_sitearch} -type f \( \
    -name '.git*' \) -print -delete

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
