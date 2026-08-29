# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname peft

Name:           python-%{srcname}
Version:        0.19.1
Release:        %autorelease
Summary:        State-of-the-art Parameter-Efficient Fine-Tuning
License:        Apache-2.0
URL:            https://github.com/huggingface/peft
#!RemoteAsset:  sha256:0d97542fe96dcdaa20d3b81c06f26f988618f416a73544ab23c3618ccb674a40
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e peft.tuners.*.bnb

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(attrs)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
State-of-the-art Parameter-Efficient Fine-Tuning (PEFT) methods.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
