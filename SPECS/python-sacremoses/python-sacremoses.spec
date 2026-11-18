# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sacremoses

Name:           python-%{srcname}
Version:        0.2.0
Release:        %autorelease
Summary:        Moses-based text preprocessing utilities
License:        MIT
URL:            https://github.com/hplt-project/sacremoses
#!RemoteAsset:  sha256:5aec4792efc2726710243d3566b381990e6b678cb1fd7b9d2dae216b4b8f1b1e
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# sacremoses.sent_tokenize raises NotImplementedError at import time by design,
# so exclude it from the import smoke test.
BuildOption(install):  -l %{srcname}
BuildOption(check):  -e sacremoses.sent_tokenize %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
sacremoses provides Moses-based text preprocessing utilities.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sacremoses

%changelog
%autochangelog
