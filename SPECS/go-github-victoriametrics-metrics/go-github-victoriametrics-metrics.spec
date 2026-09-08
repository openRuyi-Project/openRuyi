# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           metrics
%define go_import_path  github.com/VictoriaMetrics/metrics

Name:           go-github-victoriametrics-metrics
Version:        1.44.0
Release:        %autorelease
Summary:        Metrics library for Go applications
License:        MIT
URL:            https://github.com/VictoriaMetrics/metrics
#!RemoteAsset:  sha256:fa739c706a64156f6d56693bb5252312999a15947f97142c629bd97b4f5c4194
Source0:        https://github.com/VictoriaMetrics/metrics/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep Prometheus label values quoted while formatting their integer value.
# https://github.com/VictoriaMetrics/metrics/pull/132
Patch0:         2000-tests-fix-histogram-label-formatting.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/valyala/histogram)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/VictoriaMetrics/metrics) = %{version}

Requires:       go(github.com/valyala/histogram)
Requires:       go(golang.org/x/sys)

%description
VictoriaMetrics metrics provides counters, gauges, histograms, summaries, and
Prometheus-compatible metric exposition for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
