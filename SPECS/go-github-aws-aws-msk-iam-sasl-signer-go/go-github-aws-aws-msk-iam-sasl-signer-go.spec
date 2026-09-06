# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-msk-iam-sasl-signer-go
%define go_import_path  github.com/aws/aws-msk-iam-sasl-signer-go

Name:           go-github-aws-aws-msk-iam-sasl-signer-go
Version:        1.0.4
Release:        %autorelease
Summary:        AWS MSK IAM SASL signer for Go
License:        Apache-2.0
URL:            https://github.com/aws/aws-msk-iam-sasl-signer-go
#!RemoteAsset:  sha256:e6a52d43315a72af309b80dffac4542841bdbaa61bd2312ffbea3faaa384c81b
Source0:        https://github.com/aws/aws-msk-iam-sasl-signer-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/aws/aws-sdk-go-v2)

%description
The AWS MSK IAM SASL signer generates authentication tokens for Go Kafka
clients connecting to Amazon Managed Streaming for Apache Kafka with IAM.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
