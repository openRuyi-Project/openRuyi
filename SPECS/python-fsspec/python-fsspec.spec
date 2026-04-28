# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fsspec

Name:           python-%{srcname}
Version:        2026.2.0
Release:        %autorelease
Summary:        File-system specification for Python
License:        BSD-3-Clause
URL:            https://pypi.org/project/fsspec/
VCS:            git:https://github.com/fsspec/filesystem_spec
#!RemoteAsset:  sha256:6544e34b16869f5aacd5b90bdf1a71acb37792ea3ddf6125ee69a22a53fb8bff
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
BuildOption(check):  -e 'fsspec.tests.*' -e 'fsspec.implementations.*' -e fsspec.conftest -e fsspec.fuse -e fsspec.gui

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling) >= 1.27

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Fsspec provides a unified Python interface for local, remote, and embedded
filesystems.

%pyproject_extras_subpkg -n python3-%{srcname} abfs
%pyproject_extras_subpkg -n python3-%{srcname} adl
%pyproject_extras_subpkg -n python3-%{srcname} arrow
%pyproject_extras_subpkg -n python3-%{srcname} dask
%pyproject_extras_subpkg -n python3-%{srcname} dev
%pyproject_extras_subpkg -n python3-%{srcname} doc
%pyproject_extras_subpkg -n python3-%{srcname} dropbox
%pyproject_extras_subpkg -n python3-%{srcname} full
%pyproject_extras_subpkg -n python3-%{srcname} fuse
%pyproject_extras_subpkg -n python3-%{srcname} gcs
%pyproject_extras_subpkg -n python3-%{srcname} git
%pyproject_extras_subpkg -n python3-%{srcname} github
%pyproject_extras_subpkg -n python3-%{srcname} gs
%pyproject_extras_subpkg -n python3-%{srcname} gui
%pyproject_extras_subpkg -n python3-%{srcname} hdfs
%pyproject_extras_subpkg -n python3-%{srcname} http
%pyproject_extras_subpkg -n python3-%{srcname} libarchive
%pyproject_extras_subpkg -n python3-%{srcname} oci
%pyproject_extras_subpkg -n python3-%{srcname} s3
%pyproject_extras_subpkg -n python3-%{srcname} sftp
%pyproject_extras_subpkg -n python3-%{srcname} smb
%pyproject_extras_subpkg -n python3-%{srcname} ssh
%pyproject_extras_subpkg -n python3-%{srcname} test
%pyproject_extras_subpkg -n python3-%{srcname} test-downstream
%pyproject_extras_subpkg -n python3-%{srcname} test-full
%pyproject_extras_subpkg -n python3-%{srcname} tqdm

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
