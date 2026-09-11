# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mautrix
%define go_import_path  maunium.net/go/mautrix

Name:           go-maunium-go-mautrix
Version:        0.26.3
Release:        %autorelease
Summary:        Go framework for the Matrix protocol
License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/mautrix/go
#!RemoteAsset:  sha256:a9ae03675d9ce87a3b83e4efa37252d3cf3e57ef4a8c2b19cdfddf999e51af1f
Source0:        https://github.com/mautrix/go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.27 renamed JSON v2 unknown-member embedding; preserve event hashes.
Patch2000:      2000-pdu-support-json-v2-embed-tag.patch

# Live federation/DNS tests fail with lookup maunium.net or matrix.org on
# [::1]:53: connection refused in the offline OBS build.
BuildOption(check):  -skip '^(TestClient_Version|TestResolveServerName|TestServerKeyResponse_VerifySelfSignature)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(olm)
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go(github.com/chzyer/readline)
BuildRequires:  go(github.com/coder/websocket)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/rs/xid)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/skip2/go-qrcode)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/sjson)
BuildRequires:  go(github.com/yuin/goldmark)
BuildRequires:  go(go.mau.fi/util/base58)
BuildRequires:  go(go.mau.fi/util/configupgrade)
BuildRequires:  go(go.mau.fi/util/confusable)
BuildRequires:  go(go.mau.fi/util/curl)
BuildRequires:  go(go.mau.fi/util/dbutil)
BuildRequires:  go(go.mau.fi/util/exbytes)
BuildRequires:  go(go.mau.fi/util/exerrors)
BuildRequires:  go(go.mau.fi/util/exfmt)
BuildRequires:  go(go.mau.fi/util/exgjson)
BuildRequires:  go(go.mau.fi/util/exhttp)
BuildRequires:  go(go.mau.fi/util/exmaps)
BuildRequires:  go(go.mau.fi/util/exmime)
BuildRequires:  go(go.mau.fi/util/exslices)
BuildRequires:  go(go.mau.fi/util/exstrings)
BuildRequires:  go(go.mau.fi/util/exsync)
BuildRequires:  go(go.mau.fi/util/exzerolog)
BuildRequires:  go(go.mau.fi/util/fallocate)
BuildRequires:  go(go.mau.fi/util/glob)
BuildRequires:  go(go.mau.fi/util/jsonbytes)
BuildRequires:  go(go.mau.fi/util/jsontime)
BuildRequires:  go(go.mau.fi/util/progver)
BuildRequires:  go(go.mau.fi/util/ptr)
BuildRequires:  go(go.mau.fi/util/random)
BuildRequires:  go(go.mau.fi/util/requestlog)
BuildRequires:  go(go.mau.fi/util/retryafter)
BuildRequires:  go(go.mau.fi/util/variationselector)
BuildRequires:  go(go.mau.fi/zeroconfig)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(maunium.net/go/mauflag)

Provides:       go(maunium.net/go/mautrix) = %{version}

Requires:       pkgconfig(olm)
Requires:       go(filippo.io/edwards25519)
Requires:       go(github.com/chzyer/readline)
Requires:       go(github.com/coder/websocket)
Requires:       go(github.com/lib/pq)
Requires:       go(github.com/mattn/go-sqlite3)
Requires:       go(github.com/rs/xid)
Requires:       go(github.com/rs/zerolog)
Requires:       go(github.com/skip2/go-qrcode)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/sjson)
Requires:       go(github.com/yuin/goldmark)
Requires:       go(go.mau.fi/util/base58)
Requires:       go(go.mau.fi/util/configupgrade)
Requires:       go(go.mau.fi/util/confusable)
Requires:       go(go.mau.fi/util/curl)
Requires:       go(go.mau.fi/util/dbutil)
Requires:       go(go.mau.fi/util/exbytes)
Requires:       go(go.mau.fi/util/exerrors)
Requires:       go(go.mau.fi/util/exfmt)
Requires:       go(go.mau.fi/util/exgjson)
Requires:       go(go.mau.fi/util/exhttp)
Requires:       go(go.mau.fi/util/exmaps)
Requires:       go(go.mau.fi/util/exmime)
Requires:       go(go.mau.fi/util/exslices)
Requires:       go(go.mau.fi/util/exstrings)
Requires:       go(go.mau.fi/util/exsync)
Requires:       go(go.mau.fi/util/exzerolog)
Requires:       go(go.mau.fi/util/fallocate)
Requires:       go(go.mau.fi/util/glob)
Requires:       go(go.mau.fi/util/jsonbytes)
Requires:       go(go.mau.fi/util/jsontime)
Requires:       go(go.mau.fi/util/progver)
Requires:       go(go.mau.fi/util/ptr)
Requires:       go(go.mau.fi/util/random)
Requires:       go(go.mau.fi/util/requestlog)
Requires:       go(go.mau.fi/util/retryafter)
Requires:       go(go.mau.fi/util/variationselector)
Requires:       go(go.mau.fi/zeroconfig)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(maunium.net/go/mauflag)

%description
A Go implementation of the Matrix client-server API with application service
support, end-to-end encryption, federation helpers and bridge utilities.

# GOPATH defaults to the pre-Go-1.22 HTTP router, causing mock login HTTP 404.
# Enable method/wildcard routes required by the verification test server.
%check -p
export GODEBUG=httpmuxgo121=0

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
