# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname FlagEmbedding

Name:           python-%{srcname}
Version:        1.3.5
Release:        %autorelease
Summary:        Embedding toolkit for BAAI general embedding models
License:        MIT
URL:            https://github.com/FlagOpen/FlagEmbedding
VCS:            git:https://github.com/FlagOpen/FlagEmbedding
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/F/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(torch) >= 1.6
BuildRequires:  python3dist(transformers) >= 4.18
BuildRequires:  python3dist(datasets)
BuildRequires:  python3dist(accelerate) >= 0.20

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
FlagEmbedding is a Python toolkit for using BAAI general embedding models
for semantic search and retrieval tasks.

%generate_buildrequires
%pyproject_buildrequires

%check
# Skip import checks in current staging project.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%{?autochangelog}
