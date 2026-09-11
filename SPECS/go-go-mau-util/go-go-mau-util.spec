# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           util
%define go_import_path  go.mau.fi/util

# These two tests fetch live emoji data: lookup raw.githubusercontent.com
# on [::1]:53 fails with connection refused in the offline OBS build.
%global go_test_flags_default -v -skip '^(TestAdd_Full|TestFullyQualify_Full)$'

Name:           go-go-mau-util
Version:        0.9.6
Release:        %autorelease
Summary:        Go utilities for mautrix and related projects
License:        MPL-2.0
URL:            https://github.com/mautrix/go-util
#!RemoteAsset:  sha256:2830aae953fea2cfb27a2dfa24896c45637908dbb8702e0818dd13ea01cb30b5
Source0:        https://github.com/mautrix/go-util/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DATA-DOG/go-sqlmock)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/petermattis/goid)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)
BuildRequires:  go(google.golang.org/protobuf/types)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(go.mau.fi/util) = %{version}
Provides:       go(go.mau.fi/util/base58) = %{version}
Provides:       go(go.mau.fi/util/configupgrade) = %{version}
Provides:       go(go.mau.fi/util/confusable) = %{version}
Provides:       go(go.mau.fi/util/curl) = %{version}
Provides:       go(go.mau.fi/util/dbutil) = %{version}
Provides:       go(go.mau.fi/util/exbytes) = %{version}
Provides:       go(go.mau.fi/util/exerrors) = %{version}
Provides:       go(go.mau.fi/util/exfmt) = %{version}
Provides:       go(go.mau.fi/util/exgjson) = %{version}
Provides:       go(go.mau.fi/util/exhttp) = %{version}
Provides:       go(go.mau.fi/util/exmaps) = %{version}
Provides:       go(go.mau.fi/util/exmime) = %{version}
Provides:       go(go.mau.fi/util/exslices) = %{version}
Provides:       go(go.mau.fi/util/exstrings) = %{version}
Provides:       go(go.mau.fi/util/exsync) = %{version}
Provides:       go(go.mau.fi/util/exzerolog) = %{version}
Provides:       go(go.mau.fi/util/fallocate) = %{version}
Provides:       go(go.mau.fi/util/glob) = %{version}
Provides:       go(go.mau.fi/util/jsonbytes) = %{version}
Provides:       go(go.mau.fi/util/jsontime) = %{version}
Provides:       go(go.mau.fi/util/progver) = %{version}
Provides:       go(go.mau.fi/util/ptr) = %{version}
Provides:       go(go.mau.fi/util/random) = %{version}
Provides:       go(go.mau.fi/util/requestlog) = %{version}
Provides:       go(go.mau.fi/util/retryafter) = %{version}
Provides:       go(go.mau.fi/util/variationselector) = %{version}

Requires:       go(github.com/mattn/go-sqlite3)
Requires:       go(github.com/petermattis/goid)
Requires:       go(github.com/rs/zerolog)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)
Requires:       go(google.golang.org/protobuf/types)
Requires:       go(gopkg.in/yaml.v3)

%description
Shared Go utilities for mautrix-go, bridges and related libraries, including
database helpers, configuration upgrades, HTTP utilities and logging.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
