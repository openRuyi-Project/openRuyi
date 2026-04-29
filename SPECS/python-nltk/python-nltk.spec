# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nltk

Name:           python-%{srcname}
Version:        3.9.4
Release:        %autorelease
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            https://www.nltk.org/
#!RemoteAsset:  sha256:ed03bc098a40481310320808b2db712d95d13ca65b27372f8a403949c8b523d0
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  nltk
# Exclude modules requiring tkinter (_tkinter C extension unavailable),
# twython (unmaintained), pytest (test-only), or NLTK corpus data
BuildOption(check):  -e 'nltk.app*' -e 'nltk.draw*' -e 'nltk.twitter*' -e 'nltk.test*' -e 'nltk.book' -e 'nltk.langnames' -e 'nltk.tokenize.nist'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(tqdm)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
NLTK -- the Natural Language Toolkit -- is a suite of open source Python
modules, data sets, and tutorials supporting research and development in
Natural Language Processing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS.md ChangeLog README.md
%license LICENSE.txt
%{_bindir}/nltk

%changelog
%autochangelog
