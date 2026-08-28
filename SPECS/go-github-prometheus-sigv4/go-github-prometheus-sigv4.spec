# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sigv4
%define go_import_path  github.com/prometheus/sigv4

Name:           go-github-prometheus-sigv4
Version:        0.4.1
Release:        %autorelease
Summary:        AWS Signature Version 4 support for Prometheus
License:        Apache-2.0
URL:            https://github.com/prometheus/sigv4
#!RemoteAsset:  sha256:d2da42104b380d5a95711787b719e28081fc9244c91f83e78d0da4ab47292fda
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
