# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname google-resumable-media
%global pypi_name google_resumable_media

Name:           python-%{srcname}
Version:        2.10.2
Release:        %autorelease
Summary:        Resumable media transfer helpers for Google APIs
License:        Apache-2.0
URL:            https://github.com/googleapis/google-resumable-media-python
#!RemoteAsset:  sha256:1de441703cd298d75a419bfdc0066e9fc7b0a1de630df96eea8ce8f5c759358c
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l google +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(google-crc32c) >= 1
BuildRequires:  python3dist(requests) >= 2.18
BuildRequires:  python3dist(requests) < 3
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Google Resumable Media provides helpers for resumable uploads and downloads
used by Google API client libraries.

%pyproject_extras_subpkg -n python-%{srcname} requests

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
