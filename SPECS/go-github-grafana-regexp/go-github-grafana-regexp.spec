# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           regexp
%define go_import_path  github.com/grafana/regexp
%define commit_id f7b3be9d18538c56fb03caa6088db55404e784e8

Name:           go-github-grafana-regexp
Version:        0+git20260607.f7b3be9
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
A fork of the upstream Go regexp package, with some code
optimisations to make it run faster.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
