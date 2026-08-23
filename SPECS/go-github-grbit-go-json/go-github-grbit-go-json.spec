# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-json
%define go_import_path  github.com/grbit/go-json
# Skip root package tests: Go 1.26 changes encoding/json error and map-key behavior.
# Skip benchmarks: cannot find package github.com/pquerna/ffjson/fflib/v1.
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/benchmarks
}

Name:           go-github-grbit-go-json
Version:        0.11.0
Release:        %autorelease
Summary:        Fast JSON encoder and decoder compatible with encoding/json
License:        MIT
URL:            https://github.com/grbit/go-json
#!RemoteAsset:  sha256:d0ca462d987caf17d590c1650fc1371c04924d9b1e99043de27d6fcf2c473fa1
Source0:        https://github.com/grbit/go-json/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects upstream non-constant and mismatched format strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/francoispqt/gojay)
BuildRequires:  go(github.com/mailru/easyjson)

Provides:       go(github.com/grbit/go-json) = %{version}

%description
Go-json provides a fast JSON encoder and decoder that is compatible with Go's
standard encoding/json package.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
