# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname schedulefree

Name:           python-%{srcname}
Version:        1.4.1
Release:        %autorelease
Summary:        Schedule-free optimizers for PyTorch
License:        Apache-2.0
URL:            https://github.com/facebookresearch/schedule_free
#!RemoteAsset:  sha256:69ef25601d1fc0d8dd00cb36f9af78833f88b7846f1bb6ddecc9f144f3e9f7cb
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Exclude the packaged test module and the bundled algoperf experiment tree.
# The algoperf modules import undeclared research-only dependencies such as
# algorithmic_efficiency and are not part of the base runtime dependency set.
BuildOption(install):  -l %{srcname}
BuildOption(check):  -e schedulefree.test_schedulefree
BuildOption(check):  -e "schedulefree.algoperf*"
BuildOption(check):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(absl-py)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
schedulefree provides schedule-free optimizers for PyTorch.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
