# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname looseversion

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        Version numbering for anarchists and software realists
License:        PSF-2.0
URL:            https://github.com/effigies/looseversion
#!RemoteAsset:  sha256:ebde65f3f6bb9531a81016c6fef3eb95a61181adc47b7f949e9c0ea47911669e
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A backwards/forwards-compatible fork of distutils.version.LooseVersion, for
times when PEP-440 isnt what you need.

The goal of this package is to be a drop-in replacement for the original
LooseVersion. It implements an identical interface and comparison logic to
LooseVersion.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGES.md
%license LICENSE

%changelog
%{?autochangelog}
