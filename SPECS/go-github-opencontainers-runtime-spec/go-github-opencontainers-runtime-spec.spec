# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           runtime-spec
%define go_import_path  github.com/opencontainers/runtime-spec

Name:           go-github-opencontainers-runtime-spec
Version:        1.3.0
Release:        %autorelease
Summary:        OCI Runtime Specification
License:        Apache-2.0
URL:            https://github.com/opencontainers/runtime-spec
#!RemoteAsset:  sha256:136b36bd1087c38bb3202bb3b0421c241bde06f4aa6325da4d5dc03a23e68d1d
Source0:        https://github.com/opencontainers/runtime-spec/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/opencontainers/runtime-spec) = %{version}

# schema/ provides JSON-schema validation pulling xeipuuv/gojsonschema; downstream uses specs-go only.
%prep -a
rm -rf schema

%description
This package provides the Go types for the Open Container Initiative (OCI) Runtime Specification.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
