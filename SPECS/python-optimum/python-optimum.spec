# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname optimum

Name:           python-%{srcname}
Version:        2.1.0
Release:        %autorelease
Summary:        Accelerate inference and training of Transformers, Diffusers, TIMM and Sentence Transformers
License:        Apache-2.0
URL:            https://github.com/huggingface/optimum
#!RemoteAsset:  sha256:0a2a13f91500e41d34863ffdb08fcb886b3ce68a84a386e59653e3064a45dd4b
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

Patch2000:      2000-fix-utils-use-default_factory-for-mutable-dataclass-.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(optuna)
BuildRequires:  python3dist(torchvision)
BuildRequires:  python3dist(datasets)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Optimum is an extension of Transformers Diffusers TIMM and
Sentence-Transformers, providing a set of optimization tools and
enabling maximum efficiency to train and run models on targeted
hardware, while keeping things easy to use.

%pyproject_extras_subpkg -n python-optimum onnxruntime

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/optimum-cli

%changelog
%autochangelog
