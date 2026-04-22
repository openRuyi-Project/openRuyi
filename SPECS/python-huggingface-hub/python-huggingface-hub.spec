# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname huggingface_hub

Name:           python-huggingface-hub
Version:        1.5.0
Release:        %autorelease
Summary:        Client library for the Hugging Face Hub
License:        Apache-2.0
URL:            https://pypi.org/project/huggingface-hub/
VCS:            git:https://github.com/huggingface/huggingface_hub
#!RemoteAsset:  sha256:f281838db29265880fb543de7a23b0f81d3504675de82044307ea3c6c62f799d
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l huggingface_hub +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-huggingface-hub = %{version}-%{release}
%python_provide python3-huggingface-hub

%description
Hugging Face Hub client library to download and publish models, datasets,
and spaces from Python.

%prep
%autosetup -n %{srcname}-%{version}
sed -i 's/"typer",/"typer-slim",/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
