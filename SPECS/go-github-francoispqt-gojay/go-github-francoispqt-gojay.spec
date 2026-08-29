# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gojay
%define go_import_path  github.com/francoispqt/gojay
# embedded_struct tests compare JSON strings through assertly/toolbox; the
# current packaged assertly reports Payload "" as actual '""' vs expected ''. - HNO3Miracle
%define go_test_exclude_glob github.com/francoispqt/gojay/gojay/codegen/test/embedded_struct

Name:           go-github-francoispqt-gojay
Version:        1.2.13
Release:        %autorelease
Summary:        High performance JSON encoder/decoder with stream API for Golang
License:        MIT
URL:            https://github.com/francoispqt/gojay
#!RemoteAsset:  sha256:69de41c398b38217fbbb7e16a71893c7165bc8e59ba5d5b88b00db48f50cb3d5
Source0:        https://github.com/francoispqt/gojay/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-errors/errors)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/viant/assertly)
BuildRequires:  go(github.com/viant/toolbox)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/francoispqt/gojay) = %{version}

Requires:       go(github.com/go-errors/errors)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/viant/toolbox)
Requires:       go(golang.org/x/net)

%description
gojay provides a high-performance JSON encoder and decoder with streaming APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
