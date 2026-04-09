# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-metrics
%define go_import_path  github.com/rcrowley/go-metrics
# Upstream does not provide git tags, use commit ID instead - Julian
%define commit_id 65e299d6c5c92718e672a9d2bc7f96e5b687eef8
# Test failure, may be cause by outdate code
%define go_test_ignore_failure 1

Name:           go-github-rcrowley-go-metrics
Version:        0+git20250401.65e299d
Release:        %autorelease
Summary:        Go port of Coda Hale's Metrics library
License:        BSD 2-Clause
URL:            https://github.com/rcrowley/go-metrics
#!RemoteAsset
Source0:        https://github.com/rcrowley/go-metrics/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stathat/go)
BuildSystem:    golangmodules

Provides:       go(github.com/rcrowley/go-metrics) = %{version}

%description
Go port of Coda Hale's Metrics library: https://github.com/dropwizard/metrics.

Documentation: http://godoc.org/github.com/rcrowley/go-metrics.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
