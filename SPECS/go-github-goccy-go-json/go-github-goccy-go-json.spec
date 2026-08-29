# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-json
%define go_import_path  github.com/goccy/go-json

Name:           go-github-goccy-go-json
Version:        0.10.6
Release:        %autorelease
Summary:        Fast JSON encoder and decoder for Go
License:        MIT
URL:            https://github.com/goccy/go-json
#!RemoteAsset:  sha256:808f1c7fa10eaafda552f4709cac2ecc953dcda6a144050756c81a8e24d0a8c1
Source0:        https://github.com/goccy/go-json/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects non-constant fmt.Errorf format strings in tests.
# - HNO3Miracle
Patch2000:      2000-fix-test-non-constant-fmt-errorf.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/francoispqt/gojay)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/pquerna/ffjson)
BuildRequires:  go(github.com/segmentio/encoding)
BuildRequires:  go(github.com/valyala/fastjson)
BuildRequires:  go(github.com/wI2L/jettison)

Provides:       go(github.com/goccy/go-json) = %{version}

Requires:       go(github.com/francoispqt/gojay)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/pquerna/ffjson)

%description
This package provides a fast JSON encoder and decoder for Go.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
