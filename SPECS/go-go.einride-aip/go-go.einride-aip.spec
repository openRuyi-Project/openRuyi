# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aip
%define go_import_path  go.einride.tech/aip

Name:           go-go.einride-aip
Version:        0.86.3
Release:        %autorelease
Summary:        Google API Improvement Proposal helpers for Go
License:        MIT
URL:            https://github.com/einride/aip-go
#!RemoteAsset:  sha256:844340a378dad0027a7b82f9d92a80f1549ee3d25969bf1ca2e569dd92df834b
Source0:        https://github.com/einride/aip-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/stoewer/go-strcase)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gotest.tools/v3)

Provides:       go(go.einride.tech/aip) = %{version}
Provides:       go(go.einride.tech/aip/examples/examplelibrary) = %{version}
Provides:       go(go.einride.tech/aip/fieldbehavior) = %{version}
Provides:       go(go.einride.tech/aip/fieldmask) = %{version}
Provides:       go(go.einride.tech/aip/filtering) = %{version}
Provides:       go(go.einride.tech/aip/filtering/exprs) = %{version}
Provides:       go(go.einride.tech/aip/ordering) = %{version}
Provides:       go(go.einride.tech/aip/pagination) = %{version}
Provides:       go(go.einride.tech/aip/proto/gen/einride/example/freight/v1) = %{version}
Provides:       go(go.einride.tech/aip/proto/gen/einride/example/syntax/v1) = %{version}
Provides:       go(go.einride.tech/aip/reflect/aipreflect) = %{version}
Provides:       go(go.einride.tech/aip/resourceid) = %{version}
Provides:       go(go.einride.tech/aip/resourcename) = %{version}
Provides:       go(go.einride.tech/aip/validation) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/stoewer/go-strcase)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gotest.tools/v3)

%description
AIP Go provides validation, filtering, pagination, and resource helpers
for implementing Google API Improvement Proposals.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
