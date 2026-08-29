# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname binaryornot

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        A pure Python package to check if a file is binary or text
License:        BSD-3-Clause
URL:            https://github.com/binaryornot/binaryornot
#!RemoteAsset:  sha256:cc8d57cfa71d74ff8c28a7726734d53a851d02fad9e3a5581fb807f989f702f0
Source:         https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Ultra-lightweight pure Python package to guess whether a file is binary or
text, using a heuristic similar to Perl's pp_fttext.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/binaryornot

%changelog
%autochangelog
