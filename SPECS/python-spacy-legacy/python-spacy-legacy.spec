# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname spacy_legacy

Name:           python-spacy-legacy
Version:        3.0.12
Release:        %autorelease
Summary:        Legacy registered functions for spaCy backwards compatibility
License:        MIT
URL:            https://github.com/explosion/spacy-loggers
#!RemoteAsset:  sha256:b37d6e0c9b6e1d7ca1cf5bc7152ab64a4c4671f59c85adaf7a3fcb870357a774
Source0:        https://files.pythonhosted.org/packages/source/s/spacy_legacy/spacy-legacy-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package includes outdated registered functions
for spaCy v3.x, for example model architectures, pipeline
components and utilities.

%generate_buildrequires
%pyproject_buildrequires

%check
# Skip the check; it depends on the spacy

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
