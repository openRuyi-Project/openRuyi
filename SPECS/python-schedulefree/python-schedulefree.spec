# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname schedulefree

Name:           python-%{srcname}
Version:        1.4.1
Release:        %autorelease
Summary:        Schedule Free Learning in PyTorch
License:        Apache-2.0
URL:            https://github.com/facebookresearch/schedule_free
#!RemoteAsset:  sha256:69ef25601d1fc0d8dd00cb36f9af78833f88b7846f1bb6ddecc9f144f3e9f7cb
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# No module named 'algoperf'
BuildOption(check):  -e schedulefree.algoperf.external_tuning*
BuildOption(check):  -e schedulefree.algoperf.self_tuning.schedule_free_adamw.submission

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Schedule-Free Optimizers in PyTorch.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
