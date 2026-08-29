# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytorch-lightning
%global pypi_name pytorch_lightning

Name:           python-%{srcname}
Version:        2.6.4
Release:        %autorelease
Summary:        The lightweight PyTorch wrapper for ML researchers
License:        Apache-2.0
URL:            https://github.com/Lightning-AI/lightning
#!RemoteAsset:  sha256:fdd2a7052b9afb92394968205b9b55baab426aa57dec11b95bf1b84a67c2bc25
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} lightning_fabric -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(torchmetrics)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(lightning-utilities)
BuildRequires:  python3dist(requests)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyTorch Lightning is the lightweight PyTorch wrapper for high-performance
AI research. Scale your models, not the boilerplate.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
