# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname spacy

Name:           python-%{srcname}
Version:        3.8.11
Release:        %autorelease
Summary:        Industrial-strength Natural Language Processing (NLP) in Python
License:        MIT
URL:            https://github.com/explosion/spaCy
#!RemoteAsset:  sha256:54e1e87b74a2f9ea807ffd606166bf29ac45e2bd81ff7f608eadc7b05787d90d
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Skip tests to avoid extra dependencies
BuildOption(check):  -e "spacy.tests.*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cymem)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(murmurhash)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(preshed)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(spacy-legacy)
BuildRequires:  python3dist(spacy-loggers)
BuildRequires:  python3dist(thinc)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(typer-slim)
BuildRequires:  python3dist(weasel)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
spaCy is a library for advanced Natural Language Processing
in Python and Cython. It's built on the very latest research,
and was designed from day one to be used in real products.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/spacy

%changelog
%autochangelog
