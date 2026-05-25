# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           reference
%define go_import_path  github.com/distribution/reference

Name:           go-github-distribution-reference
Version:        0.6.0
Release:        %autorelease
Summary:        Docker and OCI image reference parser
License:        Apache-2.0
URL:            https://github.com/distribution/reference
#!RemoteAsset:  sha256:379bbf93dc3365a5c5fcd6c2538b63f21f9e5493a439b69999e01fad3de1ea39
Source0:        https://github.com/distribution/reference/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/opencontainers/go-digest)

Provides:       go(github.com/distribution/reference) = %{version}

Requires:       go(github.com/opencontainers/go-digest)

%description
Package reference parses and normalizes Docker and OCI image references.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
