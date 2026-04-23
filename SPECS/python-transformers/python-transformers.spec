# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname transformers

Name:           python-transformers
Version:        5.2.0
Release:        %autorelease
Summary:        Model-definition framework for state-of-the-art machine learning
License:        Apache-2.0
URL:            https://pypi.org/project/transformers/
VCS:            git:https://github.com/huggingface/transformers
#!RemoteAsset:  sha256:0088b8b46ccc9eff1a1dca72b5d618a5ee3b1befc3e418c9512b35dea9f9a650
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e 'transformers.*'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Transformers provides model definitions for state-of-the-art machine learning
across text, vision, audio, video, and multimodal tasks for inference and
training.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/transformers

%changelog
%autochangelog
