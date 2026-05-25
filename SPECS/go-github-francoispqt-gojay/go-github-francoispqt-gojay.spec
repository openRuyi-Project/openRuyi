# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gojay
%define go_import_path  github.com/francoispqt/gojay

Name:           go-github-francoispqt-gojay
Version:        1.2.13
Release:        %autorelease
Summary:        high performance JSON encoder/decoder with stream API for Golang
License:        MIT
URL:            https://github.com/francoispqt/gojay
#!RemoteAsset:  sha256:69de41c398b38217fbbb7e16a71893c7165bc8e59ba5d5b88b00db48f50cb3d5
Source0:        https://github.com/francoispqt/gojay/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gojay-1.2.13
# embedded_struct tests compare JSON strings through assertly/toolbox; the
# current packaged assertly reports Payload "" as actual '""' vs expected ''.
%define go_test_exclude_glob github.com/francoispqt/gojay/gojay/codegen/test/embedded_struct

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-errors/errors)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/mailru/easyjson/jlexer)
BuildRequires:  go(github.com/mailru/easyjson/jwriter)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(github.com/viant/assertly)
BuildRequires:  go(github.com/viant/toolbox)
BuildRequires:  go(github.com/viant/toolbox/url)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/net/websocket)

Provides:       go(github.com/francoispqt/gojay) = %{version}
Provides:       go(github.com/francoispqt/gojay/benchmarks) = %{version}
Provides:       go(github.com/francoispqt/gojay/benchmarks/decoder) = %{version}
Provides:       go(github.com/francoispqt/gojay/benchmarks/encoder) = %{version}
Provides:       go(github.com/francoispqt/gojay/gojay/codegen) = %{version}
Provides:       go(github.com/francoispqt/gojay/gojay/codegen/test/annotated_struct) = %{version}
Provides:       go(github.com/francoispqt/gojay/gojay/codegen/test/basic_struct) = %{version}
Provides:       go(github.com/francoispqt/gojay/gojay/codegen/test/embedded_struct) = %{version}
Provides:       go(github.com/francoispqt/gojay/gojay/codegen/test/pooled_struct) = %{version}

Requires:       go(github.com/go-errors/errors)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/mailru/easyjson/jlexer)
Requires:       go(github.com/mailru/easyjson/jwriter)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/viant/toolbox)
Requires:       go(github.com/viant/toolbox/url)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/net/websocket)


%description
[Image: Build Status] (https://travis-
ci.org/francoispqt/gojay.svg?branch=master) (https://travis-
ci.org/francoispqt/gojay) [Image: codecov]
(https://codecov.io/gh/francoispqt/gojay/branch/master/graph/badge.svg)
(https://codecov.io/gh/francoispqt/gojay) [Image: Go Report Card]
(https://goreportcard.com/badge/github.com/francoispqt/gojay)
(https://goreportcard.com/report/github.com/francoispqt/gojay) [Image:
Go doc] (http://img.shields.io/badge/go-documentation-blue.
svg?style=flat-
square) (https://godoc.org/github.com/francoispqt/gojay) [Image: MIT
License] (https://img.shields.io/badge/license-mit-blue.svg?style=flat-

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
