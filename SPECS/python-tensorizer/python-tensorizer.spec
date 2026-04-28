# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tensorizer

Name:           python-%{srcname}
Version:        2.12.0
Release:        %autorelease
Summary:        Module, Model, and Tensor Serialization/Deserialization
License:        MIT
URL:            https://github.com/coreweave/tensorizer
#!RemoteAsset:  sha256:1c724b4ba1c7f057530ccdbe7694efcbbf36f3e836ddf696eae35c9dc3e28132
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(hiredis)
BuildRequires:  python3dist(libnacl)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(redis)
BuildRequires:  python3dist(torch)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Module, Model, and Tensor Serialization/Deserialization.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
