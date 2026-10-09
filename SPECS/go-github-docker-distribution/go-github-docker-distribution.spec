# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           distribution
%define go_import_path  github.com/docker/distribution
%define go_test_include  %{go_import_path}/reference

Name:           go-github-docker-distribution
Version:        2.7.1
Release:        %autorelease
Summary:        Docker distribution Go module
License:        Apache-2.0
URL:            https://github.com/docker/distribution
VCS:            git:https://github.com/docker/distribution.git
#!RemoteAsset:  sha256:4c3609c102351f15c0386f619d48bb592f3100726b4bde86f3eba7739192ff55
Source0:        https://github.com/docker/distribution/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n distribution-2.7.1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/docker/go-metrics)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)

Provides:       go(github.com/docker/distribution) = %{version}

Requires:       go(github.com/docker/go-metrics)
Requires:       go(github.com/gorilla/mux)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)

%description
This package provides the github.com/docker/distribution Go module source.

%prep -a
# Do not install a nested vendor tree into downstream multi-architecture builds.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
