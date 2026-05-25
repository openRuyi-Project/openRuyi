# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           image-spec
%define go_import_path  github.com/opencontainers/image-spec

Name:           go-github-opencontainers-image-spec
Version:        1.1.1
Release:        %autorelease
Summary:        OCI image format definitions for Go
License:        Apache-2.0
URL:            https://github.com/opencontainers/image-spec
#!RemoteAsset:  sha256:fff64f2ae3a11a307227d27ba599f1e56b436301c5a2faedd57907ac97d2ac94
Source0:        https://github.com/opencontainers/image-spec/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/russross/blackfriday)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v5)

Provides:       go(github.com/opencontainers/image-spec) = %{version}

Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/santhosh-tekuri/jsonschema/v5)

%description
image-spec provides Go definitions and schema helpers for the OCI image format.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
