# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cors
%define go_import_path  github.com/rs/cors
# Example programs integrate with optional third-party web frameworks.
%define go_test_exclude_glob %{go_import_path}/examples/*

Name:           go-github-rs-cors
Version:        1.11.1
Release:        %autorelease
Summary:        CORS middleware for Go HTTP servers
License:        MIT
URL:            https://github.com/rs/cors
#!RemoteAsset:  sha256:9dfa637cfee4547e7bd30b8216cb89de3a41e485ff19e63172b509e407f519cb
Source0:        https://github.com/rs/cors/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gin-gonic/gin)

Provides:       go(github.com/rs/cors) = %{version}

Requires:       go(github.com/gin-gonic/gin)

%description
Cors provides a net/http middleware that implements Cross-Origin Resource
Sharing for Go HTTP servers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
