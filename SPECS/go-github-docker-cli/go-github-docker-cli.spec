# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cli
%define go_import_path  github.com/docker/cli
%define go_test_include %{shrink:
    %{go_import_path}/cli/config
    %{go_import_path}/cli/config/configfile
    %{go_import_path}/cli/config/credentials
    %{go_import_path}/cli/config/types
}

Name:           go-github-docker-cli
Version:        0+git20200130.5d0cf88
Release:        %autorelease
Summary:        This repository is the home of the Docker CLI
License:        Apache-2.0
URL:            https://github.com/docker/cli
VCS:            git:https://github.com/docker/cli.git
#!RemoteAsset:  sha256:76c901ade65584122e2781f978fefceef33081c09ac4f025e0778b32eb77a42c
Source0:        https://github.com/docker/cli/archive/5d0cf8839492.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n cli-5d0cf8839492eb1af7c611a58d09034d29aa9631
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/docker/docker)
BuildRequires:  go(github.com/docker/docker-credential-helpers)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(gotest.tools/assert)

Provides:       go(github.com/docker/cli) = %{version}

Requires:       go(github.com/docker/docker)
Requires:       go(github.com/docker/docker-credential-helpers)
Requires:       go(github.com/pkg/errors)

%description
This package provides the github.com/docker/cli Go module source.

%prep -a
# Do not install a nested vendor tree into the shared Go source path.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
