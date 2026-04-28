# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyctcdecode

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        CTC beam search decoder for speech recognition
License:        Apache-2.0
URL:            https://github.com/kensho-technologies/pyctcdecode
VCS:            git:https://github.com/kensho-technologies/pyctcdecode.git
#!RemoteAsset:  sha256:f3bcb313e43ca16a54938b3e77b0b375328653bba932668243db745fde513a2c
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(numpy)
Requires:       python3dist(pygtrie) < 3

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pyctcdecode provides a CTC beam search decoder for speech recognition models.
It integrates language model scoring and prefix trie based decoding in Python.

%prep -a
# openRuyi currently ships NumPy 2.x, so relax the upstream upper bound.
sed -i 's/numpy>=1.15.0,<2.0.0/numpy>=1.15.0/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
