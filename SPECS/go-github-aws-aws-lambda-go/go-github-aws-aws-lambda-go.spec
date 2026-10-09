# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-lambda-go
%define go_import_path  github.com/aws/aws-lambda-go

Name:           go-github-aws-aws-lambda-go
Version:        1.55.1
Release:        %autorelease
Summary:        Libraries for building AWS Lambda functions in Go
License:        Apache-2.0
URL:            https://github.com/aws/aws-lambda-go
#!RemoteAsset:  sha256:5e575db971788e50bae18a57d754eb414ed2c56cd881374d22811e747745d573
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
