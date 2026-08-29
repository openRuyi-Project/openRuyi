# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           otlptranslator
%define go_import_path  github.com/prometheus/otlptranslator

Name:           go-github-prometheus-otlptranslator
Version:        1.0.0
Release:        %autorelease
Summary:        Prometheus OTLP translator for Go
License:        Apache-2.0
URL:            https://github.com/prometheus/otlptranslator
#!RemoteAsset:  sha256:51efc9ed3e61af4192331dba2942bd6f919cc7af4b31c093c19e18d5ea8f3af1
Source0:        https://github.com/prometheus/otlptranslator/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/prometheus/otlptranslator) = %{version}

%description
This package provides Prometheus OTLP translator for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
