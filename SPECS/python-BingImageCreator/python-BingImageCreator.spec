# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname BingImageCreator

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        High quality image generation by Microsoft Bing Image Creator
License:        Unlicense
URL:            https://github.com/acheong08/BingImageCreator
#!RemoteAsset:  sha256:e15798b7c0394145b334d0b3bef4aad187d5e7e0c3f7b6d949e413fe11b5ea47
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(requests)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
High quality image generation by Microsoft Bing Image Creator.
This package provides a Python API and CLI tool to interact with Bing's
Image Creator service.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
