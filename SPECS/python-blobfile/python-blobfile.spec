# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname blobfile

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        Read GCS, ABS and local paths with the same interface
License:        Unlicense
URL:            https://github.com/blobfile/blobfile
#!RemoteAsset:  sha256:78514a9265b9aa7d4607042dc77c5e6461ab27036450ad8e1f6ef9a7f29bf958
Source:         https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pycryptodomex)
BuildRequires:  python3dist(urllib3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a library that provides a Python-like interface for reading local and
remote files (only from blob storage), with an API similar to open() as well as
some of the os.path and shutil functions. blobfile supports local paths, Google
Cloud Storage paths, and Azure Blob Storage paths.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
