# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sigv4
%define go_import_path  github.com/prometheus/sigv4

Name:           go-github-prometheus-sigv4
Version:        0.5.0
Release:        %autorelease
Summary:        AWS Signature Version 4 support for Prometheus
License:        Apache-2.0
URL:            https://github.com/prometheus/sigv4
#!RemoteAsset:  sha256:c5cc222b4a58af6b80162738151ed3c7639264f5365029e45dcd3af8aeee24b7
Source0:        https://github.com/prometheus/sigv4/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/prometheus/sigv4) = %{version}

Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/common)
Requires:       go(gopkg.in/yaml.v2)

%description
Sigv4 provides AWS Signature Version 4 request signing for Prometheus remote
storage integrations.

%files
%doc NOTICE README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
