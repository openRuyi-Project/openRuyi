# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nltk

Name:           python-%{srcname}
Version:        3.9.2
Release:        %autorelease
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            https://www.nltk.org/
#!RemoteAsset:  sha256:0f409e9b069ca4177c1903c3e843eef90c7e92992fa4931ae607da6de49e1419
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Exclude modules that require external NLTK corpora or optional integrations
# during import. Keep the rest of the runtime surface under import checking.
BuildOption(install):  -l %{srcname}
BuildOption(check):  -e nltk.book
BuildOption(check):  -e nltk.langnames
BuildOption(check):  -e nltk.tokenize.nist
BuildOption(check):  -e "nltk.test*"
BuildOption(check):  -e "nltk.app*"
BuildOption(check):  -e "nltk.draw*"
BuildOption(check):  -e "nltk.twitter*"
BuildOption(check):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(regex) >= 2021.8.3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
NLTK provides a broad collection of libraries and tools for natural language
processing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md AUTHORS.md ChangeLog SECURITY.md
%license LICENSE.txt
%{_bindir}/nltk

%changelog
%autochangelog
