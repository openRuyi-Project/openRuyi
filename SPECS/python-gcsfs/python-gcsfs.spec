# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gcsfs

Name:           python-%{srcname}
Version:        2026.6.0
Release:        %autorelease
Summary:        Fsspec interface for Google Cloud Storage
License:        BSD-3-Clause
URL:            https://github.com/fsspec/gcsfs
#!RemoteAsset:  sha256:bfb1f912b3f51006b00bcd5fcef915214cb51f8b892a3974178430a55990ba3f
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
BuildOption(check):    -e %{srcname}.cli.gcsfuse

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(aiohttp) >= 3.9
BuildRequires:  python3dist(decorator) > 4.1.2
BuildRequires:  python3dist(fsspec) >= 2026.3
BuildRequires:  python3dist(google-auth) >= 1.2
BuildRequires:  python3dist(google-auth-oauthlib)
BuildRequires:  python3dist(google-cloud-storage) >= 3.11
BuildRequires:  python3dist(google-cloud-storage-control)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling) >= 1.27
BuildRequires:  python3dist(requests)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Gcsfs provides an asynchronous fsspec-compatible filesystem for Google Cloud
Storage.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
