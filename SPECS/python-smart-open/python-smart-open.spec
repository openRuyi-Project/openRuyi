# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname smart-open
%global pypi_name smart_open

Name:           python-%{srcname}
Version:        7.6.1
Release:        %autorelease
Summary:        Python utils for streaming large files
License:        MIT
URL:            https://github.com/piskvorky/smart_open
#!RemoteAsset:  sha256:4347996e7ba21db7cd1e059632e0b30395407e4f6c660d2ddffc8f2a9ae5f990
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(wrapt)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
smart_open is a Python library for efficient streaming of very large files
from/to storages such as S3, GCS, Azure Blob Storage, HDFS, WebHDFS, HTTP,
HTTPS, SFTP, or local filesystem.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
