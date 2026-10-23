# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname docker

Name:           python-%{srcname}
Version:        7.2.0
Release:        %autorelease
Summary:        Python library for the Docker Engine API
License:        Apache-2.0
URL:            https://github.com/docker/docker-py
#!RemoteAsset:  sha256:cebb93773d334f778e023a7ee352a8d6e13ab1bd3b863a4d4a59dec897df43ac
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:33487af5bead23974df76aa9e7e44cb555ee939883b9d42a368ce71fb6c18916
Source1:        https://github.com/docker/docker-py/archive/refs/tags/%{version}.tar.gz#/docker-py-%{version}-tests.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Named-pipe transports are Windows-only; SSH requires the optional paramiko extra.
BuildOption(check):  -e 'docker.transport.npipe*' -e docker.transport.sshconn

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A Python library for the Docker Engine API. It lets you do anything the `docker` command does, but from within Python apps – run containers, manage containers, manage Swarms, etc.

%prep -a
tar -xf %{SOURCE1} --strip-components=1 docker-py-%{version}/tests

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest tests/unit/utils_test.py

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
