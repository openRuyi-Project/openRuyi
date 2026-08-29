# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname spacy_loggers

Name:           python-spacy-loggers
Version:        1.0.5
Release:        %autorelease
Summary:        Logging utilities for SpaCy
License:        MIT
URL:            https://github.com/explosion/spacy-loggers
#!RemoteAsset:  sha256:d60b0bdbf915a60e516cc2e653baeff946f0cfc461b452d11a4d5458c6fe5f24
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/spacy-loggers-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Starting with spaCy v3.2, alternate loggers are moved into
a separate package so that they can be added and updated
independently from the core spaCy library.

%check
# Skip the check; it depends on the spacy.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
