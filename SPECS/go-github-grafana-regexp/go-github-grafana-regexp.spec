# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           regexp
%define go_import_path  github.com/grafana/regexp
%define commit_id f7b3be9d18538c56fb03caa6088db55404e784e8

Name:           go-github-grafana-regexp
Version:        0+git20250905.f7b3be9
Release:        %autorelease
Summary:        Faster version of the Go regexp package
License:        BSD-3-Clause
URL:            https://github.com/grafana/regexp
#!RemoteAsset:  sha256:7135966bafd0ba9bac8998d507bf6328d6ff3d6edbcfc6d7409c073236ca55b0
Source0:        https://github.com/grafana/regexp/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/grafana/regexp) = %{version}


%description
Grafana Go regexp package

This repo is a fork of the upstream Go regexp package, with some code
optimisations to make it run faster.

All the optimisations have been submitted upstream, but not yet merged.

All semantics are the same, and the optimised code passes all tests from
upstream.

The main branch is non-optimised: switch over to speedup
(https://github.com/grafana/regexp/tree/speedup) branch for the improved
code.

Benchmarks:

[Image: image] (https://user-
images.githubusercontent.com/8125524/152182951-856549ed-6044-4285-b799-
69b31f598e32.png)


%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
