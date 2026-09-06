# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-json
%define go_import_path  github.com/grbit/go-json
# Benchmark packages depend on optional JSON implementation libraries that are
# not needed to build or test this package.
%define go_test_exclude_glob %{go_import_path}/benchmarks

Name:           go-github-grbit-go-json
Version:        0.11.0
Release:        %autorelease
Summary:        Fast JSON encoder/decoder compatible with encoding/json for Go
License:        MIT
URL:            https://github.com/grbit/go-json
#!RemoteAsset:  sha256:d0ca462d987caf17d590c1650fc1371c04924d9b1e99043de27d6fcf2c473fa1
Source0:        https://github.com/grbit/go-json/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream tests contain dynamic format strings incompatible with Go 1.26 vet.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/grbit/go-json) = %{version}

%description
Fast Go JSON encoder and decoder compatible with encoding/json.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
