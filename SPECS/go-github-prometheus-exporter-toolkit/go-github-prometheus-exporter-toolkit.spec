# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           exporter-toolkit
%define go_import_path  github.com/prometheus/exporter-toolkit

Name:           go-github-prometheus-exporter-toolkit
Version:        0.17.1
Release:        %autorelease
Summary:        Utilities for Prometheus exporters
License:        Apache-2.0
URL:            https://github.com/prometheus/exporter-toolkit
#!RemoteAsset:  sha256:0df83ea5a8eb6c7a2d34c7bc561c85f14c55f53bf674bb6abc82f71e4c532bd6
Source0:        https://github.com/prometheus/exporter-toolkit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/kingpin/v2)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/mdlayher/vsock)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/time)

Provides:       go(github.com/prometheus/exporter-toolkit) = %{version}

Requires:       go(github.com/alecthomas/kingpin/v2)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/mdlayher/vsock)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/common)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/time)

%description
Exporter-toolkit provides common web server and TLS utilities for Prometheus
exporters.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
