# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vtprotobuf
%define go_import_path  github.com/planetscale/vtprotobuf
# The conformance test expects an external runner that is not shipped in the
# source tree: fork/exec conformance/conformance-test-runner: no such file or directory. - HNO3Miracle
%define go_test_exclude github.com/planetscale/vtprotobuf/conformance

Name:           go-github-planetscale-vtprotobuf
Version:        0.6.0
Release:        %autorelease
Summary:        Protocol buffer compiler plugin for optimized Go code
License:        BSD-3-Clause
URL:            https://github.com/planetscale/vtprotobuf
#!RemoteAsset:  sha256:93ed5268bb2bbfe8c3aef008ba6d977a921b2ec62e7e78c762a8c1ae45c5a49c
Source0:        https://github.com/planetscale/vtprotobuf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/planetscale/vtprotobuf) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)

%description
vtprotobuf provides a Protocol Buffer compiler plugin that generates optimized
Go code.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
