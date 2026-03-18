# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nltk

Name:           python-%{srcname}
Version:        3.9.3
Release:        %autorelease
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            https://www.nltk.org/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  nltk
# Exclude modules requiring tkinter (GUI), twython (twitter), or NLTK data downloads
BuildOption(check):  -e 'nltk.app*' -e 'nltk.draw*' -e 'nltk.twitter*' -e 'nltk.book*' -e 'nltk.test*' -e 'nltk.langnames*' -e 'nltk.tokenize.nist*'

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(tqdm)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
NLTK -- the Natural Language Toolkit -- is a suite of open source Python
modules, data sets, and tutorials supporting research and development in
Natural Language Processing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%{_bindir}/nltk

%changelog
%{?autochangelog}
