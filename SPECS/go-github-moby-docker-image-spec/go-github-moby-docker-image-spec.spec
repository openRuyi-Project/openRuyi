# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           docker-image-spec
%define go_import_path  github.com/moby/docker-image-spec

Name:           go-github-moby-docker-image-spec
Version:        1.3.1
Release:        %autorelease
Summary:        Docker Image Specification v1
License:        Apache-2.0
URL:            https://github.com/moby/docker-image-spec
#!RemoteAsset:  sha256:64d792e78c099b90194d18281dcbb45d7ef5edde5ebbdf39978436d1e57b829e
Source0:        https://github.com/moby/docker-image-spec/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/opencontainers/image-spec)

Provides:       go(github.com/moby/docker-image-spec) = %{version}

Requires:       go(github.com/opencontainers/image-spec)

%description
Docker Image Specification v1 describes the legacy Docker image JSON and
manifest formats used by Docker Engine and related tooling.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
