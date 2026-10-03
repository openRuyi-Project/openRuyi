# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aliyun-log-go-sdk
%define go_import_path  github.com/aliyun/aliyun-log-go-sdk
# The root, consumer, and producer suites require live Alibaba Cloud services;
# two example directories contain multiple standalone main programs.
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/consumer
    %{go_import_path}/example/config
    %{go_import_path}/example/etl
    %{go_import_path}/producer
}

Name:           go-github-aliyun-aliyun-log-go-sdk
Version:        0.1.100
Release:        %autorelease
Summary:        Alibaba Cloud Log Service SDK for Go
License:        MIT
URL:            https://github.com/aliyun/aliyun-log-go-sdk
#!RemoteAsset:  sha256:551a836a3b17f55dd443307c224c6783b6d254e6323e675dc5d70936030d7758
Source0:        https://github.com/aliyun/aliyun-log-go-sdk/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep retry callbacks compatible with the canonical generic backoff package.
Patch2000:      2000-use-function-callback-with-generic-backoff.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/zstd)
BuildRequires:  go(github.com/Netflix/go-env)
BuildRequires:  go(github.com/alibabacloud-go/alibabacloud-gateway-spi)
BuildRequires:  go(github.com/alibabacloud-go/darabonba-openapi/v2)
BuildRequires:  go(github.com/alibabacloud-go/debug)
BuildRequires:  go(github.com/alibabacloud-go/endpoint-util)
BuildRequires:  go(github.com/alibabacloud-go/openapi-util)
BuildRequires:  go(github.com/alibabacloud-go/sts-20150401/v2)
BuildRequires:  go(github.com/alibabacloud-go/tea)
BuildRequires:  go(github.com/alibabacloud-go/tea-utils)
BuildRequires:  go(github.com/alibabacloud-go/tea-utils/v2)
BuildRequires:  go(github.com/alibabacloud-go/tea-xml)
BuildRequires:  go(github.com/aliyun/credentials-go)
BuildRequires:  go(github.com/cenkalti/backoff)
BuildRequires:  go(github.com/clbanning/mxj/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/go-kit/kit)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tjfoc/gmsm)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/DataDog/zstd)
Requires:       go(github.com/Netflix/go-env)
Requires:       go(github.com/alibabacloud-go/darabonba-openapi/v2)
Requires:       go(github.com/alibabacloud-go/sts-20150401/v2)
Requires:       go(github.com/cenkalti/backoff)
Requires:       go(github.com/go-kit/kit)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/pkg/errors)
Requires:       go(go.uber.org/atomic)
Requires:       go(golang.org/x/net)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/natefinch/lumberjack.v2)

%description
The Alibaba Cloud Log Service SDK for Go provides APIs for sending, querying,
managing, and consuming logs from Alibaba Cloud Simple Log Service.

%files
%doc README.md README_EN.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
