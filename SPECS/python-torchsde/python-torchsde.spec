# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname torchsde

Name:           python-%{srcname}
Version:        0.2.6
Release:        %autorelease
Summary:        SDE solvers and stochastic adjoint sensitivity analysis in PyTorch.
License:        Apache-2.0
URL:            https://github.com/google-research/torchsde
#!RemoteAsset:  sha256:81d074d3504f9d190f1694fb526395afbe4608ee43a88adb1262a639e5b4778b
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Differentiable stochastic differential equation solvers with GPU support
and efficient backpropagation for PyTorch.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
