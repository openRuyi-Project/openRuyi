# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname diffusers

Name:           python-%{srcname}
Version:        0.37.0
Release:        %autorelease
Summary:        State-of-the-art diffusion models for image, audio, and molecular generation
License:        Apache-2.0
URL:            https://github.com/huggingface/diffusers
#!RemoteAsset:  sha256:c6cafeb0193fdee812aa3fde5e48c6be6023608877549a421dc4581b75c94ed9
Source0:        https://github.com/huggingface/diffusers/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e 'diffusers.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Diffusers is the go-to library for state-of-the-art pretrained diffusion
models for generating images, audio, and even 3D structures of molecules.

%generate_buildrequires
%pyproject_buildrequires -r

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/diffusers-cli

%changelog
%autochangelog
