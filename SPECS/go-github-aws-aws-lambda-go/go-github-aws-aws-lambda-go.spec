# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-lambda-go
%define go_import_path  github.com/aws/aws-lambda-go

Name:           go-github-aws-aws-lambda-go
Version:        1.55.0
Release:        %autorelease
Summary:        Libraries for building AWS Lambda functions in Go
License:        Apache-2.0
URL:            https://github.com/aws/aws-lambda-go
#!RemoteAsset:  sha256:06c080cf35eb27ba2645bf9ac02c2f2cdb69b065b5b4d161218e1c28d7e746df
Source0:        https://github.com/aws/aws-lambda-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
AWS Lambda for Go provides libraries, event definitions, and runtime support
for implementing AWS Lambda functions in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
