# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: Apache-2.0

%define _name           runtime-tools
%define go_import_path  github.com/opencontainers/runtime-tools
# OBS can't reatch web
# The test will try to reatch
# https://raw.githubusercontent.com/opencontainers/runtime-spec/v1.0.1/schema/config-schema.json
%define go_test_exclude %{shrink:
    %{go_import_path}/generate
    %{go_import_path}/validate
}

Name:           go-github-opencontainers-runtime-tools
Version:        0.9.0
Release:        %autorelease
Summary:        OCI runtime validation and generation tools
License:        Apache-2.0
URL:            https://github.com/opencontainers/runtime-tools
#!RemoteAsset:  sha256:4c2978e9097a3c93648c8ecf4f785f728044cddf717686e0b05a9244a1ad273c
Source0:        https://github.com/opencontainers/runtime-tools/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-fix-nonconstant-logrus-format.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/opencontainers/runtime-tools) = %{version}
Provides:       go(github.com/opencontainers/runtime-tools/generate) = %{version}

%description
Runtime tools for validating and generating OCI runtime specifications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
