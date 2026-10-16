# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname s3fs

Name:           python-%{srcname}
Version:        2026.6.0
Release:        %autorelease
Summary:        S3 Filesystem
License:        BSD-3-Clause
URL:            https://github.com/fsspec/s3fs/
#!RemoteAsset:  sha256:b28de7082d0a4f72392884bdc497e34a4a1582f675d214c7da0acf6e950a0083
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
S3FS builds on aiobotocore to provide a convenient Python filesystem interface for S3.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
