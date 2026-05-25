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
Patch0:         2000-fix-test-non-constant-fmt-errorf.patch
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-json-0.10.6

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/francoispqt/gojay)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/mailru/easyjson/jlexer)
BuildRequires:  go(github.com/mailru/easyjson/jwriter)
BuildRequires:  go(github.com/pquerna/ffjson/ffjson)
BuildRequires:  go(github.com/pquerna/ffjson/fflib/v1)
BuildRequires:  go(github.com/segmentio/encoding/json)
BuildRequires:  go(github.com/valyala/fastjson)
BuildRequires:  go(github.com/wI2L/jettison)

Provides:       go(github.com/goccy/go-json) = %{version}
Provides:       go(github.com/goccy/go-json/internal/decoder) = %{version}
Provides:       go(github.com/goccy/go-json/internal/encoder) = %{version}
Provides:       go(github.com/goccy/go-json/internal/encoder/vm) = %{version}
Provides:       go(github.com/goccy/go-json/internal/encoder/vm_color) = %{version}
Provides:       go(github.com/goccy/go-json/internal/encoder/vm_color_indent) = %{version}
Provides:       go(github.com/goccy/go-json/internal/encoder/vm_indent) = %{version}
Provides:       go(github.com/goccy/go-json/internal/errors) = %{version}
Provides:       go(github.com/goccy/go-json/internal/runtime) = %{version}
Provides:       go(github.com/goccy/go-json/test/cover) = %{version}
Provides:       go(github.com/goccy/go-json/test/example) = %{version}

Requires:       go(github.com/francoispqt/gojay)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/mailru/easyjson/jlexer)
Requires:       go(github.com/mailru/easyjson/jwriter)
Requires:       go(github.com/pquerna/ffjson/fflib/v1)


%description
This package provides a fast JSON encoder and decoder for Go.

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
