# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gcloud-aio-storage
%global pypi_name gcloud_aio_storage

Name:           python-%{srcname}
Version:        9.6.4
Release:        %autorelease
Summary:        Async Google Cloud Storage client library
License:        MIT
URL:            https://github.com/talkiq/gcloud-aio
#!RemoteAsset:  sha256:4da741e9e45f0ab5f57aa9ba2d46032dde4b80f3eb0a03de31ac741add420485
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  gcloud

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(aiofiles)
BuildRequires:  python3dist(gcloud-aio-auth)
BuildRequires:  python3dist(pyasn1-modules)
BuildRequires:  python3dist(rsa)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Async Google Cloud Storage client library for Python, providing file upload,
download, and management for Google Cloud Storage buckets.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
