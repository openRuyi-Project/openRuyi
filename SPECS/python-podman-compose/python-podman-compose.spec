# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname podman-compose
%global pypi_name podman_compose

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        A script to run docker-compose.yml using podman
License:        GPL-2.0
URL:            https://github.com/containers/podman-compose
#!RemoteAsset:  sha256:c83fd9bcbaa635100d581ce52a7a4b712ee0d457481232aff392efe3ebc5a217
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Requires:       podman

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An implementation of Compose Spec with Podman backend. This project focuses on:
rootless and daemon-less process model, we directly execute podman, no running daemon.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/podman-compose

%changelog
%autochangelog
