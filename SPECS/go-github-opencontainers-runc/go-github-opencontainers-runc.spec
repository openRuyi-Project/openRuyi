# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           runc
%define go_import_path  github.com/opencontainers/runc
%define go_test_include %{go_import_path}/libcontainer/user

Name:           go-github-opencontainers-runc
Version:        0.1.1
Release:        %autorelease
Summary:        Go library for spawning and running containers
License:        Apache-2.0
URL:            https://github.com/opencontainers/runc
VCS:            git:https://github.com/opencontainers/runc.git
#!RemoteAsset:  sha256:e59694701625218b26b40a8ab2401ef366a940467c61aa21c71f156ea9778f9e
Source0:        https://github.com/opencontainers/runc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n runc-0.1.1
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/opencontainers/runc) = %{version}

%description
This package provides the github.com/opencontainers/runc Go module source.

%prep -a
# Historical releases carried a Godeps workspace; do not install bundled
# dependency sources into the shared Go source path.
rm -rf Godeps/_workspace

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
