# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sacrebleu

Name:           python-%{srcname}
Version:        2.6.0
Release:        %autorelease
Summary:        Reproducible BLEU, chrF, and TER score computation
License:        Apache-2.0
URL:            https://github.com/mjpost/sacrebleu
#!RemoteAsset:  sha256:91499b6cd46138d95154fff1e863c2f9be57e82f0c719d8dd718d0006cf6c566
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(numpy) >= 1.17
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(portalocker)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8
BuildRequires:  python3dist(tabulate) >= 0.8.9

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
sacrebleu provides reproducible BLEU, chrF, and TER score computation.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md DATASETS.md
%license LICENSE.txt
%{_bindir}/sacrebleu

%changelog
%autochangelog
