# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vtprotobuf
%define go_import_path  github.com/planetscale/vtprotobuf
# The conformance test expects an external runner that is not shipped in the
# source tree: fork/exec conformance/conformance-test-runner: no such file or directory. - HNO3Miracle
%define go_test_exclude github.com/planetscale/vtprotobuf/conformance

Name:           go-github-planetscale-vtprotobuf-v0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Protocol buffer compiler plugin for optimized Go code
License:        BSD-3-Clause
URL:            https://github.com/planetscale/vtprotobuf
#!RemoteAsset:  sha256:b7335c741afc07885144bead9ca902cb6fcfca667668f0ad1af6ce310fc3ca32
Source0:        https://github.com/planetscale/vtprotobuf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/planetscale/vtprotobuf) = %{version}
Conflicts:      go(github.com/planetscale/vtprotobuf) >= 0.6.0

Requires:       go(google.golang.org/protobuf)

%description
vtprotobuf provides a Protocol Buffer compiler plugin that generates optimized
Go code.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
