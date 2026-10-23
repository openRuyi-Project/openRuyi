# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           arangolint
%define go_import_path  go.augendre.info/arangolint

Name:           go-go.augendre-arangolint
Version:        0.4.0
Release:        %autorelease
Summary:        Go analyzer for ArangoDB query construction
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0
URL:            https://github.com/Crocmagnon/arangolint
#!RemoteAsset:  sha256:a20d966f2606686cc17a2769cea4b95a147a21730d779388a4d6f45b63a87320
Source0:        https://github.com/Crocmagnon/arangolint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n arangolint-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/arangodb/go-driver/v2)
BuildRequires:  go(github.com/arangodb/go-velocypack)
BuildRequires:  go(github.com/dchest/siphash)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/kkdai/maglev)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(go.augendre.info/arangolint) = %{version}
Provides:       go(go.augendre.info/arangolint/cmd/arangolint) = %{version}
Provides:       go(go.augendre.info/arangolint/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for ArangoDB query construction.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
