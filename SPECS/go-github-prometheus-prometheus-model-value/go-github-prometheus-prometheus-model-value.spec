# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           prometheus-model-value
%define go_import_path  github.com/prometheus/prometheus/model/value

Name:           go-github-prometheus-prometheus-model-value
Version:        0.311.3
Release:        %autorelease
Summary:        Prometheus model value types for Go
License:        Apache-2.0
URL:            https://github.com/prometheus/prometheus
#!RemoteAsset:  sha256:5a61d9b1ce2cf2caf5606fedd0d9c46237740f87d74d2e1ff7115967af353046
Source0:        https://github.com/prometheus/prometheus/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n prometheus-0.311.3
# Package only this standard-library-only leaf path so packages that import
# github.com/prometheus/prometheus/model/value do not need to wait for the full
# Prometheus package dependency chain.

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/prometheus/prometheus/model/value) = %{version}

%description
This package provides the Prometheus model value types for Go.

%install
install -dm0755 %{buildroot}%{go_sys_gopath}/%{go_import_path}
cp -a model/value/*.go %{buildroot}%{go_sys_gopath}/%{go_import_path}/

%check
mkdir -p _build/src/github.com/prometheus/prometheus/model
cp -a model/value _build/src/%{go_import_path}
GO111MODULE=off GOPATH="$PWD/_build:%{_datadir}/gocode" go test -v %{go_import_path}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
