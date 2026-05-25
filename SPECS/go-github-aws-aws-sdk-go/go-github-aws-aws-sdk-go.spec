# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-sdk-go
%define go_import_path  github.com/aws/aws-sdk-go

Name:           go-github-aws-aws-sdk-go
Version:        1.55.8
Release:        %autorelease
Summary:        AWS SDK for Go
License:        Apache-2.0
URL:            https://github.com/aws/aws-sdk-go
#!RemoteAsset:  sha256:b862bc662d38bcb1cff65d47c65e82ddb6294debf7272a3f9107aee2c5134ce1
Source0:        https://github.com/aws/aws-sdk-go/archive/refs/tags/v1.55.8.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n aws-sdk-go-1.55.8

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/jmespath/go-jmespath)

Provides:       go(github.com/aws/aws-sdk-go) = %{version}
Provides:       go(github.com/aws/aws-sdk-go/aws) = %{version}
Provides:       go(github.com/aws/aws-sdk-go/aws/credentials) = %{version}
Provides:       go(github.com/aws/aws-sdk-go/aws/session) = %{version}
Provides:       go(github.com/aws/aws-sdk-go/service/kms) = %{version}
Provides:       go(github.com/aws/aws-sdk-go/service/s3) = %{version}
Provides:       go(github.com/aws/aws-sdk-go/service/s3/s3manager) = %{version}
Provides:       go(github.com/aws/aws-sdk-go/service/ssm) = %{version}

Requires:       go(github.com/jmespath/go-jmespath)

%description
This package provides AWS SDK for Go.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
