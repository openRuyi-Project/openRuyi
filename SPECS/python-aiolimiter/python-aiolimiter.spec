# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiolimiter

Name:           python-%{srcname}
Version:        1.2.1
Release:        %autorelease
Summary:        An efficient implementation of a rate limiter for asyncio
License:        MIT
URL:            https://github.com/mjpieters/aiolimiter
#!RemoteAsset:  sha256:e02a37ea1a855d9e832252a105420ad4d15011505512a1a1d814647451b5cca9
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  aiolimiter

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An efficient implementation of a rate limiter for asyncio, compatible with
the asyncio.Semaphore interface.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
