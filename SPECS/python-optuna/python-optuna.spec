# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname optuna

Name:           python-%{srcname}
Version:        4.8.0
Release:        %autorelease
Summary:        A hyperparameter optimization framework
License:        MIT
URL:            https://github.com/optuna/optuna
#!RemoteAsset:  sha256:6f7043e9f8ecb5e607af86a7eb00fb5ec2be26c3b08c201209a73d36aff37a38
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# No module named 'optuna_integration'
BuildOption(check):  -e optuna.integration.*
# `optuna.multi_objective` were deleted at v4.0.0.
BuildOption(check):  -e optuna.multi_objective

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(fakeredis)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Optuna is an automatic hyperparameter optimization software framework,
particularly designed for machine learning.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/optuna

%changelog
%autochangelog
