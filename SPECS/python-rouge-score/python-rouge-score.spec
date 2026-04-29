# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rouge-score
%global pypi_name rouge_score

Name:           python-%{srcname}
Version:        0.1.2
Release:        %autorelease
Summary:        Pure Python implementation of ROUGE-1.5.5
License:        Apache-2.0
URL:            https://github.com/google-research/google-research/tree/master/rouge
#!RemoteAsset:  sha256:c7d4da2683e68c9abf0135ef915d63a46643666f848e558a1b9f7ead17ff0f04
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(absl-py)
BuildRequires:  python3dist(nltk)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.14.0
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
rouge-score provides a pure Python implementation of ROUGE-1.5.5.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
