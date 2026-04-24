# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gcloud-aio-auth
%global pypi_name gcloud_aio_auth

Name:           python-%{srcname}
Version:        5.4.4
Release:        %autorelease
Summary:        Async Google Cloud authentication library
License:        MIT
URL:            https://github.com/talkiq/gcloud-aio
#!RemoteAsset:  sha256:70b8c6edf8655003251905372e6815a24ab839bf201788a903964570e9b4091f
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  gcloud

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(backoff)
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pyjwt)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Async Google Cloud authentication library for Python, providing token
management and service account authentication for GCP services.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
