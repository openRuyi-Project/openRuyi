# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml3
%define go_import_path  github.com/oasdiff/yaml3

Name:           go-github-oasdiff-yaml3
Version:        0.0.13
Release:        %autorelease
Summary:        YAML support for the Go language.
License:        MIT AND Apache-2.0
URL:            https://github.com/oasdiff/yaml3
#!RemoteAsset:  sha256:98cd6c83501c01789580bedf4213437babdefc7135179237dd8332bff52cc0f9
Source0:        https://github.com/oasdiff/yaml3/archive/refs/tags/v0.0.13.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n yaml3-0.0.13

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(github.com/oasdiff/yaml3) = %{version}


%description
YAML support for the Go language

Fork

This fork is an improved version of the go-yaml/yaml package, enhanced
to
inject __origin__ metadata into YAML mapping nodes during decoding,
recording the file, line, and column of each key.

To enable origin tracking, call Origin on the decoder before decoding:


%files
%doc README.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
