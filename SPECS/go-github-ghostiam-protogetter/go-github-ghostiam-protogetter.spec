# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protogetter
%define go_import_path  github.com/ghostiam/protogetter

Name:           go-github-ghostiam-protogetter
Version:        1.0.1
Release:        %autorelease
Summary:        Go analyzer for Protocol Buffers getter usage
License:        MIT
URL:            https://github.com/ghostiam/protogetter
#!RemoteAsset:  sha256:610d53d97919169776a8296a669f86bba85dd40f317b0f1f99df0977adc82ec7
Source0:        https://github.com/ghostiam/protogetter/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  go(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  go(google.golang.org/protobuf/types/gofeaturespb)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/ghostiam/protogetter) = %{version}
Provides:       go(github.com/ghostiam/protogetter/cmd/protogetter) = %{version}

Requires:       go(github.com/gobwas/glob)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for Protocol Buffers getter usage. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
