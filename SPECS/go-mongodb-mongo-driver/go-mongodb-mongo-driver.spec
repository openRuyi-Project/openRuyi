# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mongo-driver
%define go_import_path  go.mongodb.org/mongo-driver

# Short mode omits integration tests. Also exclude the remaining fixtures that
# resolve test.build.10gen.cc or require MongoDB on localhost:27017.
%define skip_srv_polling ^(TestPollingSRVRecordsSpec|TestPollSRVRecords|TestPollingSRVRecordsLoadBalanced|TestPollSRVRecordsMaxHosts|TestPollSRVRecordsServiceName)$
%define skip_srv_options ^TestClientOptions$/^ApplyURI$/^(srvServiceName|srvMaxHosts)$|^TestURIOptionsSpec$/^srv-options$/^SRV_URI_with_
%define skip_srv_logging ^TestTopologyConstructionLogging$/^genuine_URIs$/^srv$

Name:           go-mongodb-mongo-driver
Version:        1.17.10
Release:        %autorelease
Summary:        MongoDB Go driver v1
License:        Apache-2.0
URL:            https://github.com/mongodb/mongo-go-driver
#!RemoteAsset:  sha256:e205a5d490b900ccdbdef228ee41bc478dfd88b34365ee5dde568e4f40249719
Source0:        https://github.com/mongodb/mongo-go-driver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Partial backport: https://github.com/mongodb/mongo-go-driver/pull/2522
Patch1000:      1000-fix-test-format-strings.patch

BuildOption(check):  -short
BuildOption(check):  -timeout=15m
BuildOption(check):  -skip '%{skip_srv_polling}|%{skip_srv_options}|%{skip_srv_logging}|^TestServerHeartbeatTimeout$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/montanaflynn/stats)
BuildRequires:  go(github.com/xdg-go/scram)
BuildRequires:  go(github.com/xdg-go/stringprep)
BuildRequires:  go(github.com/youmark/pkcs8)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sync)

Provides:       go(go.mongodb.org/mongo-driver) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/golang/snappy)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/montanaflynn/stats)
Requires:       go(github.com/xdg-go/scram)
Requires:       go(github.com/xdg-go/stringprep)
Requires:       go(github.com/youmark/pkcs8)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sync)

%description
The MongoDB Go driver provides BSON encoding, database operations,
authentication, connection pooling, and monitoring for Go applications.
This package supplies the v1 import path used by MinIO.

%prep -a
# Build against distribution Go packages rather than the upstream vendor copy.
rm -rf vendor
# These separate Go modules are live AWS Lambda and MongoDB leak-test harnesses.
# Module-mode root tests omit them; do not pull them into the GOPATH build.
rm -rf internal/test/faas/awslambda/mongodb internal/test/goleak

%check -p
# The BSON local-time test requires a local zone distinct from UTC.
export TZ=America/New_York

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
