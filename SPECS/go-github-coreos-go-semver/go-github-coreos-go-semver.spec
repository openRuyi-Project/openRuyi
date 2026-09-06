# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-semver
%define go_import_path  github.com/coreos/go-semver

Name:           go-github-coreos-go-semver
Version:        0.3.1
Release:        %autorelease
Summary:        Semantic versioning library for Go
License:        Apache-2.0
URL:            https://github.com/coreos/go-semver
#!RemoteAsset:  sha256:22763890859bc980adb6698dd67e07493646bc6472e90369aa678d2a041cb1cb
Source0:        https://github.com/coreos/go-semver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
Go-semver parses, validates, and compares semantic version strings.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
