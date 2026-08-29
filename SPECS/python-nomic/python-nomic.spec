# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nomic

Name:           python-%{srcname}
Version:        3.9.0
Release:        %autorelease
Summary:        The official Nomic Python client
License:        Apache-2.0
URL:            https://github.com/nomic-ai/nomic
#!RemoteAsset:  sha256:5be6b2e39ea07cf9db386b663dac792ff6a3d91beccef8eb18820b517cd6c0b6
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  nomic

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(filetype)
BuildRequires:  python3dist(jsonlines)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(loguru)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pyjwt)
BuildRequires:  python3dist(pytorch-lightning)
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(sagemaker)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The official Python client for Nomic, providing access to Atlas for data
visualization and exploration, as well as Nomic Embed for text and image
embeddings.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/nomic

%changelog
%autochangelog
